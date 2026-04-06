---
role: Senior Backend Engineer
team: Collaboration
level: L5
company: Figma
version: 1
---

# What We're Looking For

We're not building another CRUD app. Every keystroke, every cursor movement, every layer change needs to propagate to dozens of collaborators in real-time without conflicts. When a designer moves a rectangle in San Francisco, another designer in Tokyo sees it move smoothly 200ms later, not as a jarring jump.

The technical challenges here are genuinely hard: operational transforms, conflict-free replicated data types, handling network partitions gracefully while maintaining the illusion of seamless collaboration. We need someone who gets excited about these problems, not someone who sees them as obstacles to shipping features.

You'll be working closely with our design team — not in the "eng and design collaborate" buzzword way, but in the "you need to understand visual hierarchy to architect how layer operations propagate" way. Our designers use our product to design our product. That feedback loop shapes everything.

## Must-Haves

- Built real-time collaborative systems at scale (not just chat or comments)
- Deep understanding of distributed systems fundamentals: consensus, eventual consistency, conflict resolution
- Experience with operational transforms or CRDTs in production
- Can reason about performance at the data structure level — knows when a tree becomes a problem and what to do about it
- Shipped systems that handle network partitions gracefully

## Strong Signals

- Has debugged race conditions in collaborative editing systems
- Experience with high-frequency state synchronization (60fps+ user interactions)
- Built or contributed to developer tools, creative software, or other products where performance is user-visible
- Can articulate tradeoffs between strong consistency and user experience

## Anti-Patterns

- "Real-time" experience that's actually just WebSockets for notifications
- Treats collaboration as an afterthought that can be "added later"
- Can't explain why their system works without handwaving about "eventual consistency"
- Dismisses frontend performance concerns as "not my problem"
- Has never had to explain a technical decision to a non-engineer

## Interview Focus

- Collaborative editing scenarios: "Two users select the same object and start dragging it in opposite directions. Walk me through your system's behavior."
- System design that considers the human experience, not just technical correctness
- How they think about data models when user interactions happen faster than network round-trips
- Real examples of performance debugging in distributed systems
