---
kind: hiring
role: Senior Backend Engineer (Go)
team: Backend
level: L5
version: 1
---

# What We're Looking For

I need someone who's been burned by goroutine leaks and lived to tell the tale. Go looks simple until you're debugging a memory leak that only happens under load, or dealing with context cancellation in a distributed system. We're looking for someone who's made those mistakes and learned from them.

This isn't just about writing Go code — it's about designing systems that other engineers can understand and extend. You'll be the person junior developers come to when they're stuck on distributed systems concepts, and you'll be expected to have opinions about service boundaries and data consistency that come from real experience, not just theory.

We're scaling from handling 10k requests/day to 1M+, so you'll need to think about performance, observability, and operational concerns from day one. If you've only worked at companies where infrastructure was someone else's problem, this might not be the right fit.

## Must-Haves

- 4+ years of production Go experience, including concurrent programming patterns and memory management
- Designed and implemented REST or gRPC APIs that handle >10k requests/minute in production
- Experience with distributed systems patterns: circuit breakers, retries, timeouts, eventual consistency
- Owned end-to-end delivery of a significant backend feature or service
- Database design experience with both SQL and NoSQL, including schema migrations and query optimization

## Strong Signals

- Has debugged production issues involving goroutine leaks, race conditions, or GC pressure
- Experience with microservices architecture and service-to-service communication patterns
- Built or significantly improved observability: structured logging, metrics, distributed tracing
- Mentored junior engineers or led technical discussions that influenced team decisions
- Open source Go contributions or technical writing about Go/distributed systems

## Anti-Patterns

- Go experience limited to tutorials or side projects (we need production battle scars)
- Can't articulate the tradeoffs of their architectural decisions beyond "it works"
- Treats testing as an afterthought rather than a design tool
- Has never been on-call or responsible for production system reliability
- Dismisses operational concerns as "not my job" or "DevOps will handle it"

## Interview Focus

- Concurrency patterns in Go: when to use channels vs mutexes, goroutine lifecycle management
- System design with specific focus on failure modes and recovery strategies
- Performance debugging stories: how they identified and fixed bottlenecks
- Code review philosophy and examples of feedback they've given
- How they approach technical debt and refactoring in a fast-moving environment
