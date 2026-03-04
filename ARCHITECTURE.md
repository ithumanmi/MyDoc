# 🏗️ Repository Architecture

> **Purpose:** This document explains the organizational philosophy and structure of the MyDoc repository.
>
| **Last Updated:** March 2026

---

## 📐 1. Philosophy & Design Principles

### **1.1. Information Architecture Goals**

This repository follows a **hybrid navigation model**:

1. **Sequential (Linear):** `chapters/` provides a structured 1→10 learning path
2. **Categorical (Hierarchical):** `domains/` and `guides/` allow direct access by topic
3. **Associative (Network):** Cross-references and breadcrumbs enable exploration

**Why this matters:** Different users have different entry points:
- **Beginners** need linear guidance → Start with `chapters/`
- **Specialists** need deep-dives → Jump to specific `domains/`
- **Career-focused** need soft skills → Explore `guides/`

### **1.2. Core Design Principles**

| Principle | Implementation | Rationale |
|:---|:---|:---|
| **Separation of Concerns** | `domains/` (technical) vs `guides/` (career/life) | Prevents mixing "how to code Unity" with "how to negotiate salary" |
| **Progressive Disclosure** | README → Quick Start → Deep Dive | Doesn't overwhelm newcomers with 108k+ words |
| **Discoverability** | README.md in every directory | Users never get lost |
| **Consistency** | kebab-case naming, relative paths | Reduces cognitive load |
| **Maintainability** | Automated link checking | Quality assurance at scale |

---

## 📁 2. Directory Structure Deep Dive

### **2.1. `domains/` - Technical Knowledge Base**

**Purpose:** Pure technical skills organized by specialization

**Audience:** Developers learning specific technology stacks

**Content Type:** Roadmaps, tutorials, code concepts, technical references

**Current Domains (8):**

```
domains/
├── ai-ml/              # Artificial Intelligence & Machine Learning
│   ├── fundamentals/   # ML basics, statistics, linear algebra
│   ├── machine-learning/ # Supervised/unsupervised learning
│   ├── deep-learning/  # Neural networks, CNNs, RNNs
│   ├── nlp/            # Natural Language Processing, Transformers
│   ├── computer-vision/ # Image processing, object detection
│   ├── generative-ai/  # GANs, Diffusion models, LLMs
│   ├── mlops/          # Deployment, monitoring, pipelines
│   └── agents/         # AI agents, AutoGPT concepts
│
├── mobile-dev/         # Mobile App Development (iOS/Android)
│   └── README.md       # Flutter, React Native, Swift, Kotlin
│
├── backend-dev/        # Backend Engineering
│   ├── api-design/     # REST, GraphQL, gRPC
│   ├── database/       # SQL, NoSQL, caching
│   ├── system-design/  # Scalability, microservices
│   ├── devops-sre/     # CI/CD, Docker, Kubernetes
│   ├── security/       # Auth, encryption, OWASP
│   └── testing/        # Unit, integration, E2E tests
│
├── blockchain/         # Blockchain & Web3
│   ├── fundamentals/   # How blockchain works
│   ├── development/    # Smart contracts (Solidity)
│   ├── defi/           # Decentralized Finance
│   ├── nft-gamefi/     # NFTs and GameFi
│   └── security/       # Smart contract security
│
├── data-analytics/     # Data Analysis & Visualization
│   ├── sql-mastery.md
│   ├── data-visualization-mastery.md
│   └── projects/       # Hands-on projects
│
├── game-dev/           # Game Development (Unity focus)
│   ├── ai/             # Game AI (FSM, Behavior Trees)
│   ├── graphics/       # Shaders, VFX, lighting
│   ├── engines/        # Unity, Unreal Engine
│   ├── pcg/            # Procedural generation
│   └── unity-deep-dive/ # Advanced Unity patterns
│
├── network-security/   # Cybersecurity & Network Defense
│   ├── deep-dive/      # Advanced security topics
│   ├── labs/           # Hands-on practice labs
│   └── mmo-engineering/ # Massive multiplayer security
│
└── web-dev/            # Web Development
    └── README.md       # Frontend, backend, fullstack
```

**When to Add a New Domain:**

✅ **Add if:**
- Represents a distinct career path (e.g., `devops/` separate from `backend-dev/`)
- Has sufficient content (5+ markdown files)
- Doesn't heavily overlap with existing domains

❌ **Don't add if:**
- Too narrow (e.g., `react-only/` - put in `web-dev/`)
- Temporary trend without lasting career paths
- Better suited as a guide (e.g., "productivity" is cross-domain)

---

### **2.2. `guides/` - Life Skills & Career Navigation**

**Purpose:** Cross-domain skills, career advice, and personal development

**Audience:** All developers regardless of technical specialization

**Content Type:** Mental models, career strategies, life optimization

**Strategic Pillars (4):**

```
guides/
├── career/             # Career progression, remote work, salary negotiation
│   ├── app-monetization-guide.md
│   ├── remote-backend-guide.md
│   └── templates/      # Resume, cover letter templates
│
├── entrepreneurship/   # Building businesses
│   ├── mindset/        # Founder psychology
│   ├── operations/     # Finance, HR, legal
│   ├── growth/         # Marketing, sales
│   ├── tech-startup/   # SaaS, MVPs, fundraising
│   └── solopreneur/    # Solo founder strategies
│
├── finance/            # Macroeconomics, money systems
│   ├── monetary-system.md
│   └── economic-cycles.md
│
├── investing/          # Personal wealth building
│   ├── fundamentals/   # Stocks, real estate, bonds
│   ├── advanced/       # Options, behavioral economics
│   └── strategy/       # Portfolio construction
│
├── game-dev/           # Game dev CAREER (not technical)
│   ├── game-dev-10k-roadmap.md  # How to earn $10k/month
│   ├── publisher-roadmap.md     # Becoming a publisher
│   └── publisher-contract-template.md
│
├── growth/             # Personal development
│   ├── becoming-top-1-percent.md
│   ├── anti-slip-system.md
│   ├── life-os-framework.md
│   └── resilience-antifragility.md
│
├── productivity/       # Time management, deep work
│   ├── core-skills/    # Focus, note-taking
│   ├── career-growth/  # Promotion, networking
│   └── side-hustle/    # Freelancing, passive income
│
├── well-being/         # Health optimization
│   ├── biohacking/     # Sleep, nutrition, supplements
│   ├── mental-resilience/ # Stoicism, stress management
│   └── longevity/      # Long-term health strategies
│
├── global-intelligence/ # Understanding the world
│   ├── trusted-sources.md
│   ├── critical-thinking/  # Avoiding biases
│   ├── geopolitics-macro/  # Global trends
│   └── systems-thinking/   # Complex system analysis
│
├── ielts/              # English proficiency
│   ├── roadmap-7.5.md
│   ├── speaking-mastery.md
│   └── writing-mastery.md
│
├── innovation/         # Creative problem-solving
│   ├── design-thinking.md
│   ├── brainstorming.md
│   └── business-model-canvas.md
│
├── mmo-roadmap/        # Making money online
├── philosophy/         # Mental models, ethics
├── psychology/         # Human behavior understanding
├── legal/              # Legal basics for tech workers
└── market-research/    # Finding product-market fit
```

**Handling Overlaps (e.g., game-dev in both domains/ and guides/):**

This is **intentional** to serve different needs:

| Folder | Focus | Example Content |
|:---|:---|:---|
| `domains/game-dev/` | **HOW to build games** (Technical) | Unity architecture, C# patterns, Shader programming |
| `guides/game-dev/` | **HOW to earn from games** (Business) | Freelancing rates, Publisher contracts, Monetization |
| `domains/mobile-dev/` | **HOW to build apps** (Technical) | Flutter/React Native, State Management, Local Storage |
| `guides/mobile-dev/` | **HOW to earn from apps** (Business) | Indie Hacking, AdMob, IAP, ASO |

**Navigation notes** in both READMEs clarify this boundary.

---

### **2.3. `chapters/` - Sequential Learning Framework**

**Purpose:** A 10-chapter linear progression path for beginners

**Audience:** New developers who need structured guidance

**Content Type:** Framework, mindset, actionable exercises

**Structure:**

```
chapters/
├── 01-xac-dinh-linh-vuc.md        # Choosing your domain
├── 02-luyen-tap-co-chu-dich.md    # Deliberate practice
├── 03-hoc-hoi-mentor.md           # Finding mentors
├── 04-do-luong-phan-hoi.md        # Feedback loops
├── 05-ky-luat-thoi-quen.md        # Habits & discipline
├── 06-quan-ly-thoi-gian.md        # Time management
├── 07-networking.md                # Building relationships
├── 08-personal-brand.md            # Online presence
├── 09-systems-thinking.md          # Thinking in systems
└── 10-action-plan.md               # Putting it all together
```

**Progression Logic:**
1. **Chapters 1-3:** Foundation (What, How, Who)
2. **Chapters 4-6:** Execution (Measure, Habit, Time)
3. **Chapters 7-9:** Scale (Network, Brand, Systems)
4. **Chapter 10:** Integration (Action plan)

---

### **2.4. Supporting Directories**

#### **`templates/` - Ready-to-Use Tools**

Immediately actionable templates:
- `weekly-review.md` - Reflection framework
- `daily-log.md` - Work journal
- `okr-planning.md` - Goal setting (Quarterly)
- `project-post-mortem.md` - Learning from projects
- `cold-email-mentor.md` - Outreach template

#### **`resources/` - Curated External Links**

High-quality external resources:
- `books.md` - Must-read books
- `tools.md` - Productivity apps
- `podcasts-channels.md` - Learning content
- `communities.md` - Online communities
- **`collected_links/`** - Domain-specific curated links
  - `ai-development.md`, `backend-dev.md`, `security-dev.md`, etc.

#### **`case-studies/` - Real-World Analysis**

Success/failure case studies categorized by type:
- **`knowledge-audits/`** - Skills & depth self-assessments
- **`mental-models-analysis/`** - Multidisciplinary breakdowns (Physics, Biology, etc.)
- **`stories/`** - Profiles of leaders and companies
- **`templates/`** - Answer sheets for audits

---

## 📝 3. File Naming Conventions

### **3.1. Naming Rules**

| Element | Convention | Example |
|:---|:---|:---|
| **Files** | kebab-case | `behavioral-economics.md` |
| **Folders** | kebab-case | `network-security/` |
| **Index files** | README.md (capital) | `domains/game-dev/README.md` |
| **Language** | English filenames, Vietnamese content OK | `game-dev-roadmap.md` (file) with Vietnamese inside |

### **3.2. Special Files**

- **README.md** - Navigation hub (every major directory should have one)
- **INDEX.md** - Optional content table (e.g., `guides/INDEX.md`)
- **.md extension** - All content files are Markdown

---

## 🔗 4. Content Cross-Referencing Strategy

### **4.1. Linking Best Practices**

✅ **DO:**
- Use **relative paths**: `../../domains/ai-ml/README.md`
- Add **breadcrumbs** at top: `> [← Back to X](../Y.md) | [Home](../../README.md)`
- Create **bi-directional links** when appropriate
- Link to **specific sections**: `#2-core-concepts`

❌ **DON'T:**
- Use absolute paths (`/domains/...`) - breaks on different git hosting
- Create circular dependencies
- Link to external sites without context
- Forget to update links when moving files

### **4.2. Navigation Patterns**

**Pattern 1: Hub-and-Spoke**
- `README.md` = Hub
- Individual guides = Spokes
- Example: `guides/README.md` links to all sub-guides

**Pattern 2: Breadcrumb Trail**
```markdown
> [← Back to Guides](../README.md) | [Home](../../README.md) | [Quick Start](../../QUICK-START.md)
```

**Pattern 3: Cross-Domain References**
```markdown
> 📍 For technical Unity skills, see [domains/game-dev/](../../domains/game-dev/)
```

---

## ✅ 5. Quality Standards

### **5.1. Content Quality Gates**

Before merging new content:
- [ ] **Link validation:** 100% valid links (automated via `check_links.py`)
- [ ] **Glossary integration:** Technical terms defined in `GLOSSARY.md`
- [ ] **Difficulty labeling:** Major domain READMEs include difficulty badges (see `DIFFICULTY-GUIDE.md`)
- [ ] **Breadcrumbs present:** Navigation trail at top
- [ ] **README.md exists:** If creating new directory
- [ ] **Proper categorization:** File in correct `domains/` vs `guides/`

### **5.2. Automated Quality Checks**

**Current tools:**
- `check_links.py` - Validates all markdown links
- Output: `LINK_AUDIT_REPORT.md` with broken link details

**Future considerations:**
- Spell checker
- Markdown linter (prettier, markdownlint)
- Automated ToC generation

---

## 📐 6. Contribution Guidelines

### **6.1. Where to Add New Content?**

**Decision Tree:**

```
Is it technical HOW-TO content?
├─ YES → Add to domains/
│  └─ Which domain? (ai-ml, backend, mobile, etc.)
│
└─ NO → Is it career/business advice?
   ├─ YES → Add to guides/
   │  └─ Which pillar? (01-mental-models, 02-wealth-business, 03-career-skills, 04-lifestyle-os)
   │
   └─ NO → Is it a template/tool?
      ├─ YES → Add to templates/
      └─ NO → Is it external resource curation?
         └─ YES → Add to resources/
```

### **6.2. Pull Request Checklist**

When contributing:
1. Read **[CONTRIBUTING.md](./CONTRIBUTING.md)** first
2. Follow naming conventions (kebab-case)
3. Add breadcrumbs to your markdown file
4. Run `python check_links.py` locally
5. Update parent README.md if adding new file
6. Clear, descriptive commit messages

---

## 🔮 7. Future Scalability

### **7.1. Potential Domain Additions**

**High Priority (when content ready):**
- `domains/cloud-infrastructure/` - AWS, Azure, GCP deep-dives
- `domains/devops/` - Separate from backend-dev (Terraform, K8s, monitoring)

**Medium Priority:**
- `domains/embedded-systems/` - IoT, Arduino, embedded C++
- `domains/desktop-dev/` - Electron, Tauri, native desktop apps

**Low Priority:**
- `domains/ar-vr/` - Augmented/Virtual Reality (niche but growing)

### **7.2. Scaling Guidelines**

**When repository grows to 200k+ words:**

✅ **DO:**
- Consider splitting large domains into separate repos (e.g., ai-ml → own repo)
- Add tags/labels for content difficulty (Beginner/Intermediate/Advanced)
- Create learning path flowcharts

❌ **DON'T:**
- Split too early (overhead management cost)
- Create too many nested levels (max 3 deep: `domains/ai-ml/nlp/transformers.md`)
- Duplicate content across multiple locations

### **7.3. Archive Strategy**

For outdated content:
- Create `_archive/` folder (prefix `_` to hide from main navigation)
- Move deprecated content there with notes on why
- Link to updated versions if applicable

---

## 📊 8. Metrics & Success Criteria

### **8.1. Repository Health Indicators**

| Metric | Target | Current Status |
|:---|:---:|:---|
| **Link Health** | 100% valid | ✅ 242/242 valid |
| **Glossary Coverage** | 80%+ technical terms | ✅ Comprehensive |
| **Navigation Clarity** | All dirs have README | ✅ Complete |
| **Content Freshness** | Updated quarterly | 🟡 As needed |
| **User Onboarding** | Quick Start exists | ✅ QUICK-START.md |

### **8.2. User Success Metrics** (Future)

If tracking usage:
- Time to first valuable content (< 2 minutes via Quick Start)
- Bounce rate on README (should be low - users find path forward)
- Most accessed domains (indicates user interests)

---

## 🤝 9. Philosophy Recap

This repository architecture is designed around **three core user journeys**:

1. **The Explorer** → Browses `README.md` → Finds interesting domain → Deep-dives
2. **The Structured Learner** → Starts `QUICK-START.md` → Follows `chapters/` 1-10
3. **The Specialist** → Directly navigates to `domains/X/` via search/link

**All three journeys are valid and supported.**

---

## 📞 Questions or Suggestions?

- Open an issue on GitHub
- See **[CONTRIBUTING.md](./CONTRIBUTING.md)** for contribution process
- Check **[README.md](./README.md)** for general navigation

---

> **Remember:** Architecture should serve users, not constrain them. If this structure stops working, we evolve it. This is a living document.
>
> *Last major revision: February 2026*
