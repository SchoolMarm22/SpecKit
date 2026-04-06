---
kind: hiring
role: Senior Backend Engineer (Go)
team: Metrics Pipeline
level: L5
version: 1
---

# What We're Looking For

We process 2+ trillion metrics per day. When our pipeline has a bad day, our customers' observability goes dark — which means their production systems become unobservable. This isn't just another CRUD API; every millisecond of latency compounds across billions of data points.

You'll be dogfooding your own work daily. When you break the metrics ingestion pipeline, you'll feel it immediately in your own Datadog dashboards. This feedback loop makes you a better engineer faster than any other environment I've seen.

We're not looking for someone who's read about high-throughput systems. We need someone who's debugged why their Kafka consumer is falling behind at 2am, who understands why Go's GC tuning matters when you're processing 50GB/hour per instance, and who has strong opinions about time series data structures because they've lived with the consequences of bad choices.

## Must-Haves

- Production Go experience with high-throughput data processing (>1M events/sec)
- Deep understanding of Kafka or similar streaming platforms — not just producing/consuming, but partition strategies, offset management, and backpressure handling
- Time series database experience (InfluxDB, TimescaleDB, or built custom solutions)
- Has been on-call for a system that processes business-critical data where downtime costs real money
- Can explain memory allocation patterns in Go and why they matter at scale

## Strong Signals

- Has optimized Go services for specific latency or throughput targets
- Experience with observability tools as a user (shows they understand what good metrics feel like)
- Built or maintained data pipelines where ordering guarantees mattered
- Has worked in competitive markets where performance differentiation matters
- Open source contributions to data infrastructure projects

## Anti-Patterns

- "High scale" experience that was really just auto-scaling web servers
- Can't articulate the tradeoffs between consistency and availability in their own systems
- Thinks metrics are just "logs with numbers" — shows they don't understand cardinality explosion or aggregation strategies
- Never been responsible for data quality or pipeline reliability
- Dismissive of operational concerns like monitoring or alerting ("that's SRE's job")

## Interview Focus

- System design: How would you build a metrics ingestion pipeline from scratch? What are the bottlenecks?
- Go performance: Walk through optimizing a hot path in a Go service. When do you reach for profiling?
- Data pipeline reliability: Tell me about a time data was wrong or missing. How did you detect it? How did you fix it?
- Competitive awareness: What makes a good metrics product? How do you evaluate observability tools?
- Dogfooding mindset: How do you instrument your own services? What metrics do you care about?
