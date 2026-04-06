---
kind: hiring
role: Senior Data Engineer
team: Content Analytics
level: L5
version: 1
---

# What We're Looking For

We measure everything at Netflix — what people watch, when they stop watching, what they rewind, what makes them cancel. Our Content Analytics team builds the data infrastructure that powers decisions about which shows to renew, which regions to expand into, and how to optimize the opening 10 seconds of every piece of content.

You'll own end-to-end data products that directly influence $15B+ in content spend. When Reed asks "why did Squid Game work in Korea but not in Germany?", your pipeline better have an answer. We don't hire data engineers to move data around — we hire them to build systems that reveal insights no one else in the industry has.

The freedom is real here. No sprint planning, no story points, no daily standups unless you want them. But the responsibility is equally real. When your ETL job fails at 2am and the content executives can't see their dashboard in the morning, that's on you. We expect you to own the problem and the solution.

## Must-Haves

- Built and operated petabyte-scale data pipelines in production (AWS/GCP, not on-prem)
- Deep Spark experience — can debug performance issues, optimize shuffle operations, understand partitioning strategies beyond "partition by date"  
- Streaming data experience with Kafka or Kinesis at high throughput (millions of events per minute)
- Strong Python or Scala for data processing — not just SQL and configuration files
- Have been on-call for data systems and lived through the 3am pages when join keys don't match

## Strong Signals

- Experience with experimentation platforms or A/B testing infrastructure
- Built data systems for product teams who actually used them (not just dashboards that sit unused)
- Media/entertainment domain knowledge — understands concepts like audience measurement, content attribution, engagement metrics
- Has strong opinions about data quality and monitoring that go beyond "we run some tests"
- Can articulate the CAP theorem implications for their actual system design choices

## Anti-Patterns

- "Big data" experience that was really just running someone else's Airflow DAGs
- Only worked with clean, pre-processed datasets — never dealt with raw user behavior data
- Treats data engineering as a cost center rather than a product that enables insights
- Can't explain why they chose batch vs streaming for their last project
- Defensive about their technical choices when questioned (candor is non-negotiable here)

## Interview Focus

- System design: "Design the data pipeline for measuring content engagement across 200M+ subscribers" — looking for partition strategies, late-arriving data handling, exactly-once processing
- Production war stories: specific incidents they owned, what broke, how they debugged it, what monitoring they added afterward
- Data quality philosophy: how do you ensure correctness when your pipeline processes 500TB/day and feeds models that influence billion-dollar content decisions
- Technical judgment: given our scale and growth trajectory, when would you choose Lambda architecture vs Kappa? Why?
- Ownership mindset: how do they balance moving fast with building reliable systems that other teams depend on
