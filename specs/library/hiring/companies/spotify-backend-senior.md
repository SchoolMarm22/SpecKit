---
kind: hiring
role: Senior Backend Engineer
team: Audio Platform
level: L5
version: 1
---

# What We're Looking For

We're not just building another CRUD API. Our squad owns the audio processing pipeline that handles 100 million tracks and 500 million podcast episodes. When an artist uploads a track, we're the ones making sure it sounds great on everything from AirPods to car speakers to that ancient Bluetooth speaker your aunt still uses.

You'll work in a truly autonomous squad — we own everything from the ingestion APIs to the ML models that detect audio quality issues. Our PM doesn't write tickets for us; we identify problems, propose solutions, and ship them. The Audio Platform squad has shipped features that directly impacted DAU, and we can point to the exact A/B tests that proved it.

Audio domain knowledge isn't required, but curiosity about how sound works is essential. The best engineers on our team geek out about codec efficiency and psychoacoustic masking. If you've ever wondered why Spotify sounds better than YouTube Music, you'll fit right in.

## Must-Haves

- Built and scaled event-driven systems handling millions of events/day (we process 2B audio events daily)
- Real experience with Java or Scala in production microservices (not just Spring Boot tutorials)
- Owned an end-to-end feature from conception to A/B test results
- Experience with data pipeline orchestration (Airflow, Luigi, or similar) — our audio processing involves 12-step pipelines
- Can reason about distributed system trade-offs (we're eventually consistent by design, not accident)

## Strong Signals

- Has worked with media processing, codecs, or large file handling
- Built developer tools or internal platforms (bonus points if you've contributed to Backstage)
- Experience with ML feature pipelines or model serving
- Shipped features where latency measurably impacted user behavior
- Comfortable with both sync APIs and async event processing

## Anti-Patterns

- "Microservices" experience that was really just one service calling another
- Can't explain why they chose eventual consistency vs strong consistency for a specific use case
- Views audio/media as "just files" without understanding the domain complexity
- Expects detailed requirements instead of problem statements
- Has never measured the business impact of their technical decisions

## Interview Focus

- System design around audio processing at scale (how would you handle transcoding 100M tracks?)
- Past ownership examples — we want to hear about features they drove from problem identification to impact measurement
- How they've handled the complexity of media formats and codec compatibility
- Their approach to building developer-friendly APIs (our internal customers are other Spotify engineers)
- Experience with gradual rollouts and A/B testing infrastructure
