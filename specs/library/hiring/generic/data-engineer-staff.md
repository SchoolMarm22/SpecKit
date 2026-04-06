---
kind: hiring
role: Staff Data Engineer
team: Data
level: L6
version: 1
---

# What We're Looking For

I need someone who thinks beyond individual pipelines and sees the data platform as a product. This role is about architectural decisions that affect the entire organization — not just building ETL jobs, but designing the systems that make other engineers more effective.

The right person has lived through data platform scaling pain points: the Airflow cluster that melted down during peak traffic, the lake house migration that took 18 months, the data quality crisis that broke trust with product teams. They've been the technical leader who had to make the hard calls when things went sideways.

This isn't a hands-off role. You'll still write code, but your code needs to enable 20+ other engineers. Your architectural decisions will outlive your tenure here. I need someone who can hold their own in staff eng discussions about company-wide technical strategy.

## Must-Haves

- Designed and operated data platforms serving 10+ engineering teams
- Led a major data infrastructure migration (on-prem to cloud, batch to streaming, monolith to mesh)
- Built data systems that handle 100M+ events per day with SLA requirements
- Has strong opinions about data modeling that go beyond "star schema good, snowflake bad"
- Experience with data governance at scale — not just documentation, but enforcement

## Strong Signals

- Has architected real-time data systems (not just batch ETL)
- Deep experience with both transactional and analytical workloads
- Can articulate the business impact of their technical decisions
- Has mentored senior engineers and influenced hiring standards
- Understands data contracts and schema evolution strategies

## Anti-Patterns

- "Big data" experience that never dealt with actual scale or SLA pressure
- Can't explain the CAP theorem implications for their system design
- Treats data quality as a post-processing problem rather than a system design problem
- Has only worked with one cloud provider or orchestration tool
- Makes technology choices based on resume building rather than business needs

## Interview Focus

- System design: multi-tenant data platform with strict isolation requirements
- War stories: major outages or migrations they've led, focusing on decision-making under pressure
- Technical strategy: how they'd evaluate build vs buy for core platform components
- Org influence: examples of changing engineering practices beyond their immediate team
- Code review of their most complex data pipeline — architecture decisions, not syntax
