---
kind: hiring
role: Staff Backend Engineer (Rust)
team: Backend
level: L6
version: 1
---

# What We're Looking For

I need someone who doesn't just write Rust code, but thinks in systems. At staff level, you're not just implementing features — you're shaping how we build software. You should have opinions about service boundaries, data consistency models, and operational complexity that come from actually running distributed systems in production.

The Rust part matters because we're betting on performance and reliability at scale. But if you've never had to explain to a product manager why rewriting in Rust was worth the 6-month migration, or if you can't articulate the operational tradeoffs of zero-copy deserialization, you're probably not ready for this role. We need someone who's lived through the "why is this service using 40% more CPU after the Rust rewrite" conversations and came out with better systems on the other side.

## Must-Haves

- Designed and operated distributed systems with 99.9%+ uptime requirements
- Deep Rust experience including async runtime internals, memory management patterns, and performance profiling in production
- Led technical decisions that affected multiple teams (service boundaries, data models, API contracts)
- Shipped systems that handle >10M requests/day with clear performance characteristics
- On-call experience debugging production issues across service boundaries

## Strong Signals

- Has opinions about when NOT to use Rust and can defend them
- Experience with consensus protocols, event sourcing, or other distributed systems patterns
- Built or contributed to Rust libraries used by other teams
- Can explain the operational implications of their architectural choices
- Has mentored senior engineers through complex system design decisions

## Anti-Patterns

- "Rust expert" whose experience is mostly toy projects or rewrites without production load
- Can't explain the business impact of their technical decisions
- Focuses on code elegance over system reliability and operational simplicity
- Never had to debug a distributed systems issue across team boundaries
- Treats performance optimization as premature rather than understanding when it matters

## Interview Focus

- System design with specific focus on failure modes and operational complexity
- Rust-specific architectural decisions: async vs sync, when to use channels vs shared state, memory layout choices
- Stories about technical leadership across team boundaries — how they influenced without authority
- Trade-off reasoning: when they chose boring solutions over clever ones and why
- Incident response: complex distributed systems debugging under pressure
