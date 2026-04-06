---
kind: hiring
role: Senior Backend Engineer (Java)
team: Backend
level: L5
version: 1
---

# What We're Looking For

I need someone who's lived through the Java ecosystem's evolution — from Spring XML hell to Boot's opinionated defaults, from monoliths to microservices and back to modular monoliths. You should have opinions about when to use CompletableFuture vs reactive streams, and why.

This isn't a "Java developer" role, it's a backend systems role where Java happens to be the primary tool. I want someone who thinks about data flow, service boundaries, and operational concerns first, then picks the right Java patterns to solve those problems. You'll be making architectural decisions that affect 3-4 other teams, so your code needs to be more than just working — it needs to be maintainable by people who aren't you.

## Must-Haves

- 5+ years of production Java experience with Spring ecosystem (Boot, Data, Security)
- Designed and owned a service that other teams depend on (internal API, shared library, or data pipeline)
- Shipped code that handles significant load (>10k RPM or >100GB data processing)
- Experience debugging production issues in distributed systems (tracing, profiling, heap dumps)
- Can architect database schemas and has opinions about transaction boundaries

## Strong Signals

- Has migrated a legacy system to modern architecture (monolith breakup, Java version upgrade, framework migration)
- Experience with message queues or event streaming (Kafka, RabbitMQ, SQS)
- Contributed to or maintained open source Java libraries
- Has mentored junior engineers through complex technical decisions
- Can explain JVM tuning decisions they've made in production

## Anti-Patterns

- Only worked on CRUD APIs without complex business logic
- Can't explain the difference between checked and unchecked exceptions (or worse, thinks checked exceptions are always bad)
- Reflexively suggests microservices for every problem
- Has never worked with legacy code or brownfield projects
- Treats testing as someone else's job or an afterthought

## Interview Focus

- Service design: how they think about API boundaries and backward compatibility
- Performance debugging: walk through finding and fixing a real bottleneck
- Mentoring scenarios: how they'd guide a junior through a complex technical decision
- Architecture tradeoffs: when they'd choose different patterns (reactive vs imperative, SQL vs NoSQL, sync vs async)
