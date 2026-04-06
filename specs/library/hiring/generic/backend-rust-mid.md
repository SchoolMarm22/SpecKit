---
kind: hiring
role: Mid-Level Backend Engineer (Rust)
team: Backend
level: L4
version: 1
---

# What We're Looking For

I want someone who has moved beyond the "syntax learning" phase of Rust and is starting to think in terms of ownership, lifetimes, and zero-cost abstractions. You don't need to be a Rust wizard, but you should be past the point where the borrow checker is your main enemy.

Looking for engineers who can own a service end-to-end — not just implement features, but think about error handling, observability, and how their code will behave under load. You should be comfortable being the primary owner of 1-2 services, including being on-call for them.

We're not looking for someone who needs their hand held, but we're also not expecting you to architect our entire system. You should be able to take a well-defined problem, break it down, and execute independently while knowing when to ask for help.

## Must-Haves

- 2+ years writing production Rust (not just side projects or tutorials)
- Has owned a service that serves real traffic and been responsible for its reliability
- Comfortable with async Rust — knows when to use tokio vs threads and can debug deadlocks
- Can write proper error handling with Result types and custom error enums
- Experience with at least one production database integration (PostgreSQL, MongoDB, etc.)

## Strong Signals

- Has contributed to or maintains a Rust crate (shows you write code for other humans)
- Can explain why they chose Rust for a specific project vs other languages
- Experience with Rust testing patterns beyond basic unit tests
- Has debugged production performance issues in Rust applications

## Anti-Patterns

- "Rust experience" that's really just following tutorials or porting existing code
- Can't explain when not to use Rust (everything looks like a nail)
- Writes Rust like it's Java or Python — fighting the language instead of working with it
- Has never been on-call for code they've written
- Can't articulate the tradeoffs in their architectural decisions

## Interview Focus

- Ownership patterns and lifetime management — can they think in terms of borrowing vs cloning?
- Error handling philosophy — how do they structure error types and propagation?
- Performance reasoning — can they explain when allocation matters and when it doesn't?
- Production debugging stories — how do they approach investigating issues in running systems?
