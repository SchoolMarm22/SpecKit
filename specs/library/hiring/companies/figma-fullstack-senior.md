---
kind: hiring
role: Senior Full-Stack Engineer
team: FigJam
level: L5
version: 1
---

# What We're Looking For

FigJam isn't just another whiteboard tool — it's a multiplayer canvas where ideas come alive in real-time. Every pixel matters, every interaction needs to feel delightful, and when someone draws a sticky note in Tokyo, it better show up instantly in San Francisco without any flicker or lag.

We're looking for an engineer who gets excited about the intersection of craft and performance. Someone who's built real-time systems before and knows that "eventually consistent" isn't good enough when five people are trying to move the same object simultaneously. You should care as much about the 60fps smoothness of a drag interaction as you do about the elegance of your operational transform algorithms.

The best candidates understand that at Figma, engineering and design aren't separate disciplines — we're all building tools for makers, which means we have to be makers ourselves.

## Must-Haves

- Shipped real-time collaborative features in production (WebRTC, WebSockets, or operational transforms)
- Deep Canvas API or WebGL experience — you've wrestled with coordinate systems and rendering performance
- Built multiplayer state synchronization that handles conflicts gracefully
- Experience optimizing JavaScript performance at the micro level (frame budgets, garbage collection, memory management)
- Track record of working closely with designers to implement pixel-perfect, 60fps interactions

## Strong Signals

- Has debugged race conditions in distributed systems or real-time applications
- Can articulate the tradeoffs between different conflict resolution strategies (last-write-wins vs. operational transforms vs. CRDTs)
- Experience with high-performance web technologies (WASM, SharedArrayBuffer, OffscreenCanvas)
- Built developer tools or creative software where the UX bar is exceptionally high
- Open source contributions to graphics, real-time, or creative coding libraries

## Anti-Patterns

- "Real-time" experience that was actually just polling every few seconds
- Can't explain why their last performance optimization actually worked
- Treats design feedback as implementation details rather than product requirements
- Full-stack experience limited to CRUD apps with traditional request-response patterns
- Dismisses browser compatibility or performance constraints as "edge cases"

## Interview Focus

- Walk through a complex real-time feature they built — how they handled edge cases, race conditions, and performance
- How they approach debugging performance issues in the browser (profiling, flame graphs, actual methodology)
- Design partnership: examples of pushing back on designs for technical reasons vs. finding creative technical solutions
- System design for real-time collaboration — how would they architect cursor sharing or live editing?
- Code review: looking at actual FigJam performance-critical code and discussing optimization approaches
