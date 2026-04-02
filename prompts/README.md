# Prompt Templates

This directory contains versioned prompt templates used by SpecKit modules. Each template is a markdown file with YAML frontmatter.

## Format

```markdown
---
prompt_version: "0.1.0"
module: module_name
---

System prompt content here...
```

The **frontmatter** provides metadata:
- `prompt_version` — Semantic version. Increment when changing the prompt. This version is recorded in every output's meta block for audit traceability.
- `module` — Which module uses this template (informational, not enforced).

The **body** becomes the system prompt passed to Claude. It should be readable by anyone — no prompt engineering obscurantism.

## Templates

| File | Module | Purpose |
|------|--------|---------|
| `interview_prep.md` | `interview_prep` | System prompt for generating interview preparation packages |
| `spec_lint.md` | `spec_lint` | System prompt for analyzing spec quality and bias |

## How Templates Are Loaded

Modules call `self._load_prompt_template()` which:
1. Looks for `prompts/{module_name}.md` relative to the project root
2. Strips the YAML frontmatter
3. Returns the body as a string

The template body is used as the `system` parameter in the Claude API call. The user message (containing the actual spec + inputs) is composed separately by the module.

## Editing Prompts

When modifying a prompt template:
1. **Bump `prompt_version`** in the frontmatter
2. **Run the eval suite** (`make test-all`) to verify output quality hasn't regressed
3. **Check consistency** — the consistency eval will catch if your changes make output less stable
4. **Check bias** — the bias swap eval will catch if your changes introduce demographic sensitivity

Prompt changes are the highest-leverage changes in the system. A small wording change in the system prompt affects every output. Treat prompt edits like schema migrations — test thoroughly.
