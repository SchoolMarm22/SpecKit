# Spec File Format — RFC

## 1. Overview

A **spec file** is a natural language document that configures how AI behaves in a people management workflow. Spec files are to people management what config files are to infrastructure — human-readable, version-controlled, and machine-applicable.

SpecKit treats spec files as the single source of truth. The AI is the executor. The human is the decision-maker. The spec is the contract between them.

## 2. File Format

- **Format:** Markdown with YAML frontmatter
- **Extension:** `.md`
- **Location:** `specs/{kind}/{name}.md`
- **Encoding:** UTF-8

A spec file consists of two parts:

1. **YAML frontmatter** — Machine-readable metadata, delimited by `---`
2. **Markdown body** — Natural language instructions that Claude reads and applies

```
---
kind: hiring
role: Senior Frontend Engineer
team: Platform
level: L5
version: 2
---

# What We're Looking For

[Natural language content...]

## Must-Haves

[Criteria...]
```

## 3. Frontmatter Schema

### Required Fields (all kinds)

| Field | Type | Description |
|-------|------|-------------|
| `kind` | string | Spec category. One of: `hiring`, `review`, `team`, `onboarding`, `offboarding` |
| `version` | int | Human-managed version number |

### Required Fields (kind: hiring)

| Field | Type | Description |
|-------|------|-------------|
| `role` | string | Job title |
| `team` | string | Team name |
| `level` | string | Level designation (e.g., L4, L5, Senior) |

### Optional Fields (all kinds)

| Field | Type | Description |
|-------|------|-------------|
| `author` | string | Who wrote this spec |
| `created` | string | ISO 8601 date |
| `updated` | string | ISO 8601 date |

**Unknown fields are preserved, not rejected.** Teams can add custom metadata without forking the format.

## 4. Body Format

The markdown body is split into **sections** by H2 headings (`##`).

### Section Normalization

Section names are normalized for programmatic access:

1. Strip leading `#` characters
2. Lowercase
3. Replace non-alphanumeric characters with underscores
4. Strip leading/trailing underscores

Examples:
- `## Must-Haves` → `must_haves`
- `## Anti-Patterns` → `anti_patterns`
- `## Interview Focus` → `interview_focus`

Content before the first H2 heading is stored under the key `preamble`.

### Section Enforcement

Sections are **not rigidly enforced** at the loader level. Modules declare which sections they expect and handle missing sections gracefully (with warnings, not errors). Managers should not need to memorize a section taxonomy.

## 5. Supported Kinds

| Kind | Description | Status |
|------|-------------|--------|
| `hiring` | Job descriptions, interview criteria, evaluation rubrics | Active |
| `review` | Performance review configuration | Format-ready |
| `team` | Team norms, operating principles | Format-ready |
| `onboarding` | New hire onboarding plans | Format-ready |
| `offboarding` | Exit process, knowledge capture | Format-ready |

Kinds are extensible. The validation layer warns on unknown kinds but does not reject them.

## 6. Versioning

The `version` field in frontmatter is **human-managed** — an integer that the spec author increments when making meaningful changes. This is for quick reference, not for cryptographic integrity.

For production use, pair the `version` field with Git SHA for full lineage:
- `version: 3` tells you "this is the third significant revision"
- `git log specs/hiring/senior-frontend-platform.md` tells you every change

SpecKit records the spec version in every output's meta block, creating an audit trail from output back to the spec that produced it.

## 7. Examples

### Hiring Spec (complete)

```markdown
---
kind: hiring
role: Senior Frontend Engineer
team: Platform
level: L5
version: 2
author: cindi.martinez
created: 2026-03-15
updated: 2026-03-28
---

# What We're Looking For

Prefer candidates with real startup experience. Full-stack at a 200-person
company is different from full-stack at a 5-person startup.

## Must-Haves

- Shipped production React at scale (>100k users)
- Owned a frontend architecture decision that went wrong and can talk
  about what they learned

## Strong Signals

- Open source contributions
- Has mentored junior engineers

## Anti-Patterns

- "Full-stack" experience that was really just touching a REST endpoint
- Can't explain tradeoffs in their own architectural decisions

## Interview Focus

- Real ownership vs. proximity to impressive work
- How they handle technical disagreements
```

### Review Spec (sketch)

```markdown
---
kind: review
team: Platform
version: 1
---

# Review Criteria

## Impact

Evaluate based on shipped outcomes, not activity volume.

## Growth

Where has this person stretched beyond their current level?

## Collaboration

How do peers describe working with this person?
```

### Team Spec (sketch)

```markdown
---
kind: team
team: Platform
version: 1
---

# How We Work

## Communication

Default to async. Use meetings for decisions, not status updates.

## Code Review

Every PR gets reviewed within 4 hours. Review the design, not just the code.

## On-Call

On-call rotates weekly. The on-call engineer owns incident response
and writes the postmortem.
```
