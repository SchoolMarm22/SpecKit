---
kind: hiring
role: Senior Data Engineer
team: Marketplace
level: L5
version: 1
---

# What We're Looking For

At Airbnb, data engineering isn't just about moving bytes around — it's about enabling millions of people to belong anywhere. Every pipeline you build directly impacts whether a host in Tokyo can trust a guest from São Paulo, or whether that guest finds the perfect home for their family reunion.

We've rebuilt our data stack post-2020 to be leaner but more impactful. No more "big data for big data's sake" — every system needs to serve our hosts and guests. You'll be building the data foundation that powers search ranking, trust & safety decisions, and pricing recommendations that directly affect people's livelihoods and travel experiences.

The marketplace team specifically owns the data that makes magic happen: matching the right guests with the right hosts, surfacing listings that create belonging, and ensuring our pricing algorithms help hosts earn while keeping travel accessible. This isn't abstract optimization work — this is craft that touches human lives.

## Must-Haves

- Built production data pipelines handling PII at scale (10M+ records daily) with proper privacy controls
- Owned end-to-end data quality for business-critical metrics (can explain how bad data propagates and breaks downstream systems)
- Designed schema evolution strategies for high-throughput systems without breaking downstream consumers
- Experience with both batch and streaming architectures — can articulate when each is appropriate and why
- Built data products that non-technical stakeholders actually use (not just other engineers)

## Strong Signals

- Has worked in marketplace/two-sided network businesses (understands host vs guest data patterns)
- Experience with experimentation data pipelines (A/B testing, feature flags, causal inference)
- Built real-time ML feature pipelines that serve production models
- Has debugged data quality issues that affected user-facing product metrics
- Can explain privacy engineering concepts beyond just "we encrypt at rest"

## Anti-Patterns

- Views data engineering as purely technical infrastructure divorced from user impact
- Can't explain how their pipeline choices affect data freshness vs system reliability tradeoffs
- Has never had to explain a data discrepancy to a PM or exec in business terms
- Treats data quality as someone else's problem (QA team, downstream consumers)
- Only experience is internal tools — never built data products that external users depend on

## Interview Focus

- Walk through a data quality incident: how they detected it, communicated impact, and prevented recurrence
- Design session: how would you build real-time pricing data for a marketplace with seasonal patterns and regional differences
- Schema design philosophy: evolving data contracts without breaking 20+ downstream services
- Privacy and compliance: handling global user data across different regulatory environments
- Craft discussion: a data pipeline they're proud of and what makes it well-designed vs just functional
