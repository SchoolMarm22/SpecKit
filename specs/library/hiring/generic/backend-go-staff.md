---
kind: hiring
role: Staff Backend Engineer (Go)
team: Backend
level: L6
version: 1
---

# What We're Looking For

I need someone who's moved beyond "how do I build this feature" to "should we build this feature, and if so, how do we build it so it doesn't break in 18 months." Staff engineers at our level own technical strategy for their domain, influence architecture decisions across teams, and mentor other engineers through complex technical decisions.

This isn't about being the best Go programmer in the room (though you should be good). It's about being the person who can look at our monolith-to-microservices migration, understand the organizational dynamics, and chart a path that doesn't crater our delivery velocity. You should have war stories about distributed systems that actually broke in production, not just theoretical knowledge about CAP theorem.

We're specifically looking for someone who's been through at least one major architectural transition at scale - whether that's breaking apart a monolith, migrating databases, or rebuilding core services. The scar tissue from those experiences is what makes staff engineers valuable.

## Must-Haves

- 7+ years backend experience with 4+ years in Go, including designing and implementing distributed systems that handled real production load (10k+ RPS)
- Led a major architectural initiative that spanned multiple teams and took 6+ months to complete
- Mentored senior engineers through complex technical decisions and can point to specific engineers who grew because of your guidance
- Deep understanding of distributed systems patterns - you've debugged race conditions, handled partial failures, and designed for eventual consistency in production
- Experience with observability at scale - you've built monitoring systems, not just used them, and have opinions about SLI/SLO design

## Strong Signals

- Has strong opinions about API design and can articulate why they chose REST vs GraphQL vs gRPC for specific use cases
- Contributed to Go open source projects or has published technical writing about distributed systems
- Experience with multiple data stores (SQL, NoSQL, streaming) and understands when to use each
- Has been the technical lead on a complex migration (database, framework, architecture) that went smoothly
- Can explain distributed systems concepts to non-technical stakeholders without losing the important details

## Anti-Patterns

- Individual contributor mindset - focuses on their own code quality rather than team/org effectiveness
- Architecture astronaut - designs beautiful systems that are impossible to implement or maintain
- Can't explain technical decisions in business terms or understand delivery pressure
- Only worked at large companies with infinite resources - doesn't understand constraint-driven design
- Treats Go like Java/Python - hasn't internalized Go's concurrency model or idioms

## Interview Focus

- System design with real constraints - not just "design Twitter" but "you have 6 months and 3 engineers to replace this legacy system that handles 80% of our revenue"
- Technical leadership stories - times they influenced architecture decisions across teams, resolved technical disagreements, or coached engineers through complex problems
- Go-specific architecture decisions - goroutine design patterns, interface design, error handling strategies, and performance optimization
- Migration strategy and execution - how they've successfully moved production systems without breaking things
