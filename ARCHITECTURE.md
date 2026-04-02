# Architecture

This document describes SpecKit's internal architecture, data flow, and design rationale. Read this if you want to contribute, extend, or understand why things are built the way they are.

## System Overview

SpecKit is a four-layer system. Each layer has a single responsibility and a clean API boundary.

```
┌──────────────────────────────────────────────────────────────┐
│  Layer 3: Interfaces                                         │
│  CLI (click) · MCP Server (mcp SDK) · Web Demo (FastAPI)     │
│  Responsibility: Transport only. No business logic.          │
├──────────────────────────────────────────────────────────────┤
│  Layer 2.5: Modules                                          │
│  interview_prep · spec_lint                                  │
│  Responsibility: Prompt composition + output schema.         │
├──────────────────────────────────────────────────────────────┤
│  Layer 2: Engine                                             │
│  Engine · ClaudeClient · RunRecord · Registry                │
│  Responsibility: Plan execution, API calls, audit logging.   │
├──────────────────────────────────────────────────────────────┤
│  Layer 1: Spec Files                                         │
│  SpecFile · Loader · Validation                              │
│  Responsibility: Parse, validate, list spec files.           │
└──────────────────────────────────────────────────────────────┘
```

## Data Flow

Every operation follows the same path:

```
Request → SpecFile → Module.plan() → InvocationPlan → Engine.execute() → ModuleResult → Response
```

Concrete example for `speckit prep`:

```
1. CLI parses --spec and --resume args
2. load_spec("specs/hiring/senior-frontend-platform.md") → SpecFile
3. registry.resolve("interview_prep", "hiring") → InterviewPrepModule
4. module.plan(spec, {"resume_text": "..."}) → InvocationPlan
   └─ Loads prompts/interview_prep.md as system prompt
   └─ Injects spec body + resume into user message
   └─ Attaches output_schema() as tool definition
5. engine.execute(plan, spec, "interview_prep") → ModuleResult
   └─ Creates RunRecord (status: "running")
   └─ ClaudeClient.invoke() sends to Anthropic API with tool_use
   └─ Claude returns structured JSON via tool call
   └─ RunRecord marked "success", appended to .speckit/runs/YYYY-MM-DD.jsonl
   └─ ModuleResult contains output + meta block
6. CLI serializes result as JSON to stdout
```

## Layer 1: Spec Files

### SpecFile Dataclass

```python
@dataclass
class SpecFile:
    kind: str                       # "hiring", "review", etc.
    metadata: dict                  # All YAML frontmatter fields
    body: str                       # Full markdown body (no frontmatter)
    sections: dict[str, str]        # Normalized section key → content
    source_path: str | None         # None if parsed from raw text
    version: int                    # From frontmatter, defaults to 1
```

### Loader Design

The loader is intentionally simple:

- **YAML parsing:** `pyyaml` for frontmatter. No custom YAML extensions.
- **Section splitting:** Regex split on `\n## ` (not a markdown parser). This avoids a heavy dependency and handles real-world markdown reliably.
- **Section normalization:** Headings are lowercased, non-alphanumeric chars become underscores. `## Must-Haves` → `must_haves`.
- **Two entry points:** `load_spec(path)` for file-backed specs, `parse_spec(text)` for the web demo paste flow.

### Validation

`validate_spec_structure()` is fast, deterministic, and makes zero API calls. It checks:

- Required fields present for the spec's `kind`
- `kind` is in the known set (warns but doesn't reject unknown kinds)
- Missing recommended sections (suggestions, not errors)

This is separate from the AI-powered spec lint, which uses Claude to analyze content quality.

## Layer 2: Engine

### ClaudeClient

The thinnest possible wrapper around the Anthropic SDK:

```python
client.invoke(system_prompt, messages, tool_schema) → dict
```

It uses `tool_choice={"type": "tool", "name": "structured_output"}` to force Claude to return structured JSON matching the provided schema. No retry logic. No multi-provider abstraction. No prompt caching. This is intentional — complexity should be earned, not anticipated.

### Engine

The engine is module-agnostic. It receives an `InvocationPlan` and returns a `ModuleResult`. It doesn't know what interview prep is or what a lint check does. Its responsibilities:

1. Create a `RunRecord` before the API call
2. Call `ClaudeClient.invoke()` with the plan's parameters
3. Build the meta block (spec version, prompt version, model, timestamp, run ID)
4. Mark the run as success or failure
5. Persist the run record to JSONL

### RunRecord

Every engine execution produces a `RunRecord` persisted to `.speckit/runs/YYYY-MM-DD.jsonl`. Fields:

- `run_id` — UUID
- `module_name` — Which module ran
- `spec_path`, `spec_version` — Which spec was used
- `prompt_version` — Which prompt template version
- `model` — Which Claude model
- `started_at`, `completed_at` — Timestamps
- `status` — "running", "success", or "failed"
- `error` — Error message if failed

This is the audit trail. You can reconstruct exactly what produced any output.

### Registry

Maps module names to `Module` instances. `resolve(action, spec_kind)` validates that the module supports the requested spec kind before returning it. This prevents runtime errors like trying to lint-check a spec kind that the lint module hasn't been designed for.

## Layer 2.5: Modules

### Module ABC

Every module implements five methods:

| Method | Returns | Purpose |
|--------|---------|---------|
| `name` | `str` | Module identifier |
| `supported_kinds` | `list[str]` | Which spec kinds this module handles |
| `input_schema()` | `dict` | JSON Schema for required inputs beyond the spec |
| `plan(spec, inputs)` | `InvocationPlan` | Compose the full Claude request |
| `output_schema()` | `dict` | JSON Schema for the structured output |

The base class provides two helpers:
- `_load_prompt_template()` — Reads `prompts/{name}.md`, strips frontmatter, returns the body
- `_get_prompt_version()` — Extracts `prompt_version` from the template's frontmatter

### Prompt Templates

Prompt templates live in `prompts/` as markdown files with YAML frontmatter:

```markdown
---
prompt_version: "0.1.0"
module: interview_prep
---

You are an expert interview preparation assistant...
```

The frontmatter provides versioning. The body becomes the system prompt. Prompts are intentionally readable — anyone should be able to open the file and understand what Claude is being told to do.

### Interview Prep Module

**Input:** A hiring spec + a candidate resume (plain text).

**Output:** A structured JSON package containing:
- `candidate_snapshot` — 3-4 sentence summary
- `spec_alignment` — Item-by-item assessment (criterion, signal, confidence, follow-up)
- `recommended_questions` — 8-10 tailored questions with category, intent, good answers, red flags
- `bias_check` — Flags for non-job-relevant factors + summary note

**Confidence levels:** `strong`, `moderate`, `weak`, `no_signal`

**Question categories:** `technical_depth`, `experience_verification`, `culture_and_collaboration`, `growth_areas`

### Spec Lint Module

**Input:** Any spec file (all kinds supported).

**Output:** A structured JSON report containing:
- `issues` — Array of findings, each with level, category, text, suggestion
- `summary` — 2-3 sentence assessment
- `overall_quality` — `strong`, `adequate`, `needs_work`, `problematic`

**Issue categories:** `bias_risk`, `vagueness`, `missing_section`, `legal_risk`, `clarity`, `completeness`

## Layer 3: Interfaces

### CLI (`speckit/cli.py`)

Built with Click. Five commands:

| Command | API Calls | Description |
|---------|-----------|-------------|
| `speckit prep` | Yes | Generate interview prep |
| `speckit lint` | Yes | Structural + AI lint |
| `speckit list` | No | List specs as JSON |
| `speckit serve` | No (server) | Start MCP server |
| `speckit web` | No (server) | Start web demo |

All commands output JSON. Use `--pretty` for indented output. Pipe through `jq` for filtering.

### MCP Server (`speckit/mcp_server.py`)

Uses the official `mcp` Python SDK. Exposes:

- **Resources:** Spec files as `spec://{kind}/{name}` URIs
- **Tools:** `prepare_interview`, `lint_spec`, `list_specs`

The MCP server is a transport layer. It translates MCP protocol calls into engine calls and returns results in MCP format. No business logic.

### Web Demo (`speckit/web/`)

FastAPI app with two API endpoints (`/api/prep`, `/api/lint`) and a single-file HTML UI. The web demo accepts raw text paste for both spec and resume — it uses `parse_spec()` instead of `load_spec()`, so there's no dependency on the filesystem. Zero setup for trying SpecKit.

## Eval Suite

### Design Principle

Evals make real API calls and validate real Claude behavior. These are not mocks. The eval suite tests that the system produces useful, consistent, and fair output.

### Test Categories

**Consistency (`evals/test_consistency.py`):**
Run the same spec + resume through interview prep 3 times. Assert structural stability:
- Same question categories appear
- Confidence levels within ±1 step
- At least 70% criteria overlap
- Question counts stable (±2)

**Bias Swap (`evals/test_bias_swap.py`):**
Swap the candidate name across 4 demographic variants (James Mitchell, DeShawn Washington, Mei-Lin Chen, Priya Patel). Assert:
- Identical confidence levels
- Same category distributions (±1)
- No differential red-flag language
- Consistent bias check results

**Lint Validation (`evals/test_spec_lint.py`):**
Feed known-bad specs and verify correct issue detection:
- "Culture fit" → `bias_risk` warning
- "Native English speaker" → flagged
- Missing anti-patterns → `missing_section` suggestion
- Clean spec → no errors, strong/adequate quality

### Running Evals

```bash
make test          # Non-slow tests only (no API calls)
make test-all      # Full suite (~$0.50-1.00 in API costs)
make test-bias     # Bias swap tests only (~$0.30)
```

## Error Handling

Custom exception hierarchy rooted at `SpecKitError`:

| Exception | When |
|-----------|------|
| `SpecValidationError` | Spec fails structural validation |
| `UnknownModuleError` | Requested module doesn't exist |
| `IncompatibleSpecError` | Module doesn't support the spec's kind |
| `EngineError` | Claude didn't return expected structured output |

All errors include actionable messages: "Spec file missing required field 'role' for kind 'hiring'" not "Validation error."

## What's Deliberately Not Here

- **No authentication.** This is a tool, not a platform.
- **No database.** Files on disk + JSONL. Git is version control.
- **No candidate scoring or ranking.** Architectural boundary, not a missing feature.
- **No multi-provider abstraction.** Claude only. The Anthropic SDK is the only AI dependency.
- **No build step for the web UI.** Single HTML file, vanilla JS, no npm.
- **No Docker/k8s config.** Runs locally. `pip install` and go.
- **No retry logic in ClaudeClient.** The Anthropic SDK handles retries. Don't add a layer.
