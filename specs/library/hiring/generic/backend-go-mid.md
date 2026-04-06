---
kind: hiring
role: Mid-Level Backend Engineer (Go)
team: Backend
level: L4
version: 1
---

# What We're Looking For

I need someone who can take a feature spec and run with it end-to-end — from database schema to API design to deployment. Not someone who needs their hand held, but also not someone who thinks they know everything and ignores code review feedback.

The sweet spot is 2-4 years of real Go experience. I've seen too many candidates who "learned Go in a weekend" coming from Java or Python and think goroutines solve everything. I want someone who understands Go's idioms, has hit the common gotchas, and knows when to reach for channels vs. mutexes vs. just keeping it simple.

We're microservices-heavy with a decent amount of legacy code to maintain. You'll need to be comfortable both building new services from scratch and debugging someone else's 3-year-old code that has no tests and unclear requirements.

## Must-Haves

- 2+ years production Go experience with HTTP services and database integration
- Designed and implemented REST APIs that other teams actually consume
- Worked with SQL databases (PostgreSQL preferred) including schema migrations
- Experience with containerization (Docker) and at least one orchestration platform
- Can write comprehensive tests and has opinions about what makes tests maintainable

## Strong Signals

- Has debugged performance issues in production (not just development)
- Experience with gRPC or other RPC frameworks beyond REST
- Comfortable with distributed systems concepts (eventual consistency, retries, circuit breakers)
- Has worked in a microservices environment and can articulate the tradeoffs
- Open source Go contributions or side projects

## Anti-Patterns

- "Go experience" that's really just following tutorials or bootcamp projects
- Can't explain when to use pointers vs. values in Go
- Thinks goroutines are the answer to every concurrency problem
- Has never written a test that actually caught a real bug
- Dismisses error handling as "boilerplate" rather than understanding Go's philosophy

## Interview Focus

- API design decisions: how they structure endpoints, handle errors, version APIs
- Debugging methodology: walking through how they'd investigate a production issue
- Code organization: how they structure Go projects and why
- Error handling patterns and their experience with Go's explicit error model
- Concurrency: when they'd use goroutines vs. simpler approaches
