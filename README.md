# SpecKit

Spec files for AI-native people management.

## What This Is

Spec files are natural language documents that configure how AI behaves in people management workflows — hiring, reviews, onboarding, team management. SpecKit is an open-source engine that parses spec files, applies them through Claude, and produces structured, auditable output. It ships with one reference module (interview prep), a spec linter, a CLI, an MCP server for Claude Desktop, and an eval suite that tests for consistency and bias.

## The Insight

There's a gap between how we configure AI for code and how we configure AI for people. In the coding world, we've learned that natural language configuration works — prompts, specs, system instructions. The equivalent for people management doesn't exist yet. HR tools still use dropdowns and checkboxes. A hiring manager can't express "I want startup experience because full-stack at a 5-person company means something different than full-stack at Meta" through a form field. But they can write it in a spec, and Claude can apply it consistently to 500 candidates.

Spec files are to people management what config files are to infrastructure — human-readable, version-controlled documents that make AI behavior consistent, auditable, and manager-controlled.

## Quick Start

```bash
# Clone and install
git clone https://github.com/yourusername/speckit.git
cd speckit
pip install -e ".[dev]"

# Set your API key
export ANTHROPIC_API_KEY=your-key

# Generate interview prep from a spec + resume
speckit prep --spec hiring/senior-frontend-platform --resume ./resume.txt --pretty

# Lint a spec for bias and quality
speckit lint --spec hiring/senior-frontend-platform --pretty

# List available specs
speckit list --kind hiring --pretty

# Start the MCP server (for Claude Desktop)
speckit serve

# Start the web demo (localhost:8000)
speckit web
```

## The Spec File Format

A spec file is a markdown file with YAML frontmatter. The frontmatter is machine-readable metadata. The body is natural language that Claude reads and applies.

```markdown
---
kind: hiring
role: Senior Frontend Engineer
team: Platform
level: L5
version: 2
---

# What We're Looking For

Prefer candidates with real startup experience...

## Must-Haves
- Shipped production React at scale (>100k users)
- Owned a frontend architecture decision that went wrong

## Anti-Patterns
- Can't explain tradeoffs in their own decisions
- Dismissive of accessibility or performance
```

See [SPEC_FORMAT.md](SPEC_FORMAT.md) for the full format specification.

## Architecture

SpecKit follows a strict layered architecture where each layer has a single responsibility:

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

No business logic lives in the interfaces. No Claude-specific logic lives in the modules. No module-specific logic lives in the engine. Each function does one thing.

### Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| **Structured output via tool_use** | Claude's `tool_choice` guarantees JSON conforming to a schema. No regex parsing, no "please return JSON" prompting. |
| **Prompt templates as markdown files** | Prompts are versioned separately from code. Anyone can read `prompts/interview_prep.md` and understand what Claude is asked to do. |
| **Meta block on every output** | Every result includes spec version, prompt version, model, timestamp, and run ID. This is the audit trail. |
| **No database** | Specs are files on disk. Run records are append-only JSONL. Git is the version control system. |
| **No resume screening** | Interview prep helps humans prepare better questions. Screening replaces human judgment with AI judgment. That's a different product with different risk. This is a deliberate architectural boundary. |

## What's Built

- **Interview Prep module** — spec + resume → structured interview package with candidate snapshot, spec alignment, tailored questions, and bias check
- **Spec Lint module** — analyzes specs for bias risk, vagueness, legal risk, missing sections, and clarity issues
- **CLI** — `speckit prep`, `speckit lint`, `speckit list`, `speckit serve`, `speckit web`
- **MCP Server** — expose specs as resources and tools for Claude Desktop
- **Web Demo** — single-file dark-mode UI; paste a spec and resume, get instant results
- **Eval suite** — consistency tests, bias swap tests, lint validation

## What's Not Built (Yet)

The spec format supports the full employee lifecycle. These modules are designed but not yet implemented:

- **Resume Screening** — Deliberately not built. Interview prep helps humans prepare. Screening replaces human judgment. That's a different product with different risk.
- **Onboarding Plans** — Generate personalized onboarding from team specs + interview signal
- **1:1 Prep** — Synthesize previous notes, work patterns, and growth goals before each meeting
- **Review Evidence Assembly** — Continuous evidence collection for performance reviews
- **Offboarding Knowledge Capture** — Structured exit interviews with cross-departure synthesis

## What It Cannot Do

Being explicit about limitations:

- **Cannot score or rank candidates.** The interview prep module produces a preparation package for the interviewer. It does not output a hire/no-hire recommendation or a numerical score.
- **Cannot operate without an API key.** All AI-powered features (prep, lint) require `ANTHROPIC_API_KEY`. The `list` command works offline.
- **Cannot guarantee bias-free output.** The bias swap eval tests for demographic consistency, but no system can fully eliminate bias. The bias check in every output is a transparency tool, not a guarantee.
- **Cannot replace human judgment.** Every output is structured as input to a human decision-maker, not as a decision itself.
- **Cannot integrate with ATS/HRIS systems directly.** The MCP server is the integration surface. External connectors (Greenhouse, Workday, etc.) would be built on top.

## Extending SpecKit

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
        return ["hiring"]  # Which spec kinds this works with

    def input_schema(self) -> dict:
        return {
            "type": "object",
            "required": ["your_input"],
            "properties": {
                "your_input": {"type": "string", "description": "..."}
            }
        }

    def plan(self, spec, inputs: dict) -> InvocationPlan:
        system_prompt = self._load_prompt_template()
        user_message = f"Your spec:\n{spec.body}\n\nYour input:\n{inputs['your_input']}"
        return InvocationPlan(
            system_prompt=system_prompt,
            messages=[{"role": "user", "content": user_message}],
            tool_schema=self.output_schema(),
            prompt_version=self._get_prompt_version(),
        )

    def output_schema(self) -> dict:
        return {
            "type": "object",
            "required": ["result"],
            "properties": {
                "result": {"type": "string", "description": "..."}
            }
        }
```

2. Create `prompts/your_module.md` with YAML frontmatter containing `prompt_version`.

3. Register it in `speckit/registry.py`:

```python
def create_default_registry() -> ModuleRegistry:
    registry = ModuleRegistry()
    registry.register(InterviewPrepModule())
    registry.register(SpecLintModule())
    registry.register(YourModule())  # Add here
    return registry
```

4. Add a CLI command in `speckit/cli.py` and corresponding MCP tool in `speckit/mcp_server.py`.

### Adding a New Spec Kind

1. Add the kind to `VALID_KINDS` in `speckit/validation.py`.
2. Add kind-specific required fields to `validate_spec_structure()`.
3. Create a `specs/{kind}/` directory with example specs.
4. Write a module that lists the new kind in its `supported_kinds`.

### Writing Your Own Specs

Specs are just markdown files with YAML frontmatter. Place them in `specs/{kind}/`:

```bash
# Create a new spec
mkdir -p specs/hiring
cat > specs/hiring/my-role.md << 'EOF'
---
kind: hiring
role: My Role Title
team: My Team
level: L4
version: 1
---

# What We're Looking For
...
EOF

# Verify it loads
speckit list --kind hiring --pretty

# Run it
speckit prep --spec hiring/my-role --resume ./candidate.txt --pretty
```

## Philosophy

- **The architecture is the ethics.** The decision not to build screening isn't a gap — it's a design decision. Interview prep helps interviewers prepare better questions. Screening replaces human judgment with AI judgment. We build the former.
- **Structured output isn't just for convenience — it's for auditability.** Every output includes a meta block with the spec version, prompt version, model, and timestamp that produced it.
- **Bias tests are in CI, not in a compliance PDF.** The eval suite runs real API calls that test for demographic bias in outputs.
- **The spec is always the source of truth.** The AI is always the executor. The human is always the decision-maker.

## MCP Setup

Add SpecKit to your Claude Desktop configuration (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "speckit": {
      "command": "speckit",
      "args": ["serve"],
      "env": {
        "ANTHROPIC_API_KEY": "your-key"
      }
    }
  }
}
```

Then in Claude Desktop, you can:
- Browse specs as resources (`spec://hiring/senior-frontend-platform`)
- Use the `prepare_interview` tool with a spec reference and resume text
- Use the `lint_spec` tool to analyze spec quality
- Use the `list_specs` tool to discover available specs

### MCP Resources

| URI Pattern | Description |
|-------------|-------------|
| `spec://hiring/*` | All hiring specs |
| `spec://review/*` | All review specs |
| `spec://hiring/senior-frontend-platform` | A specific spec's full content |

### MCP Tools

| Tool | Parameters | Returns |
|------|-----------|---------|
| `prepare_interview` | `spec_ref` (string), `resume_text` (string) | Full interview prep JSON |
| `lint_spec` | `spec_ref` (string) | Lint results JSON |
| `list_specs` | `kind` (string, optional) | Array of available specs |

## Development

```bash
git clone https://github.com/yourusername/speckit.git
cd speckit
pip install -e ".[dev]"

# Run non-slow tests (no API key needed — currently only structural tests)
make test

# Run full eval suite (requires ANTHROPIC_API_KEY, ~$0.50-1.00)
make test-all

# Run bias swap tests specifically (~$0.30)
make test-bias

# Quick smoke test
speckit list --kind hiring --pretty
```

### Project Structure

```
speckit/
├── speckit/                 # Python package
│   ├── __init__.py          # Public API + exceptions
│   ├── spec.py              # SpecFile dataclass, loader, parser
│   ├── validation.py        # Structural validation (no API calls)
│   ├── engine.py            # Executes plans against Claude
│   ├── registry.py          # Module registry
│   ├── claude_client.py     # Thin Anthropic SDK wrapper
│   ├── run_record.py        # RunRecord + JSONL persistence
│   ├── cli.py               # CLI (click)
│   ├── mcp_server.py        # MCP server
│   ├── modules/
│   │   ├── base.py          # Module ABC, InvocationPlan, ModuleResult
│   │   ├── interview_prep.py
│   │   └── spec_lint.py
│   └── web/
│       ├── app.py           # FastAPI
│       └── static/
│           └── index.html   # Single-file demo UI
├── specs/                   # Example spec files
│   ├── hiring/
│   │   ├── senior-frontend-platform.md
│   │   └── devops-lead.md
│   └── review/
├── prompts/                 # Versioned prompt templates
│   ├── interview_prep.md
│   └── spec_lint.md
├── evals/                   # Eval suite (real API calls)
│   ├── test_consistency.py
│   ├── test_bias_swap.py
│   ├── test_spec_lint.py
│   └── fixtures/
│       ├── sample_resume.md
│       └── biased_spec.md
├── SPEC_FORMAT.md           # Format RFC
├── ARCHITECTURE.md          # Detailed architecture docs
├── pyproject.toml
├── Makefile
└── .speckit/                # Git-ignored runtime state
    └── runs/                # JSONL run records
```

## License

MIT
