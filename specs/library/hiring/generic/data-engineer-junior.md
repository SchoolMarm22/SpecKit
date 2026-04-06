---
kind: hiring
role: Junior Data Engineer
team: Data
level: L3
version: 1
---

# What We're Looking For

I'm looking for someone who gets excited about data quality problems and doesn't just see them as tedious work. The best junior data engineers I've hired are the ones who started noticing inconsistencies in their own side projects or internship work and couldn't help but dig into why.

You don't need years of experience, but you need to demonstrate that you can think through data problems methodically. I'd rather hire a recent grad who built a personal project that properly handles missing data than someone with a fancy internship who can't explain why their SQL query returns different row counts on different days.

## Must-Haves

- Can write clean SQL with joins, window functions, and CTEs (not just basic SELECT statements)
- Has built at least one end-to-end data pipeline, even if small (personal project, internship, bootcamp)
- Understands data types and can explain when you'd use VARCHAR vs TEXT or why floating point math is tricky
- Can explain the difference between batch and streaming processing (even if they've only done batch)
- Basic Python or similar for data manipulation (pandas, basic file I/O)

## Strong Signals

- Has worked with messy, real-world data (not just clean academic datasets)
- Asks good questions about data lineage and upstream dependencies
- Shows curiosity about data quality issues rather than just fixing them
- Has opinions about code organization and can explain why they structure scripts a certain way

## Anti-Patterns

- Only experience is with perfectly clean datasets from coursework
- Can't explain what happens when their pipeline fails halfway through
- Treats SQL as a reporting tool rather than a programming language
- No experience with version control or collaborative development
- Assumes all data problems can be solved by throwing more compute at them

## Interview Focus

- Walk through their pipeline project: what could go wrong, how would they debug it
- SQL problem-solving with realistic messy data scenarios
- How they approach learning new tools (we use dbt, Airflow, Snowflake - they don't need to know them but should show they can learn)
- Data quality scenarios: "You notice row counts dropped 20% yesterday, what do you do?"
