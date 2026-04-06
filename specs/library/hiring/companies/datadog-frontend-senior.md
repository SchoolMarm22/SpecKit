---
kind: hiring
role: Senior Frontend Engineer
team: Dashboards
level: L5
company: Datadog
version: 1
---

# What We're Looking For

Our dashboards render millions of metrics in real-time for customers monitoring everything from Kubernetes clusters to payment pipelines. When Shopify's Black Friday traffic spikes, they're staring at our charts. When that chart takes 3 seconds to load instead of 300ms, that's an engineer somewhere having a bad day.

You'll be building React components that handle massive datasets without choking the browser. We're not a typical CRUD app — we're more like building Grafana, but faster, prettier, and with better UX. Our users are engineers who know when something feels slow, so performance isn't negotiable.

We dogfood everything. Your dashboard improvements will make your own on-call shifts better. You'll use our APM to debug the React app you're building, creating that tight feedback loop that makes our product actually good.

## Must-Haves

- Built high-performance React apps that handle large datasets (100k+ DOM elements, real-time updates)
- Experience with charting libraries (D3, Chart.js, or similar) and understands canvas vs SVG tradeoffs for performance
- Has optimized bundle size and runtime performance in a meaningful way — can talk specific techniques beyond "I used React.memo"
- Comfortable reading Go code and working with REST/GraphQL APIs at scale
- Experience with real-time data visualization or live-updating interfaces

## Strong Signals

- Has worked on developer tools, monitoring, or observability products
- Understands the performance implications of React rendering patterns with large datasets
- Experience with data visualization UX — knows when a line chart vs heatmap vs table makes sense
- Can articulate frontend monitoring and observability strategies (yes, we monitor our own frontend)

## Anti-Patterns

- Frontend experience limited to typical web apps — no experience with data-heavy interfaces
- Treats performance as an afterthought rather than a design constraint
- Can't explain why their React app is slow beyond "there's too much data"
- Dismisses accessibility in data visualization as "too hard" or "not relevant"
- Never used the tools they're building (hasn't been on-call, doesn't understand monitoring workflows)

## Interview Focus

- How they'd approach rendering 10,000 time series without killing the browser
- System design for real-time dashboard updates — what gets updated when and why
- Performance debugging story — walk through a specific optimization they made and the measurable impact
- Understanding of our users — how do engineers actually use dashboards during incidents vs normal operations
