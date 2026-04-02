---
kind: hiring
role: DevOps Lead
team: Infrastructure
level: L5
version: 1
author: marcus.wong
---

# What We're Looking For

Someone who's been on-call at 3am and knows what it feels like when
the alerts fire and nobody else is awake. We need a lead who has
lived through outages, not just read about incident management in
a book.

This person will own our CI/CD pipeline, cloud infrastructure, and
reliability culture. They need to be technical enough to debug a
Kubernetes networking issue and senior enough to present an
infrastructure roadmap to the VP of Engineering.

## Must-Haves

- Operated production Kubernetes clusters (not just deployed to them)
- Built or significantly improved a CI/CD pipeline end-to-end
- On-call experience with real incident response (not simulated)
- Terraform or equivalent IaC at scale (50+ resources managed)

## Strong Signals

- Has strong opinions about monitoring that go beyond "we use Datadog"
- Can explain the tradeoff between build speed and build reliability
  in their own CI/CD system
- Has reduced on-call burden for a team (not just carried it)
- Open source infrastructure contributions

## Anti-Patterns

- "DevOps" experience that was really just writing YAML for someone
  else's pipeline
- Can't explain their alerting philosophy beyond "we alert on errors"
- Has never debugged a production issue they didn't cause themselves
- Treats infrastructure as a cost center rather than a product

## Interview Focus

- Incident stories: what happened, what they did, what they'd do
  differently. The "differently" part is the signal.
- Pipeline philosophy: why their pipeline is shaped the way it is,
  not just what tools it uses.
- How they'd approach our current pain point: deploys take 45 minutes
  and developers avoid deploying on Fridays.
