---
kind: hiring
role: Senior Backend Engineer
team: Core
level: L5
version: 1
---

# What We're Looking For

We're not building another CRUD app. Linear feels fast because every backend decision optimizes for the 60fps animations our users expect. When someone creates an issue, assigns it, and watches the UI update in real-time across multiple clients, that's a distributed systems problem disguised as project management software.

You'll own systems that power real-time collaboration for teams who ship software daily. Our GraphQL API handles complex subscription patterns, our sync engine keeps offline clients coherent, and our database queries need to stay under 10ms even as workspaces scale to thousands of issues. We're TypeScript everywhere — backend, frontend, even our database layer — because we believe consistency reduces cognitive overhead.

We hire for judgment over resume. The best engineers we've hired could explain why they chose Postgres over MongoDB for a specific feature, not just recite database theory.

## Must-Haves

- Built and operated GraphQL APIs in production (subscriptions, not just queries)
- Real-time systems experience — WebSocket management, operational transforms, or conflict resolution
- TypeScript at scale with strong opinions about type safety vs. developer velocity tradeoffs
- Database performance tuning experience — can explain when to denormalize and why
- Has been responsible for API design decisions that downstream clients depended on

## Strong Signals

- Experience with offline-first or local-first architectures
- Has migrated a production system without downtime (shows systems thinking)
- Contributed to developer tooling or has strong opinions about DX
- Can articulate why they chose specific database indices or query patterns
- Background in tools, dev productivity, or products that developers use daily

## Anti-Patterns

- "Full-stack" but can't explain database query performance under load
- Microservices experience where they only owned one small service
- GraphQL experience limited to toy projects or simple REST wrappers
- Treats real-time features as "nice to have" rather than core architecture
- Can't explain how their code would behave under 10x current load

## Interview Focus

- API design philosophy: how they think about client needs vs. server constraints
- Real-time architecture: their mental model for keeping distributed state consistent
- Performance instincts: when they optimize and what they measure
- TypeScript depth: how they balance type safety with shipping speed
- System ownership: examples of being responsible for both the happy path and the edge cases
