---
kind: hiring
role: Senior Site Reliability Engineer
team: Platform
level: L5
company: Datadog
version: 1
---

# What We're Looking For

We're not just another observability company — we *are* observability. Our customers trust us with their most critical systems, which means our reliability bar is higher than most. When Shopify's Black Friday traffic spikes, when Netflix pushes a new release, when banks process payments — they're watching those systems through Datadog. If we're down, they're blind.

You'll be joining a team that processes 50+ trillion data points per day. That's not a typo. Our Go services handle more metrics ingestion than most companies see web requests. We dogfood everything we build, which means you'll be using the same alerting, dashboards, and APM that our customers pay us for. When something breaks, you'll feel it first.

Looking for someone who's scaled systems through real hypergrowth, not just theoretical load. The difference between 1M and 100M data points per minute isn't just "add more servers" — it's rethinking your entire approach to data structures, memory management, and distributed consensus.

## Must-Haves

- Scaled stateful systems through 10x+ growth (not just web servers behind a load balancer)
- Production Go experience in high-throughput environments (>100k req/sec)
- Deep understanding of time-series databases — either built one, operated ClickHouse/InfluxDB at scale, or can explain why LSM-trees matter for our workload
- On-call experience where your decisions affected customer SLAs, not just internal tools
- Systems programming mindset: can debug memory leaks, understand GC pressure, profile CPU bottlenecks

## Strong Signals

- Has opinions about metrics cardinality that go beyond "high cardinality is bad"
- Experience with streaming data pipelines (Kafka, Pulsar, or similar) at scale
- Built or significantly improved observability tooling (even if not at an observability company)
- Can articulate the tradeoffs between consistency and availability in distributed systems
- Contributed to Go stdlib, Kubernetes, or other infrastructure OSS

## Anti-Patterns

- "SRE" experience that was really just managing cloud infrastructure
- Can't explain why eventual consistency matters for metrics aggregation
- Thinks reliability is just about uptime percentages, not data accuracy
- Never questioned whether their monitoring was actually useful vs. just comprehensive
- Assumes observability problems are solved by throwing more Prometheus at them

## Interview Focus

- War stories from scaling data-intensive systems — the decisions they made when things got ugly
- How they'd approach debugging a 10% data loss that only affects customers in EU-West
- Their philosophy on alerting: what deserves to wake someone up vs. what can wait until morning
- Technical deep-dive on a system they scaled — we'll probe hard on the "why" behind their architecture choices
- How they balance between shipping fast and maintaining reliability when every feature affects data ingestion
