---
kind: hiring
role: Senior Backend Engineer (Go/Java)
team: Cloud
level: L5
version: 1
---

# What We're Looking For

I need someone who understands that at Google scale, elegance matters more than cleverness. We're looking for an engineer who has written design docs that actually influenced system architecture, not just documented what was already built. The kind of person who thinks through edge cases before writing the first line of code.

Our systems handle traffic spikes that would crash most companies' entire infrastructure on a normal Tuesday. I want someone who has lived through the pain of premature optimization and learned when *not* to optimize. Someone who can write Go that doesn't just work, but works when it's handling 10x the expected load because someone posted our API on Hacker News.

The best engineers I've hired understand that code review isn't a formality — it's where the real system design happens. They write CLs that reviewers actually want to read, with commit messages that explain the *why* behind every design decision.

## Must-Haves

- Designed and implemented distributed systems that handle >1M QPS
- Written design docs that got adopted (not just approved) by senior engineers
- Go or Java experience at scale — can explain memory allocation patterns and GC impact on tail latency
- Production experience with microservices communication patterns (gRPC, pub/sub, event-driven architectures)
- Has debugged performance issues using profiling tools and distributed tracing

## Strong Signals

- Contributing member of design review committees or architecture forums
- Experience with capacity planning and load testing at scale
- Has mentored other engineers through the promotion process
- Open source contributions to infrastructure projects (shows they think beyond their immediate team)
- Can articulate specific tradeoffs between consistency, availability, and partition tolerance in real systems

## Anti-Patterns

- "Distributed systems" experience that was really just calling other teams' APIs
- Can't explain why they chose their current architecture over alternatives
- Writes code first, design doc later (or never)
- Thinks code review is about catching syntax errors
- Has never been on-call or doesn't understand operational impact of their code

## Interview Focus

- System design: not just drawing boxes, but explaining failure modes and capacity planning
- Code design: can they write clean, testable Go/Java that other engineers want to maintain?
- Technical leadership: how do they influence technical decisions without formal authority?
- Design doc quality: can they think through a problem systematically before coding?
- Scale challenges: what breaks when you go from 1K to 1M to 1B users?
