---
kind: hiring
role: Senior DevOps / Platform Engineer
team: Internal Platform
level: L5
version: 1
---

# What We're Looking For

We're the people who keep Datadog running while Datadog keeps everyone else running. That means our platform needs to ingest trillions of data points per day while maintaining sub-second query times — and we dogfood everything we build, so when our platform breaks, we feel it first.

I need someone who understands that observability isn't just a buzzword — it's how you design systems from day one. You should have strong opinions about metrics cardinality, the difference between logs and traces, and why RED vs USE matters for different system components. We're not just building infrastructure; we're building the infrastructure that powers the infrastructure that powers modern software.

This isn't a role where you'll be abstracting away complexity with endless YAML. You'll be writing Go, thinking about distributed systems, and making architectural decisions that affect how millions of engineers debug their production systems.

## Must-Haves

- Operated distributed systems at scale (billions of events/day minimum)
- Go experience in production — we're a Go shop and you'll be reading and writing it daily
- Built internal platforms that other engineers actually want to use (not just tolerate)
- Experience with time-series databases, message queues, or stream processing at scale
- Can articulate the observability pyramid and where different telemetry types belong

## Strong Signals

- Has built or operated an observability platform (metrics, logs, traces, or RUM)
- Experience with Kubernetes operators or controllers in Go
- Strong opinions about service mesh architectures backed by production experience
- Has debugged performance issues using actual observability tools, not just guessing
- Open source contributions to infrastructure or observability projects

## Anti-Patterns

- "Platform engineer" experience that was really just Terraform and Jenkins
- Can't explain why they chose specific monitoring tools beyond "it was already there"
- Talks about "shifting left" without understanding what that means for platform design
- Has never been on-call for systems they built
- Dismisses the importance of developer experience ("they should just read the docs")

## Interview Focus

- System design: How would you build a metrics ingestion pipeline that needs to handle 10x traffic spikes?
- Observability philosophy: What's your hierarchy for alerting vs monitoring vs debugging?
- Platform thinking: How do you balance flexibility vs simplicity when building tools for 2000+ engineers?
- Performance debugging: Walk through diagnosing a P99 latency regression using telemetry data
- Dogfooding experience: How do you use observability tools to improve the systems that generate observability data?
