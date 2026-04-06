---
kind: hiring
role: Senior DevOps / Platform Engineer
team: Blockchain Infrastructure
level: L5
version: 1
---

# What We're Looking For

We're not just another fintech company — we're building the cryptoeconomy, and that means our infrastructure requirements are fundamentally different. You need to understand that when our systems go down, it's not just user frustration; it's real money that can't move, trades that can't execute, and customer trust that evaporates.

I need someone who gets excited about the technical challenges of running infrastructure that bridges traditional finance and crypto. You'll be managing systems that need to sync with multiple blockchains, handle regulatory compliance across jurisdictions, and maintain 99.99% uptime because our customers' financial lives depend on it. If you think crypto is just "fake internet money," this isn't the role for you.

## Must-Haves

- Production experience with high-frequency financial systems or payment processing (money can't be "eventually consistent")
- Deep Kubernetes expertise with multi-region deployments and disaster recovery that you've actually tested
- Built monitoring and alerting for systems where false positives cost money and false negatives cost more
- Experience with blockchain node infrastructure (Bitcoin, Ethereum, or similar) — not just reading about it, actually running it
- Strong security mindset with experience in regulated environments (SOX, PCI, or similar compliance frameworks)

## Strong Signals

- Has run cryptocurrency mining or staking infrastructure
- Experience with Go services in production (our entire backend is Go)
- Built or improved CI/CD for systems with complex integration testing requirements
- Understands the difference between finality and confirmation in distributed systems
- Has opinions about when to use managed services vs. self-hosting in crypto contexts

## Anti-Patterns

- Crypto skeptic who sees this as "just another infrastructure job"
- Can't explain why blockchain systems need different reliability patterns than web apps
- Treats security as a checkbox rather than a mindset
- No experience with financial data or regulated systems
- "Move fast and break things" mentality (we move deliberately and test thoroughly)

## Interview Focus

- Incident response in financial systems: how do you handle a trading halt vs. a blog outage?
- Blockchain infrastructure challenges: sync lag, reorgs, gas management
- Security-first architecture decisions and their performance tradeoffs
- How they balance innovation velocity with regulatory compliance requirements
- Real examples of building monitoring for systems where every alert matters
