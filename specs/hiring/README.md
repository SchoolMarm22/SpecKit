# Hiring Specs

This directory contains spec files for `kind: hiring`. Each file configures how Hiring Manager Tools evaluates candidates for a specific role.

## Included Specs

| File | Role | Team | Level |
|------|------|------|-------|
| `senior-frontend-platform.md` | Senior Frontend Engineer | Platform | L5 |
| `devops-lead.md` | DevOps Lead | Infrastructure | L5 |

## Writing a Hiring Spec

A hiring spec captures the **manager's actual priorities** — not a generic job description.

### Required Frontmatter

```yaml
---
kind: hiring
role: Job Title
team: Team Name
level: L5
version: 1
---
```

### Recommended Sections

| Section | Purpose |
|---------|---------|
| `## Must-Haves` | Non-negotiable criteria. Be specific: "shipped production React at scale" not "React experience" |
| `## Strong Signals` | Differentiators. What would make you excited about a candidate? |
| `## Anti-Patterns` | What you explicitly don't want. Knowing what to avoid is as useful as knowing what to seek |
| `## Interview Focus` | What the interviewer should probe. Direct guidance for the conversation |

### Tips

- **Be opinionated.** "I'd rather hire someone with 2 years at a startup than 5 years at Google" is a valid and useful spec statement. Generic specs produce generic outputs.
- **Name the tradeoffs.** If startup experience matters more than FAANG pedigree, say so. The module weighs what you weigh.
- **Include anti-patterns.** They're often more revealing than must-haves. "Can't explain tradeoffs in their own decisions" is a precise anti-pattern.
- **Write in your own voice.** Specs are natural language. Write like you'd explain the role to a colleague, not like you're filling out an HR form.

## Validation

Run `speckit lint --spec hiring/your-spec-name` to check a spec for:
- Structural completeness (required frontmatter fields)
- Bias risk ("culture fit", "native speaker", prestige requirements)
- Vagueness ("team player", "self-starter")
- Missing sections (anti-patterns, interview focus)
- Legal risk (protected characteristics, disparate impact)
