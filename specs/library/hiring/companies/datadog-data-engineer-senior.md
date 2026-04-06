---
kind: hiring
role: Senior Data Engineer
team: Log Analytics
level: L5
version: 1
---

# What We're Looking For

This isn't just another data engineering role. We're processing 5+ trillion log events daily for customers who depend on us to find the needle in the haystack during their 3am outages. When Shopify's checkout breaks on Black Friday, they're searching through millions of logs per second in our interface to figure out why.

The Log Analytics team owns the ingestion, storage, and query infrastructure that makes this possible. You'll be writing Go services that need to handle 10M+ events per second while maintaining sub-100ms p99 query latency. This is systems engineering disguised as data engineering — you need to understand distributed systems, not just Spark jobs.

We dogfood everything. You'll be using your own log search to debug your own services, which means you feel the pain when performance degrades or the UX is clunky. This feedback loop makes us better engineers.

## Must-Haves

- Built high-throughput data ingestion systems (1M+ events/sec sustained)
- Designed and implemented data storage solutions with specific latency/throughput requirements (not just "we used Kafka")
- Production experience with time-series or columnar storage engines (ClickHouse, TimescaleDB, or built custom)
- Can write performant Go or explain why your current language choice would be better for our use case
- Has been on-call for data systems where downtime means customer incidents go unresolved

## Strong Signals

- Experience with log aggregation at scale (ELK, Fluentd, or competitive products)
- Built custom indexing or search infrastructure (not just used Elasticsearch)
- Contributed to open source data infrastructure projects
- Previous work at observability/monitoring companies or adjacent spaces
- Can articulate the tradeoffs between different compression algorithms for log storage

## Anti-Patterns

- "Big data" experience that was really just writing Spark jobs on someone else's platform
- Can't explain why they chose specific storage formats or partitioning strategies
- Treats data engineering as ETL orchestration rather than systems building
- No opinion on observability tooling or has never been in a customer-facing data role
- Assumes "eventual consistency" is acceptable for user-facing query results

## Interview Focus

- System design: how would you build log ingestion for 10M events/sec with <1min search latency?
- Performance debugging: walk through optimizing a slow query on billions of log records
- Trade-off discussions: storage cost vs query speed, ingestion throughput vs data durability
- Customer empathy: describe a time when data quality issues affected end users
- Technical depth on storage engines: when would you choose row vs columnar, compression strategies
