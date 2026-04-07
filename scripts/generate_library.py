#!/usr/bin/env python3
"""Generate the Hiring Manager Tools spec library.

Creates ~155 hiring specs across roles, levels, and companies using Claude.
Run from the project root: python scripts/generate_library.py

Requires ANTHROPIC_API_KEY in environment.
Estimated cost: ~$0.50-1.00 using Claude Sonnet.
"""

import asyncio
import json
import os
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import anthropic

# ---------------------------------------------------------------------------
# Matrix definitions
# ---------------------------------------------------------------------------

LEVELS = [
    {"label": "Junior", "code": "L3", "slug": "junior"},
    {"label": "Mid-Level", "code": "L4", "slug": "mid"},
    {"label": "Senior", "code": "L5", "slug": "senior"},
    {"label": "Staff", "code": "L6", "slug": "staff"},
]

ROLE_FAMILIES = [
    # Engineering
    {"name": "Frontend Engineer (React)", "slug": "frontend-react", "team": "Frontend", "category": "engineering"},
    {"name": "Frontend Engineer (Angular)", "slug": "frontend-angular", "team": "Frontend", "category": "engineering"},
    {"name": "Frontend Engineer (Vue)", "slug": "frontend-vue", "team": "Frontend", "category": "engineering"},
    {"name": "Backend Engineer (Python)", "slug": "backend-python", "team": "Backend", "category": "engineering"},
    {"name": "Backend Engineer (Node.js)", "slug": "backend-node", "team": "Backend", "category": "engineering"},
    {"name": "Backend Engineer (Go)", "slug": "backend-go", "team": "Backend", "category": "engineering"},
    {"name": "Backend Engineer (Java)", "slug": "backend-java", "team": "Backend", "category": "engineering"},
    {"name": "Backend Engineer (Rust)", "slug": "backend-rust", "team": "Backend", "category": "engineering"},
    {"name": "Full-Stack Engineer", "slug": "fullstack", "team": "Product Engineering", "category": "engineering"},
    {"name": "Mobile Engineer (iOS)", "slug": "mobile-ios", "team": "Mobile", "category": "engineering"},
    {"name": "Mobile Engineer (Android)", "slug": "mobile-android", "team": "Mobile", "category": "engineering"},
    {"name": "DevOps / Platform Engineer", "slug": "devops", "team": "Infrastructure", "category": "engineering"},
    {"name": "Data Engineer", "slug": "data-engineer", "team": "Data", "category": "engineering"},
    {"name": "ML Engineer", "slug": "ml-engineer", "team": "Machine Learning", "category": "engineering"},
    {"name": "Security Engineer", "slug": "security", "team": "Security", "category": "engineering"},
    {"name": "QA / Test Engineer", "slug": "qa", "team": "Quality", "category": "engineering"},
    # Product & Design
    {"name": "Product Manager", "slug": "pm", "team": "Product", "category": "product"},
    {"name": "Product Designer", "slug": "designer", "team": "Design", "category": "product"},
    # Marketing & Growth
    {"name": "Growth Marketer", "slug": "growth-marketer", "team": "Growth", "category": "marketing"},
    {"name": "Content Marketer", "slug": "content-marketer", "team": "Marketing", "category": "marketing"},
    {"name": "Social Media Marketer", "slug": "social-media-marketer", "team": "Marketing", "category": "marketing"},
    {"name": "Email / Lifecycle Marketer", "slug": "email-marketer", "team": "Marketing", "category": "marketing"},
    {"name": "SEO Specialist", "slug": "seo-specialist", "team": "Marketing", "category": "marketing"},
    {"name": "Marketing Analyst", "slug": "marketing-analyst", "team": "Marketing Analytics", "category": "marketing"},
]

# Skip combos that don't make sense
SKIP_COMBOS = {
    ("backend-rust", "junior"),    # Rust junior roles are very rare
    ("security", "junior"),        # Security usually requires experience
    ("ml-engineer", "junior"),     # ML usually requires grad-level knowledge
    ("qa", "staff"),               # Staff QA is uncommon
    ("social-media-marketer", "staff"),  # No staff-level social media
    ("email-marketer", "junior"),  # Email marketing needs some experience
    ("seo-specialist", "junior"),  # SEO needs experience
    ("marketing-analyst", "junior"),  # Analytics needs foundations
}

COMPANIES = [
    {
        "name": "Google",
        "slug": "google",
        "culture": "Design doc culture. Everything gets a doc before it gets code. Promo-driven engineering — impact is measured by launch metrics and peer recognition. Massive scale (billions of users). Strong IC track. Code review is thorough and institutional. Monorepo (google3). Internal tools for everything.",
        "roles": [
            ("Backend Engineer (Go/Java)", "backend", "L5", "senior", "Cloud"),
            ("Frontend Engineer", "frontend", "L5", "senior", "Search"),
            ("ML Engineer", "ml-engineer", "L5", "senior", "DeepMind / Core ML"),
            ("Product Manager", "pm", "L5", "senior", "Search"),
            ("Site Reliability Engineer", "sre", "L5", "senior", "Cloud"),
        ],
    },
    {
        "name": "Apple",
        "slug": "apple",
        "culture": "Secrecy is cultural — teams don't know what other teams are building. Hardware-software integration is the competitive advantage. Craft over speed. Polish matters more than shipping fast. Small teams with enormous scope. DRI (Directly Responsible Individual) model.",
        "roles": [
            ("iOS Engineer", "ios", "L5", "senior", "iOS Frameworks"),
            ("Frontend Engineer", "frontend", "L5", "senior", "Apple Music"),
            ("Security Engineer", "security", "L5", "senior", "Platform Security"),
            ("Product Manager", "pm", "L5", "senior", "Hardware-Software"),
            ("Product Designer", "designer", "L5", "senior", "Human Interface"),
        ],
    },
    {
        "name": "Amazon",
        "slug": "amazon",
        "culture": "Leadership Principles drive everything — 'Ownership', 'Bias for Action', 'Disagree and Commit', 'Dive Deep'. PRFAQ culture (press release written before building). Two-pizza teams. Service-oriented architecture since 2002. Frugality is a value. Bar raiser program in hiring. Oncall is everyone's job.",
        "roles": [
            ("Backend Engineer (Java)", "backend", "L5", "senior", "AWS"),
            ("Full-Stack Engineer", "fullstack", "L5", "senior", "Retail"),
            ("DevOps / Platform Engineer", "devops", "L5", "senior", "AWS Infrastructure"),
            ("Product Manager", "pm", "L5", "senior", "Retail / AWS"),
            ("Data Engineer", "data-engineer", "L5", "senior", "Supply Chain"),
        ],
    },
    {
        "name": "Netflix",
        "slug": "netflix",
        "culture": "Freedom and Responsibility — no vacation policy, no expense policy, trust people to make good decisions. Context not control. Keeper test: would you fight to keep this person? Extremely high talent density. Pay top-of-market. No stack ranking. Candor is expected.",
        "roles": [
            ("Backend Engineer", "backend", "L5", "senior", "Streaming Platform"),
            ("Frontend Engineer", "frontend", "L5", "senior", "UI Platform"),
            ("Data Engineer", "data-engineer", "L5", "senior", "Content Analytics"),
            ("ML Engineer", "ml-engineer", "L5", "senior", "Recommendations"),
            ("Product Manager", "pm", "L5", "senior", "Studio Technology"),
        ],
    },
    {
        "name": "Meta",
        "slug": "meta",
        "culture": "Move fast. Impact over process. Open source culture (React, PyTorch, Llama). Internal bootcamp for new engineers — pick your team after joining. Hackathons are real (features ship from them). Performance reviews driven by impact and peer calibration. Massive internal tools ecosystem.",
        "roles": [
            ("Frontend Engineer (React)", "frontend-react", "L5", "senior", "Product"),
            ("Backend Engineer", "backend", "L5", "senior", "Infrastructure"),
            ("ML Engineer", "ml-engineer", "L5", "senior", "AI / GenAI"),
            ("Mobile Engineer (Android)", "mobile-android", "L5", "senior", "Instagram"),
            ("Growth Marketer", "growth-marketer", "L5", "senior", "Growth"),
        ],
    },
    {
        "name": "Microsoft",
        "slug": "microsoft",
        "culture": "Growth mindset (Satya-era transformation). Enterprise scale — your code runs in every Fortune 500 company. Azure is the strategic bet. TypeScript, C#, .NET ecosystem. Strong research org (MSR). Inclusive culture push. Model-based reasoning. Ship on cadence (Windows, Office, Azure).",
        "roles": [
            ("Backend Engineer (.NET/C#)", "backend-dotnet", "L5", "senior", "Azure"),
            ("Frontend Engineer", "frontend", "L5", "senior", "Office / Teams"),
            ("DevOps / Platform Engineer", "devops", "L5", "senior", "Azure DevOps"),
            ("Product Manager", "pm", "L5", "senior", "Azure / M365"),
            ("Security Engineer", "security", "L5", "senior", "Identity & Security"),
        ],
    },
    {
        "name": "Stripe",
        "slug": "stripe",
        "culture": "Writing culture — memos, not meetings. Developer experience is a product principle. Ruby and Go backend. Extremely high code quality bar. API design is craft. Long-term thinking. Small teams. Users are developers. Every engineer does oncall.",
        "roles": [
            ("Backend Engineer (Ruby/Go)", "backend", "L5", "senior", "Payments"),
            ("Frontend Engineer", "frontend", "L5", "senior", "Dashboard"),
            ("Product Manager", "pm", "L5", "senior", "Payments Platform"),
            ("Product Designer", "designer", "L5", "senior", "Developer Experience"),
            ("DevOps / Platform Engineer", "devops", "L5", "senior", "Infrastructure"),
        ],
    },
    {
        "name": "Airbnb",
        "slug": "airbnb",
        "culture": "Belonging is the mission. Design-driven culture (co-founder is a designer). Host and guest empathy required. Service-oriented architecture. Strong internal design system. Went through massive layoffs in 2020 and rebuilt leaner. Brian Chesky involved in product details. Quality of craft matters.",
        "roles": [
            ("Frontend Engineer", "frontend", "L5", "senior", "Guest Experience"),
            ("Full-Stack Engineer", "fullstack", "L5", "senior", "Host Platform"),
            ("Product Designer", "designer", "L5", "senior", "Core Experience"),
            ("Product Manager", "pm", "L5", "senior", "Search & Discovery"),
            ("Data Engineer", "data-engineer", "L5", "senior", "Marketplace"),
        ],
    },
    {
        "name": "Shopify",
        "slug": "shopify",
        "culture": "Merchant obsession. Ruby on Rails at scale (one of the largest Rails apps). React + Polaris design system for frontend. Remote-first (Digital by Default). Craft at scale. GSD (Get Shit Done) culture under Tobi. Internal hackdays called 'Hack Days'. Strong CLI/developer tooling culture.",
        "roles": [
            ("Frontend Engineer", "frontend", "L5", "senior", "Storefront"),
            ("Full-Stack Engineer (Rails)", "fullstack", "L5", "senior", "Core"),
            ("Mobile Engineer", "mobile", "L5", "senior", "Shop App"),
            ("Product Manager", "pm", "L5", "senior", "Merchant Experience"),
            ("Data Engineer", "data-engineer", "L5", "senior", "Commerce Analytics"),
        ],
    },
    {
        "name": "Spotify",
        "slug": "spotify",
        "culture": "Squad/tribe/guild model (though evolved from original). Autonomous squads own their domain end-to-end. Music and audio domain knowledge valued. Data-driven product decisions. Strong backend systems (Java/Python). Backstage (open-source developer portal) came from here. Distributed across Europe and US.",
        "roles": [
            ("Backend Engineer", "backend", "L5", "senior", "Audio Platform"),
            ("Frontend Engineer", "frontend", "L5", "senior", "Web Player"),
            ("Mobile Engineer", "mobile", "L5", "senior", "iOS/Android"),
            ("ML Engineer", "ml-engineer", "L5", "senior", "Personalization"),
            ("Data Engineer", "data-engineer", "L5", "senior", "Listening Analytics"),
        ],
    },
    {
        "name": "Uber",
        "slug": "uber",
        "culture": "Marketplace complexity — matching supply and demand in real-time across cities. Reliability at scale (millions of trips/day). Strong Go backend. Geo-spatial systems. Growth engineering culture. Moved from 'hustle' to more structured engineering post-2017. Real-time systems and low-latency requirements.",
        "roles": [
            ("Backend Engineer (Go)", "backend-go", "L5", "senior", "Marketplace"),
            ("Mobile Engineer", "mobile", "L5", "senior", "Rider/Driver Apps"),
            ("ML Engineer", "ml-engineer", "L5", "senior", "Pricing & ETA"),
            ("Data Engineer", "data-engineer", "L5", "senior", "Marketplace Analytics"),
            ("Platform Engineer", "platform", "L5", "senior", "Developer Platform"),
        ],
    },
    {
        "name": "Coinbase",
        "slug": "coinbase",
        "culture": "Crypto-native — you should believe in the mission. Remote-first. Compliance and security are existential (regulated financial institution). Go backend, React frontend. Move carefully in a fast-moving space. Strong testing culture (financial correctness matters). On-chain and off-chain systems.",
        "roles": [
            ("Backend Engineer (Go)", "backend-go", "L5", "senior", "Trading Platform"),
            ("Frontend Engineer", "frontend", "L5", "senior", "Consumer App"),
            ("Security Engineer", "security", "L5", "senior", "Crypto Security"),
            ("Mobile Engineer", "mobile", "L5", "senior", "Coinbase App"),
            ("DevOps / Platform Engineer", "devops", "L5", "senior", "Blockchain Infrastructure"),
        ],
    },
    {
        "name": "Datadog",
        "slug": "datadog",
        "culture": "Observability domain expertise. Performance-sensitive systems (processing trillions of data points). Go backend, React frontend. Dogfooding culture — you use what you build. Strong engineering culture with focus on system design. Competitive market (vs Splunk, New Relic, Grafana).",
        "roles": [
            ("Backend Engineer (Go)", "backend-go", "L5", "senior", "Metrics Pipeline"),
            ("Frontend Engineer", "frontend", "L5", "senior", "Dashboards"),
            ("Site Reliability Engineer", "sre", "L5", "senior", "Platform"),
            ("Data Engineer", "data-engineer", "L5", "senior", "Log Analytics"),
            ("DevOps / Platform Engineer", "devops", "L5", "senior", "Internal Platform"),
        ],
    },
    {
        "name": "Figma",
        "slug": "figma",
        "culture": "Design tools for designers — the product IS the craft. Multiplayer/real-time collaboration is the core technical challenge. WebGL, WASM, C++ compiled to web. Small team, enormous impact. Design-engineering partnership is genuine, not performative. Recently acquired then un-acquired (independent). Speed of iteration matters.",
        "roles": [
            ("Frontend Engineer", "frontend", "L5", "senior", "Editor"),
            ("Backend Engineer", "backend", "L5", "senior", "Collaboration"),
            ("Product Designer", "designer", "L5", "senior", "Core Editor"),
            ("Product Manager", "pm", "L5", "senior", "Developer Platform"),
            ("Full-Stack Engineer", "fullstack", "L5", "senior", "FigJam"),
        ],
    },
    {
        "name": "Linear",
        "slug": "linear",
        "culture": "Craft and speed. Small team building the best project management tool for software teams. Opinionated product design. Keyboard-first UX. TypeScript everywhere. Performance is a feature (60fps animations in a web app). No enterprise bloat. Quality over quantity in hiring.",
        "roles": [
            ("Frontend Engineer", "frontend", "L5", "senior", "Product"),
            ("Backend Engineer", "backend", "L5", "senior", "Core"),
            ("Product Designer", "designer", "L5", "senior", "Product"),
            ("Full-Stack Engineer", "fullstack", "L5", "senior", "Integrations"),
            ("Product Manager", "pm", "L5", "senior", "Core Product"),
        ],
    },
]

# ---------------------------------------------------------------------------
# Example specs (for voice/tone reference in the prompt)
# ---------------------------------------------------------------------------

EXAMPLE_SPEC_1 = """---
kind: hiring
role: Senior Frontend Engineer
team: Platform
level: L5
version: 1
---

# What We're Looking For

Prefer candidates with real startup experience. Full-stack at a 200-person
company is different from full-stack at a 5-person startup. At a small
startup, "full-stack" means you were the stack.

I'd rather hire someone with 2 years at a real startup than 5 years at
Google, unless the Google person can clearly articulate what *they* built
vs. what the team built.

## Must-Haves

- Shipped production React at scale (>100k users)
- Owned a frontend architecture decision that went wrong and can talk
  about what they learned
- Can write CSS without a framework. Tailwind is fine but shouldn't be
  a dependency on their ability to think about layout.

## Strong Signals

- Open source contributions (shows they write code meant to be read)
- Has mentored junior engineers (we're growing the team from 3 to 8)
- Experience with design systems or component libraries

## Anti-Patterns

- "Full-stack" experience that was really just touching a REST endpoint
- Can't explain tradeoffs in their own architectural decisions
- Only ever worked on greenfield projects (we have legacy code, it's real)
- Dismissive of accessibility or performance as "nice to haves"

## Interview Focus

- Real ownership vs. proximity to impressive work
- How they handle technical disagreements
- Whether they've ever been wrong about an architecture decision"""

EXAMPLE_SPEC_2 = """---
kind: hiring
role: DevOps Lead
team: Infrastructure
level: L5
version: 1
---

# What We're Looking For

Someone who's been on-call at 3am and knows what it feels like when
the alerts fire and nobody else is awake. We need a lead who has
lived through outages, not just read about incident management in
a book.

## Must-Haves

- Operated production Kubernetes clusters (not just deployed to them)
- Built or significantly improved a CI/CD pipeline end-to-end
- On-call experience with real incident response (not simulated)
- Terraform or equivalent IaC at scale (50+ resources managed)

## Strong Signals

- Has strong opinions about monitoring that go beyond "we use Datadog"
- Can explain the tradeoff between build speed and build reliability

## Anti-Patterns

- "DevOps" experience that was really just writing YAML for someone
  else's pipeline
- Can't explain their alerting philosophy beyond "we alert on errors"
- Treats infrastructure as a cost center rather than a product

## Interview Focus

- Incident stories: what happened, what they did, what they'd do
  differently. The "differently" part is the signal.
- Pipeline philosophy: why their pipeline is shaped the way it is."""

# ---------------------------------------------------------------------------
# Prompt template
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """You are a hiring spec file generator for Hiring Manager Tools, an open-source spec-file engine.

You generate realistic, opinionated hiring spec files that read like they were written by an experienced hiring manager — not generic HR boilerplate.

Rules:
1. Write in first person, from the hiring manager's perspective
2. Be specific and opinionated — mention real technologies, real tradeoffs, real antipatterns
3. Must-Haves should have 3-5 items, each concrete and evaluable
4. Strong Signals should have 3-5 items
5. Anti-Patterns should have 3-5 items that reveal real hiring mistakes
6. Interview Focus should have 3-5 specific areas to probe
7. The preamble (before ## Must-Haves) should be 2-3 paragraphs explaining what makes this role unique
8. Calibrate expectations to the level — junior should expect learning potential, staff should expect system-level thinking
9. For company-specific specs, deeply reflect that company's actual engineering culture, values, and technical stack
10. Output ONLY the spec file content (frontmatter + markdown body), no explanation

Here are two example specs showing the voice and format:

--- EXAMPLE 1 ---
{example1}

--- EXAMPLE 2 ---
{example2}
""".format(example1=EXAMPLE_SPEC_1, example2=EXAMPLE_SPEC_2)


def build_generic_prompt(role: dict, level: dict) -> str:
    return f"""Generate a hiring spec for:

Role: {level['label']} {role['name']}
Team: {role['team']}
Level: {level['code']}

This is a generic spec (not company-specific). It should reflect industry-standard expectations for a {level['label'].lower()} {role['name'].lower()} at a typical tech company.

{'For this junior role, emphasize learning potential, growth mindset, and foundational skills over years of experience.' if level['slug'] == 'junior' else ''}
{'For this mid-level role, emphasize independent execution, solid technical foundations, and growing ownership.' if level['slug'] == 'mid' else ''}
{'For this senior role, emphasize technical leadership, architectural judgment, mentoring, and cross-team impact.' if level['slug'] == 'senior' else ''}
{'For this staff role, emphasize system-level thinking, org-wide influence, technical strategy, and force-multiplier impact.' if level['slug'] == 'staff' else ''}

Output the complete spec file with YAML frontmatter and markdown body."""


def build_company_prompt(company: dict, role_info: tuple) -> str:
    role_title, role_slug, level_code, level_slug, team = role_info
    level_label = next(l['label'] for l in LEVELS if l['slug'] == level_slug)

    return f"""Generate a hiring spec for:

Role: {level_label} {role_title}
Team: {team}
Level: {level_code}
Company: {company['name']}

Company culture context:
{company['culture']}

This spec should deeply reflect {company['name']}'s actual engineering culture, interview style, and technical values. Don't just mention the company name — write it in the voice of a {company['name']} hiring manager who cares about what makes their team different.

Output the complete spec file with YAML frontmatter and markdown body."""


# ---------------------------------------------------------------------------
# Generation logic
# ---------------------------------------------------------------------------

@dataclass
class SpecJob:
    """A single spec to generate."""
    prompt: str
    output_path: str
    label: str  # For progress logging


def build_job_list(base_dir: str) -> list[SpecJob]:
    """Build the full list of specs to generate."""
    jobs = []

    # Generic specs
    for role in ROLE_FAMILIES:
        for level in LEVELS:
            if (role["slug"], level["slug"]) in SKIP_COMBOS:
                continue

            filename = f"{role['slug']}-{level['slug']}.md"
            output_path = os.path.join(base_dir, "generic", filename)
            prompt = build_generic_prompt(role, level)
            label = f"generic/{filename}"
            jobs.append(SpecJob(prompt=prompt, output_path=output_path, label=label))

    # Company specs
    for company in COMPANIES:
        for role_info in company["roles"]:
            role_title, role_slug, level_code, level_slug, team = role_info
            filename = f"{company['slug']}-{role_slug}-{level_slug}.md"
            output_path = os.path.join(base_dir, "companies", filename)
            prompt = build_company_prompt(company, role_info)
            label = f"companies/{filename}"
            jobs.append(SpecJob(prompt=prompt, output_path=output_path, label=label))

    return jobs


async def generate_spec(
    client: anthropic.AsyncAnthropic,
    job: SpecJob,
    semaphore: asyncio.Semaphore,
    model: str = "claude-sonnet-4-20250514",
) -> tuple[str, bool, str]:
    """Generate a single spec file. Returns (label, success, error_or_empty)."""
    async with semaphore:
        # Skip if already exists
        if os.path.exists(job.output_path):
            return (job.label, True, "skipped (exists)")

        try:
            response = await client.messages.create(
                model=model,
                max_tokens=2000,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": job.prompt}],
            )

            content = response.content[0].text.strip()

            # Validate it starts with frontmatter
            if not content.startswith("---"):
                return (job.label, False, "Output missing frontmatter")

            # Write to file
            os.makedirs(os.path.dirname(job.output_path), exist_ok=True)
            with open(job.output_path, "w", encoding="utf-8") as f:
                f.write(content + "\n")

            return (job.label, True, "")

        except Exception as e:
            return (job.label, False, str(e))


async def main():
    base_dir = os.path.join("specs", "library", "hiring")

    print("Building job list...")
    jobs = build_job_list(base_dir)
    print(f"Total specs to generate: {len(jobs)}")

    generic_count = sum(1 for j in jobs if "generic/" in j.label)
    company_count = sum(1 for j in jobs if "companies/" in j.label)
    print(f"  Generic: {generic_count}")
    print(f"  Company-specific: {company_count}")
    print()

    # Check for API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set")
        sys.exit(1)

    client = anthropic.AsyncAnthropic()
    semaphore = asyncio.Semaphore(8)  # Max 8 concurrent requests

    print("Generating specs...")
    start_time = time.time()

    tasks = [generate_spec(client, job, semaphore) for job in jobs]
    results = await asyncio.gather(*tasks)

    elapsed = time.time() - start_time

    # Report
    successes = sum(1 for _, ok, _ in results if ok)
    failures = [(label, err) for label, ok, err in results if not ok]
    skipped = sum(1 for _, _, msg in results if msg == "skipped (exists)")

    print(f"\nDone in {elapsed:.1f}s")
    print(f"  Generated: {successes - skipped}")
    print(f"  Skipped (already exist): {skipped}")
    print(f"  Failed: {len(failures)}")

    if failures:
        print("\nFailures:")
        for label, err in failures:
            print(f"  {label}: {err}")

    # Validate all generated specs
    print("\nValidating specs...")
    sys.path.insert(0, os.getcwd())
    from hiring_manager_tools.spec import parse_spec

    valid = 0
    invalid = 0
    for job in jobs:
        if os.path.exists(job.output_path):
            with open(job.output_path, "r") as f:
                text = f.read()
            try:
                spec = parse_spec(text)
                if spec.kind == "hiring":
                    valid += 1
                else:
                    print(f"  WARN: {job.label} has kind='{spec.kind}' (expected 'hiring')")
                    invalid += 1
            except Exception as e:
                print(f"  INVALID: {job.label}: {e}")
                invalid += 1

    print(f"  Valid: {valid}")
    print(f"  Invalid: {invalid}")


if __name__ == "__main__":
    asyncio.run(main())
