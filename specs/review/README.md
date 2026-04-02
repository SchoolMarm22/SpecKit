# Review Specs

The spec file format supports `kind: review` for performance review configuration.

## Status

**Format-ready, module not yet implemented.**

You can write review specs now using the standard format. They will parse, validate, and be listed by `speckit list`. When the review module ships, your specs will work without changes.

## Example

```markdown
---
kind: review
team: Platform
version: 1
author: your.name
---

# Review Criteria

## Impact

Evaluate based on shipped outcomes, not activity volume.
Distinguish between individual contribution and team-level impact.

## Growth

Where has this person stretched beyond their current level?
What skills are they developing, and what evidence supports progress?

## Collaboration

How do peers describe working with this person?
Do they elevate the people around them?
```

## Planned Module

The review module would:
- Accept a review spec + collected evidence (peer feedback, project outcomes, 1:1 notes)
- Produce a structured evidence summary aligned to the spec's criteria
- Surface gaps where more evidence is needed
- Flag potential recency bias or halo effects

## Why This Isn't Built Yet

Review specs affect compensation, promotion, and career trajectory. The stakes are higher than interview prep, and the bias surface area is larger. This module should be built with extensive eval coverage and careful prompt engineering. Format-ready means the spec format is stable. Module-ready is a separate bar.
