# Hiring Manager Tools

Spec files for AI-native people management.

---

## README for Humans

### What is this?

A CLI tool that turns your hiring specs (markdown files describing what you're looking for in a candidate) into structured interview prep packages powered by Claude. You write what matters for a role in plain English. The tool applies your priorities consistently to every candidate.

### Install & Run

```bash
pip install hiring-manager-tools
export ANTHROPIC_API_KEY=your-key

# Generate interview prep from a spec + resume
spec prep --spec hiring/senior-frontend-platform --resume ./resume.txt --pretty

# Lint a spec for bias and quality issues
spec lint --spec hiring/senior-frontend-platform --pretty

# List available specs
spec list --kind hiring --pretty

# Launch the web demo (localhost:8000)
spec web
```

### Write a Spec

Create a markdown file in `specs/hiring/`:

```markdown
---
kind: hiring
role: Senior Frontend Engineer
team: Platform
level: L5
version: 1
---

# What We're Looking For

I'd rather hire someone with 2 years at a real startup than
5 years at Google, unless the Google person can clearly
articulate what *they* built vs. what the team built.

## Must-Haves
- Shipped production React at scale (>100k users)
- Owned a frontend architecture decision that went wrong

## Anti-Patterns
- Can't explain tradeoffs in their own decisions
- Dismissive of accessibility or performance
```

Write it like you'd explain the role to a colleague. Be opinionated. The tool weights what you weight.

### What You Get Back

- **Candidate Snapshot** — 3-4 sentence summary of the candidate
- **Spec Alignment** — Item-by-item assessment against your criteria with confidence levels
- **Interview Questions** — 8-10 tailored questions with what to look for and red flags
- **Bias Check** — Flags any non-job-relevant factors that may have influenced the assessment

### What It Can't Do

- Score or rank candidates (by design — it helps you prepare, not decide)
- Work without an API key (all AI features need `ANTHROPIC_API_KEY`)
- Guarantee bias-free output (the bias check is transparency, not a guarantee)
- Replace your judgment (every output is input to a human decision)

### Extend It

- **Add specs:** Drop `.md` files in `specs/hiring/`, run `spec list` to verify
- **Lint your specs:** `spec lint` checks for bias risk, vagueness, legal issues
- **Web demo:** `spec web` → paste spec + resume in the browser, get instant results
- **MCP for Claude Desktop:** `spec serve` → use specs as resources inside Claude

### Spec Library

`specs/library/` contains ~160 ready-to-use hiring specs covering frontend, backend, full-stack, mobile, DevOps, data, ML, PM, design, and marketing roles across 4 levels — plus company-specific specs for Google, Apple, Amazon, Netflix, Meta, Stripe, and 9 more companies. See `specs/library/README.md` for the full catalog.

---

## README for Agents

The following sections provide detailed architectural context, extension patterns, and implementation details for AI agents and developers working with this codebase.

### Architecture

Hiring Manager Tools follows a strict four-layer architecture:

```
┌─────────────────────────────────────────────────┐
│  Interfaces: CLI, MCP Server, Web Demo          │  ← Thin transport layers
├─────────────────────────────────────────────────┤
│  Engine: execute(plan, spec) → ModuleResult     │  ← Orchestration + audit trail
├─────────────────────────────────────────────────┤
│  Modules: interview_prep, spec_lint             │  ← Prompt composition + schemas
├─────────────────────────────────────────────────┤
│  Core: SpecFile, Registry, ClaudeClient         │  ← Types + loading + API wrapper
└─────────────────────────────────────────────────┘
```

**Data flow for every operation:**

1. Interface receives a request (CLI args, MCP tool call, HTTP POST)
2. `load_spec()` or `parse_spec()` produces a `SpecFile`
3. `Registry.resolve()` finds the right `Module` for the action + spec kind
4. `Module.plan()` composes the prompt and returns an `InvocationPlan`
5. `Engine.execute()` sends the plan to Claude via `ClaudeClient`, records a `RunRecord`, and returns a `ModuleResult`
6. Interface formats and returns the result

No business logic lives in the interfaces. No Claude-specific logic lives in the modules. No module-specific logic lives in the engine.

### Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| **Structured output via tool_use** | Claude's `tool_choice` guarantees JSON conforming to a schema. No regex parsing, no "please return JSON" prompting. |
| **Prompt templates as markdown files** | Prompts are versioned separately from code. Anyone can read `prompts/interview_prep.md` and understand what Claude is asked to do. |
| **Meta block on every output** | Every result includes spec version, prompt version, model, timestamp, and run ID. This is the audit trail. |
| **No database** | Specs are files on disk. Run records are append-only JSONL. Git is the version control system. |
| **No resume screening** | Deliberate architectural boundary. Prep helps humans prepare; screening replaces human judgment. |

### What's Built

| Component | File(s) | Description |
|-----------|---------|-------------|
| Spec Parser | `speckit/spec.py` | `SpecFile` dataclass, YAML frontmatter parsing, section splitting by H2, `load_spec()`, `parse_spec()`, `list_specs()` |
| Validation | `speckit/validation.py` | Structural checks (no API calls). Required fields per kind, unknown kind warnings |
| Engine | `speckit/engine.py` | Executes `InvocationPlan`s, records runs to JSONL, builds meta blocks |
| Claude Client | `speckit/claude_client.py` | Thin Anthropic SDK wrapper. `tool_use` with forced `tool_choice` for structured JSON |
| Registry | `speckit/registry.py` | Maps module names to instances, validates spec-kind compatibility |
| Run Records | `speckit/run_record.py` | `RunRecord` dataclass, JSONL persistence to `.speckit/runs/YYYY-MM-DD.jsonl` |
| Module ABC | `speckit/modules/base.py` | `Module`, `InvocationPlan`, `ModuleResult`. Prompt template loading helpers |
| Interview Prep | `speckit/modules/interview_prep.py` | Hiring spec + resume → snapshot, alignment, questions, bias check |
| Spec Lint | `speckit/modules/spec_lint.py` | Any spec → issues (bias_risk, vagueness, legal_risk, missing_section, clarity) |
| CLI | `speckit/cli.py` | Click-based. `prep`, `lint`, `list`, `serve`, `web` |
| MCP Server | `speckit/mcp_server.py` | Resources (`spec://kind/name`) + Tools (`prepare_interview`, `lint_spec`, `list_specs`) |
| Web Demo | `speckit/web/app.py`, `speckit/web/static/index.html` | FastAPI + single-file dark-mode UI |
| Eval: Consistency | `evals/test_consistency.py` | Same input 3x, assert structural stability |
| Eval: Bias Swap | `evals/test_bias_swap.py` | 4 name variants, assert identical assessments |
| Eval: Lint | `evals/test_spec_lint.py` | Known-bad specs → correct flags |

### Output Schemas

**Interview Prep (`interview_prep` module):**
- `candidate_snapshot`: string (3-4 sentences)
- `spec_alignment`: array of `{criterion, signal, confidence, follow_up}` — confidence is `strong|moderate|weak|no_signal`
- `recommended_questions`: array of `{question, category, seeks, good_answer_looks_like, red_flags}` — category is `technical_depth|experience_verification|culture_and_collaboration|growth_areas`
- `bias_check`: `{flags: string[], note: string}`

**Spec Lint (`spec_lint` module):**
- `issues`: array of `{level, category, text, suggestion}` — level is `error|warning|suggestion`, category is `bias_risk|vagueness|missing_section|legal_risk|clarity|completeness`
- `summary`: string (2-3 sentences)
- `overall_quality`: `strong|adequate|needs_work|problematic`

### Adding a New Module

1. Create `speckit/modules/your_module.py` implementing the `Module` ABC:

```python
from speckit.modules.base import Module, InvocationPlan

class YourModule(Module):
    @property
    def name(self) -> str:
        return "your_module"

    @property
    def supported_kinds(self) -> list[str]:
        return ["hiring"]

    def input_schema(self) -> dict:
        return {"type": "object", "required": ["your_input"], "properties": {...}}

    def plan(self, spec, inputs: dict) -> InvocationPlan:
        system_prompt = self._load_prompt_template()
        user_message = f"Spec:\n{spec.body}\n\nInput:\n{inputs['your_input']}"
        return InvocationPlan(
            system_prompt=system_prompt,
            messages=[{"role": "user", "content": user_message}],
            tool_schema=self.output_schema(),
            prompt_version=self._get_prompt_version(),
        )

    def output_schema(self) -> dict:
        return {"type": "object", "required": ["result"], "properties": {...}}
```

2. Create `prompts/your_module.md` with YAML frontmatter (`prompt_version`, `module`).
3. Register in `speckit/registry.py` → `create_default_registry()`.
4. Add CLI command in `speckit/cli.py` and MCP tool in `speckit/mcp_server.py`.

### Adding a New Spec Kind

1. Add the kind to `VALID_KINDS` in `speckit/validation.py`.
2. Add kind-specific required fields to `validate_spec_structure()`.
3. Create `specs/{kind}/` with example specs.
4. Write a module that includes the new kind in `supported_kinds`.

### Error Handling

Exception hierarchy rooted at `SpecKitError`:

| Exception | When |
|-----------|------|
| `SpecValidationError` | Spec fails structural validation |
| `UnknownModuleError` | Requested module doesn't exist |
| `IncompatibleSpecError` | Module doesn't support the spec's kind |
| `EngineError` | Claude didn't return structured output |

### What's Not Built (by design)

- No authentication or user management
- No database (files + JSONL + Git)
- No candidate scoring or ranking
- No ATS/HRIS integrations (MCP server is the integration surface)
- No build step for web UI (single HTML file, vanilla JS)
- No multi-model abstraction (Claude only)
- No Docker/k8s config

### MCP Server Setup

```json
{
  "mcpServers": {
    "hiring-manager-tools": {
      "command": "spec",
      "args": ["serve"],
      "env": {
        "ANTHROPIC_API_KEY": "your-key"
      }
    }
  }
}
```

**Resources:** `spec://hiring/*`, `spec://hiring/senior-frontend-platform`

**Tools:** `prepare_interview(spec_ref, resume_text)`, `lint_spec(spec_ref)`, `list_specs(kind?)`

### Development

```bash
git clone https://github.com/SchoolMarm22/Hiring-Manager-Tools.git
cd Hiring-Manager-Tools
pip install -e ".[dev]"
make test          # Non-slow tests (no API key needed)
make test-all      # Full eval suite (~$0.50-1.00)
make test-bias     # Bias swap tests (~$0.30)
```

### Project Structure

```
├── speckit/                 # Python package
│   ├── __init__.py          # Public API + exceptions
│   ├── spec.py              # SpecFile dataclass, loader, parser
│   ├── validation.py        # Structural validation
│   ├── engine.py            # Plan execution + audit
│   ├── registry.py          # Module registry
│   ├── claude_client.py     # Anthropic SDK wrapper
│   ├── run_record.py        # RunRecord + JSONL
│   ├── cli.py               # CLI (click)
│   ├── mcp_server.py        # MCP server
│   ├── modules/
│   │   ├── base.py          # Module ABC
│   │   ├── interview_prep.py
│   │   └── spec_lint.py
│   └── web/
│       ├── app.py           # FastAPI
│       └── static/index.html
├── specs/                   # Example + library specs
├── prompts/                 # Versioned prompt templates
├── evals/                   # Eval suite (real API calls)
├── ARCHITECTURE.md          # Deep architecture docs
├── SPEC_FORMAT.md           # Format RFC
└── pyproject.toml
```

### Philosophy

- The architecture is the ethics — no screening module is a design decision, not a gap.
- Structured output is for auditability, not convenience.
- Bias tests run in CI, not in a compliance PDF.
- The spec is the source of truth. The AI is the executor. The human is the decision-maker.

## License

MIT
