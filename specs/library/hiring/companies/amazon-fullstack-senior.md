---
kind: hiring
role: Senior Full-Stack Engineer
team: Retail
level: L5
version: 1
---

# What We're Looking For

We're not building features — we're building primitives that millions of customers depend on. Every line of code you write will be scrutinized by our traffic patterns, and every architectural decision will be stress-tested by Prime Day.

I need someone who's built production systems that actually scale, not just systems that could theoretically scale. Someone who's been paged at 2am because their service was taking down checkout, and came back the next day with a plan to make sure it never happens again. We have hundreds of services talking to each other — you need to understand what happens when any one of them gets slow, not just when they fail completely.

Our two-pizza team owns everything from the React components customers see to the DynamoDB tables that store their cart state. If you've only worked in organizations where "full-stack" means you call someone else's APIs, this isn't the role for you.

## Must-Haves

- Built and owned production services handling >1M requests/day
- Experience with event-driven architectures and eventual consistency (not just CRUD over REST)
- Has been on-call for services they built and can articulate specific improvements they made based on production incidents
- Comfortable with both SQL and NoSQL at scale — knows when to choose DynamoDB vs RDS and why
- Can write a convincing PRFAQ for a technical decision (we don't build things because they're cool)

## Strong Signals

- Has worked backwards from customer experience to technical architecture
- Experience with A/B testing frameworks and can explain statistical significance vs practical significance
- Has made a service 10x cheaper to run through architectural changes, not just infrastructure tweaks
- Can explain the CAP theorem implications of a specific system they've built

## Anti-Patterns

- "Microservices" experience that was really just deploying separate repos
- Has never had to debug a cascading failure across multiple services
- Treats operational excellence as someone else's job
- Can't articulate the customer impact of their technical decisions
- Avoids hard conversations about technical tradeoffs ("it depends" without specifics)

## Interview Focus

- System design: How do you build cart functionality that works during Prime Day? What are the failure modes?
- Behavioral deep-dive on ownership: Tell me about a time you fixed something that wasn't your fault but was impacting customers
- Code review simulation: Here's some production code with a subtle race condition — what do you see?
- Disagree and commit scenario: Walk through a time you disagreed with a technical decision but committed to it anyway
