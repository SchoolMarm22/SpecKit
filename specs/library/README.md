# Spec Library

A collection of ~160 ready-to-use hiring specs covering the full landscape of tech company roles.

## Structure

```
specs/library/hiring/
├── generic/           # Role x level matrix (no company-specific culture)
│   ├── frontend-react-junior.md
│   ├── frontend-react-mid.md
│   ├── frontend-react-senior.md
│   ├── frontend-react-staff.md
│   ├── backend-python-junior.md
│   └── ...
└── companies/         # Company-specific specs reflecting real engineering culture
    ├── google-backend-senior.md
    ├── apple-ios-senior.md
    ├── amazon-backend-senior.md
    ├── netflix-backend-senior.md
    ├── meta-frontend-react-senior.md
    ├── stripe-backend-senior.md
    └── ...
```

## Generic Specs

Covers 24 role families across 4 levels:

### Engineering Roles
| Role | Junior | Mid | Senior | Staff |
|------|--------|-----|--------|-------|
| Frontend (React) | x | x | x | x |
| Frontend (Angular) | x | x | x | x |
| Frontend (Vue) | x | x | x | x |
| Backend (Python) | x | x | x | x |
| Backend (Node.js) | x | x | x | x |
| Backend (Go) | x | x | x | x |
| Backend (Java) | x | x | x | x |
| Backend (Rust) | - | x | x | x |
| Full-Stack | x | x | x | x |
| Mobile (iOS) | x | x | x | x |
| Mobile (Android) | x | x | x | x |
| DevOps / Platform | x | x | x | x |
| Data Engineer | x | x | x | x |
| ML Engineer | - | x | x | x |
| Security Engineer | - | x | x | x |
| QA / Test Engineer | x | x | x | - |

### Product & Design
| Role | Junior | Mid | Senior | Staff |
|------|--------|-----|--------|-------|
| Product Manager | x | x | x | x |
| Product Designer | x | x | x | x |

### Marketing & Growth
| Role | Junior | Mid | Senior | Staff |
|------|--------|-----|--------|-------|
| Growth Marketer | x | x | x | x |
| Content Marketer | x | x | x | x |
| Social Media Marketer | x | x | x | - |
| Email / Lifecycle Marketer | - | x | x | x |
| SEO Specialist | - | x | x | x |
| Marketing Analyst | - | x | x | x |

## Company-Specific Specs

15 companies, ~5 roles each. These specs reflect the company's actual engineering culture, interview style, and technical values.

| Company | Culture Angle | Roles |
|---------|--------------|-------|
| **Google** | Design doc culture, scale, promo-driven | Backend, Frontend, ML, PM, SRE |
| **Apple** | Secrecy, craft, hardware-software | iOS, Frontend, Security, PM, Designer |
| **Amazon** | Leadership Principles, ownership, PRFAQ | Backend, Full-Stack, DevOps, PM, Data |
| **Netflix** | Freedom & responsibility, talent density | Backend, Frontend, Data, ML, PM |
| **Meta** | Move fast, impact, open source | Frontend (React), Backend, ML, Mobile, Growth |
| **Microsoft** | Growth mindset, enterprise scale | Backend (.NET), Frontend, DevOps, PM, Security |
| **Stripe** | Writing culture, API craft, developer UX | Backend (Ruby/Go), Frontend, PM, Designer, DevOps |
| **Airbnb** | Belonging, design-driven, empathy | Frontend, Full-Stack, Designer, PM, Data |
| **Shopify** | Merchant obsession, Rails at scale | Frontend, Full-Stack, Mobile, PM, Data |
| **Spotify** | Squad model, autonomy, music domain | Backend, Frontend, Mobile, ML, Data |
| **Uber** | Marketplace complexity, reliability | Backend (Go), Mobile, ML, Data, Platform |
| **Coinbase** | Crypto-native, compliance, security | Backend (Go), Frontend, Security, Mobile, DevOps |
| **Datadog** | Observability domain, performance | Backend (Go), Frontend, SRE, Data, DevOps |
| **Figma** | Design tools, multiplayer, WebGL/WASM | Frontend, Backend, Designer, PM, Full-Stack |
| **Linear** | Craft, speed, keyboard-first | Frontend, Backend, Designer, Full-Stack, PM |

## Using Library Specs

```bash
# List all library specs
speckit list --specs-dir specs/library --kind hiring --pretty

# Use a library spec for interview prep
speckit prep --spec library/hiring/generic/frontend-react-senior --resume ./resume.txt --specs-dir specs --pretty

# Lint a library spec
speckit lint --spec library/hiring/companies/google-backend-senior --specs-dir specs --pretty
```

## Regenerating

The library was generated using `scripts/generate_library.py`:

```bash
export ANTHROPIC_API_KEY=your-key
python3 scripts/generate_library.py
```

The script is idempotent — it skips specs that already exist. Delete a file to regenerate it.

## Customizing

These specs are starting points. Copy one to `specs/hiring/`, edit it to reflect your actual team's priorities, and use it with Hiring Manager Tools:

```bash
cp specs/library/hiring/generic/backend-python-senior.md specs/hiring/my-backend-role.md
# Edit to taste, then:
speckit prep --spec hiring/my-backend-role --resume ./candidate.txt --pretty
```
