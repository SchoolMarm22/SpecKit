---
kind: hiring
role: Senior Data Engineer
team: Data
level: L5
version: 1
---

# What We're Looking For

I need someone who's lived through the full lifecycle of a data platform — from the early days when everything was held together with cron jobs and prayers, to building something that actually scales. You should have opinions about data modeling that come from getting burned by bad decisions, not just reading blog posts.

We're not looking for someone who just writes Spark jobs. I need someone who can look at our current architecture, identify the bottlenecks we don't even know we have yet, and build systems that won't break when we 10x our data volume. You should be the person other engineers come to when they need to understand why their query is slow or why their pipeline failed at 2am.

## Must-Haves

- Built and maintained production data pipelines processing >1TB daily
- Designed data models that evolved successfully over 2+ years without major rewrites
- Owned end-to-end data quality and can articulate your monitoring philosophy beyond "we check row counts"
- Production experience with modern data stack (Spark/Airflow/dbt or equivalent) at scale
- Has been on-call for data systems and debugged pipeline failures under pressure

## Strong Signals

- Can explain the tradeoffs between batch and streaming architectures from experience, not theory
- Has migrated a data system from one technology to another (cloud migration, warehouse migration, etc.)
- Experience mentoring junior data engineers through their first production pipeline
- Built or significantly improved data discovery/lineage tooling
- Has strong opinions about testing data pipelines that go beyond "we validate schema"

## Anti-Patterns

- "Big data" experience that was really just SQL on someone else's well-architected system
- Can't explain why they chose specific technologies beyond "it's what the team was using"
- Treats data quality as a post-processing step rather than a design constraint
- Only worked with clean, well-structured data sources (we have messy third-party APIs and legacy databases)
- Dismissive of business context — thinks stakeholders "just don't understand the technical constraints"

## Interview Focus

- Pipeline failure war stories: what broke, how they debugged it, how they prevented it from happening again
- Data modeling decisions: show me a schema you designed and walk through the tradeoffs
- Scaling challenges: when did their current system start to break and how did they address it
- Cross-team collaboration: how they've worked with product managers and analysts who don't understand backfill complexity
