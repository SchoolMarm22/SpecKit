---
kind: hiring
role: Senior Backend Engineer (Rust)
team: Backend
level: L5
version: 1
---

# What We're Looking For

We need someone who chose Rust for the right reasons, not just because it's trendy. You should have battle scars from production Rust — the kind you only get from debugging lifetime issues at 2am or explaining to your team why that "simple" refactor took three weeks because the borrow checker had opinions.

This isn't a role where you'll be writing Rust in isolation. You'll be the person other engineers come to when they're stuck on async/await hell or when they need to understand why their service is using 2GB of memory when it should be using 200MB. You should be comfortable being the Rust expert in the room while also knowing when not to use Rust at all.

## Must-Haves

- 3+ years of production Rust experience (not just side projects)
- Built and operated high-throughput services (>10k RPS) in Rust
- Deep understanding of async Rust ecosystem (tokio, async-std, or equivalent)
- Can explain ownership, borrowing, and lifetimes to someone learning Rust
- Production experience with at least one major Rust web framework (axum, warp, actix-web)

## Strong Signals

- Has contributed to Rust open source projects or crates
- Experience migrating services from other languages to Rust
- Can articulate when NOT to use Rust (Python for ML pipelines, Go for simple CRUD, etc.)
- Has mentored engineers through their first Rust projects
- Understanding of Rust's performance characteristics and profiling tools

## Anti-Patterns

- Only talks about Rust's safety features, ignoring performance or productivity tradeoffs
- Can't explain why they chose specific crates over alternatives
- Has never dealt with complex lifetime issues in real codebases
- Thinks every service should be rewritten in Rust
- Can't work with async code without copying examples from Stack Overflow

## Interview Focus

- Architecture decisions: when they chose Rust vs. other languages and why
- Debugging stories: how they've diagnosed performance or memory issues
- Teaching ability: can they explain complex Rust concepts simply
- Production readiness: error handling, logging, metrics, graceful shutdown
- Team dynamics: how they've introduced Rust to teams or codebases
