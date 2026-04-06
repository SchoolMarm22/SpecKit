---
kind: hiring
role: Senior Backend Engineer (Go)
team: Trading Platform
level: L5
version: 1
---

# What We're Looking For

We're building financial infrastructure that moves billions of dollars. One bug in our matching engine doesn't just mean downtime — it means regulatory scrutiny, customer funds at risk, and potentially congressional hearings. I need someone who understands that "move fast and break things" doesn't apply when you're a regulated financial institution.

You should believe crypto is the future of finance, not just another place to apply your CRUD skills. We're not a fintech company that happens to do crypto — we're crypto-native, and that changes everything about how we think about system design, data consistency, and user trust.

Our Go services handle order matching, settlement, custody operations, and regulatory reporting. We interact with 15+ blockchains, each with their own quirks and failure modes. You'll be writing code that needs to work correctly in Byzantine failure scenarios, not just when AWS has a good day.

## Must-Haves

- 5+ years of Go in production, with strong opinions about error handling, context propagation, and goroutine lifecycle management
- Experience with financial systems, trading platforms, or payments infrastructure where correctness isn't negotiable
- Has debugged race conditions in high-throughput systems (>10k RPS) and can explain their methodology
- Understanding of blockchain fundamentals — not just "I used web3.js once" but can explain finality, reorgs, and why nonce management matters
- Testing mindset that goes beyond unit tests: property-based testing, chaos engineering, or formal verification experience

## Strong Signals

- Has worked at a crypto company or built crypto-adjacent systems (DeFi protocols, exchanges, wallet infrastructure)
- Experience with regulatory compliance in financial services (SOX, audits, immutable logs)
- Can discuss the tradeoffs between different consensus mechanisms and why they matter for system design
- Has opinions about database consistency models and when to use them (we use both Postgres and CockroachDB for different use cases)

## Anti-Patterns

- Crypto skeptic or thinks this is "just another database problem" (it's not)
- Has never been on-call for a system that handles real money
- Can't explain why idempotency matters or how they've implemented it
- Thinks microservices solve all problems or monoliths solve all problems (we use both deliberately)
- Never worked somewhere with serious compliance requirements

## Interview Focus

- System design for Byzantine environments: how do you handle blockchain reorgs in a trading system?
- Go-specific architecture decisions: channel usage, error propagation strategies, graceful shutdown patterns
- War stories about financial correctness: times when their code had to handle money and what safeguards they built
- Regulatory thinking: how would you design audit trails for a system that needs SOX compliance?
- Crypto-specific scenarios: designing hot wallet management, handling mempool congestion, cross-chain settlement
