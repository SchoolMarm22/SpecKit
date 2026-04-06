---
kind: hiring
role: Senior Backend Engineer (Node.js)
team: Backend
level: L5
version: 1
---

# What We're Looking For

I need someone who's been through the Node.js maturity curve — who started when callbacks were king, lived through the Promise revolution, and now thinks in async/await. More importantly, someone who's felt the pain of poorly architected Node services at scale and knows what good looks like.

This isn't about knowing every npm package. It's about understanding when to reach for Express vs Fastify vs Koa, when to use clustering vs worker threads, and why you'd choose PostgreSQL over MongoDB for a specific use case. I want someone who's debugged memory leaks in production and can explain why `process.nextTick()` exists without Googling it.

## Must-Haves

- 4+ years building production Node.js services handling real traffic (>10k RPM)
- Deep understanding of the event loop and can explain why blocking operations kill Node performance
- Has designed and built RESTful APIs that other teams actually use and don't complain about
- Experience with at least one major Node.js framework (Express, Fastify, NestJS) and can articulate why they chose it
- Has debugged and fixed performance bottlenecks in production Node applications

## Strong Signals

- Built or significantly improved a service's error handling and observability
- Experience mentoring junior developers through Node.js gotchas
- Has opinions about TypeScript in Node.js projects backed by real experience
- Can discuss database connection pooling, query optimization, and transaction management
- Open source contributions or technical blog posts about Node.js patterns

## Anti-Patterns

- "Full-stack" experience where Node.js was just a thin API layer over database queries
- Can't explain the difference between `setImmediate()`, `setTimeout()`, and `process.nextTick()`
- Treats npm packages as black boxes and can't evaluate third-party dependencies for security or performance
- Only worked on CRUD APIs — never dealt with real-time features, background jobs, or complex business logic
- Dismisses testing as "QA's job" or only writes happy-path unit tests

## Interview Focus

- Event loop understanding: how would you handle a CPU-intensive task in Node.js?
- API design: walk through a complex endpoint they've built and the tradeoffs they made
- Debugging stories: memory leaks, performance issues, mysterious crashes they've investigated
- Code review philosophy: what do they look for when reviewing Node.js code?
- Architecture decisions: when would you split a monolith vs optimize it, and why?
