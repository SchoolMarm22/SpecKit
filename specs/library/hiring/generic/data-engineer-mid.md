---
kind: hiring
role: Mid-Level Data Engineer
team: Data
level: L4
version: 1
---

# What We're Looking For

I need someone who's moved beyond writing one-off scripts and has built data systems that other people depend on. Mid-level means you've been burned by bad data quality decisions and learned from it. You understand that "it works on my laptop" isn't the same as "it works in production at 2am when the upstream API changes its schema."

Looking for someone who can own a domain end-to-end — not just implement tickets, but think through the edge cases and failure modes. You should have opinions about data modeling that go beyond "let's just dump everything into a data lake and figure it out later."

## Must-Haves

- Built and maintained production ETL/ELT pipelines that process real business data daily
- Experience with both SQL and Python/Scala for data transformation (not just one or the other)
- Has debugged data quality issues in production and implemented monitoring to catch them earlier
- Can design dimensional models or similar structured approaches (not everything belongs in a bronze/silver/gold architecture)
- Experience with at least one orchestration tool (Airflow, Prefect, Dagster) beyond just scheduling cron jobs

## Strong Signals

- Has worked with streaming data (Kafka, Kinesis) and understands when batch vs stream makes sense
- Experience with dbt or similar transformation frameworks
- Can explain their approach to data testing and validation
- Has dealt with PII/sensitive data and understands compliance implications
- Experience with infrastructure as code for data resources

## Anti-Patterns

- "Big data" experience that was really just running Spark jobs someone else wrote
- Can't explain the difference between a data warehouse and a data lake (or thinks they're the same thing)
- Has never worked with analysts or other data consumers — only built pipelines in isolation
- Treats data quality as someone else's problem
- Only comfortable with one cloud provider and can't articulate why they chose it

## Interview Focus

- Data modeling decisions: walk through a schema they designed and the tradeoffs they made
- Pipeline failure stories: what broke, how they debugged it, what monitoring they added
- Performance optimization: a time they made something faster and how they measured success
- Stakeholder communication: how they gather requirements from analysts or data scientists
