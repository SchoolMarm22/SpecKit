---
kind: hiring
role: Senior Full-Stack Engineer
team: Integrations
level: L5
version: 1
---

# What We're Looking For

We're building integrations that feel like they're part of Linear itself, not bolted-on afterthoughts. When someone connects GitHub or Slack, it should feel as fast and polished as our core issue tracking. This means understanding both external APIs and our own performance constraints — animations still need to hit 60fps even when syncing thousands of GitHub issues.

You'll own the full stack of integration experiences, from the OAuth flows users see to the sync engines running in our infrastructure. We're not looking for someone who treats integrations as CRUD operations. We need someone who thinks about rate limits, webhook reliability, and data consistency while maintaining the craft standards that make Linear feel different.

This role involves a lot of reading other companies' API documentation and finding elegant ways to map their mental models onto ours. You should enjoy the puzzle of making disparate systems work together seamlessly.

## Must-Haves

- Built and maintained webhook systems at scale (handling failures, retries, deduplication)
- Deep TypeScript experience with strong opinions about type safety in integration layers
- Experience with OAuth 2.0 flows and API authentication patterns beyond "add the token to headers"
- Owned performance optimizations in a React application — can explain specific techniques you used
- Built or maintained integrations between complex systems where data consistency actually mattered

## Strong Signals

- Has reverse-engineered an API that had poor documentation
- Experience with GraphQL federation or stitching multiple data sources
- Understanding of database transaction patterns for sync operations
- Can articulate opinions about webhook vs polling tradeoffs
- Built developer tools or worked on products that other engineers use

## Anti-Patterns

- "Integration experience" that was really just calling REST endpoints from frontend code
- Thinks performance is about caching everything rather than fundamentally fast operations
- Can't explain how they would handle a webhook endpoint being down for 6 hours
- Treats TypeScript like JavaScript with optional types
- Dismisses animation and interaction details as "design team problems"

## Interview Focus

- System design for bidirectional sync (GitHub issues ↔ Linear issues, handling conflicts)
- Code review of TypeScript integration code — how they structure types and handle errors
- Performance debugging scenario in a React app with complex data flows
- API design philosophy: how they would design webhooks for Linear's API
- Specific examples of integration challenges they've solved and the edge cases they discovered
