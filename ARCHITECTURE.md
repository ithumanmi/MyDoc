# 🏗️ Repository Architecture

> **Purpose:** This document explains the organizational philosophy and structure of the Docs repository.
>
> **Last Updated:** August 2026  
> **Scale snapshot:** ~1,800 Markdown files · ~1.2M words · 15 technical domains

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
| **Progressive Disclosure** | README → Quick Start → Deep Dive | Doesn't overwhelm newcomers with ~1.2M words |
| **Discoverability** | README.md in every directory | Users never get lost |
| **Consistency** | kebab-case naming, relative paths | Reduces cognitive load |
| **Maturity transparency** | Stable / Drafting / Stub badges on domain hubs | Prevents false confidence in thin domains |
| **Maintainability** | Automated link checking | Quality assurance at scale |

---

## 📁 2. Directory Structure Deep Dive

### **2.1. `domains/` - Technical Knowledge Base**

**Purpose:** Pure technical skills organized by specialization

**Audience:** Developers learning specific technology stacks

**Content Type:** Roadmaps, tutorials, code concepts, technical references

**Current Domains (15)** — see maturity table in [`domains/README.md`](./domains/README.md):

```
domains/
├── game-dev/            # 🟢 Stable — design, production, programming, labs
├── ai-ml/               # 🟢 Stable — ML, DL, NLP, CV, generative, agents, mlops
├── blockchain/          # 🟢 Stable — contracts, DeFi, MEV, staking, security
├── backend-dev/         # 🟢 Stable — API, DB, architecture, security, labs
├── mmo-engineering/     # 🟢 Stable — anti-detect, automation, platforms
├── network-security/    # 🟢 Stable — foundations → offense/defense + labs
├── mobile-dev/          # 🟡 Drafting — foundations → senior paths
├── business-analytics/  # 🟡 Drafting — metrics, experimentation, trading
├── system-design/       # 🟡 Drafting — interview deep-dives + labs
├── dsa/                 # 🟡 Drafting — patterns + coding challenges
├── web-dev/             # 🟡 Drafting — frontend, fullstack, portfolio
├── iot/                 # 🟡 Drafting — embedded, MQTT, cloud, OTA, labs
├── devops-sre/          # 🟡 Drafting — SLO, K8s, IaC, observability
├── data-science/        # 🟡 Drafting — Spark, lakehouse, quality, Kafka
└── data-analytics/      # 🟡 Drafting — SQL/BI + portfolio projects
```

**Naming:** all domain folders use kebab-case (`iot/`).

**When to Add a New Domain:**

✅ **Add if:**
- Represents a distinct career path (e.g., `devops-sre/` separate from `backend-dev/`)
- Commit to reaching Drafting (≥10 markdown files) within one quarter
- Doesn't heavily overlap with existing domains

❌ **Don't add if:**
- Too narrow (e.g., `react-only/` — put in `web-dev/`)
- Temporary trend without lasting career paths
- Better suited as a guide (e.g., "productivity" is cross-domain)

**Maturity rules (file-count heuristic):**

| Level | `*.md` count | Expectation |
|:---|---:|:---|
| 🟢 Stable | ≥ 50 | Full roadmap; OK as primary learning track |
| 🟡 Drafting | 10–49 | Usable outline; gaps expected |
| 🟠 Stub | ≤ 9 | README-first; contribute or pick a Stable domain |

---

### **2.2. `guides/` - Life Skills & Career Navigation**

**Purpose:** Cross-domain skills, career advice, and personal development

**Audience:** All developers regardless of technical specialization

**Content Type:** Mental models, career strategies, life optimization

**Strategic Pillars (6)** — ~900 Markdown files:

```
guides/
├── 01-mental-models/     # biology, chemistry, engineering, history, math,
│                         # mysticism, philosophy, physics, psychology,
│                         # global-intelligence
├── 02-wealth-business/   # entrepreneurship, finance, investing, legal,
│                         # logistics, market-research, mmo-roadmap
├── 03-career-skills/     # career, growth, productivity, innovation, ielts,
│                         # sales + career tracks: game-dev, mobile-dev,
│                         # web-dev, blockchain, security, data-*
├── 04-lifestyle-os/      # life-os, well-being, politics
├── 05-games-os/          # make / play / earn / follow umbrella
└── 06-vn-law/            # Luật VN: catalog VBQPPL + notes (not legal advice)
```

**Handling Overlaps (e.g., game-dev in both domains/ and guides/):**

This is **intentional** to serve different needs:

| Folder | Focus | Example Content |
|:---|:---|:---|
| `domains/game-dev/` | **HOW to build games** (Technical) | Unity architecture, C# patterns, Shader programming |
| `guides/03-career-skills/game-dev/` | **HOW to earn from games** (Business) | Freelancing rates, Publisher contracts, Monetization |
| `domains/mobile-dev/` | **HOW to build apps** (Technical) | Flutter/React Native, State Management, Local Storage |
| `guides/03-career-skills/mobile-dev/` | **HOW to earn from apps** (Business) | Indie Hacking, AdMob, IAP, ASO |

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

Immediately actionable templates (~33 files):
- `weekly-review.md` - Reflection framework
- `daily-log.md` - Work journal
- `okr-planning.md` - Goal setting (Quarterly)
- `project-post-mortem.md` - Learning from projects
- `cold-email-mentor.md` - Outreach template
- See `templates/TEMPLATES-INDEX.md` for the full catalog

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
- **`answer-templates/`** - Answer sheets for audits

#### **`challenges/` - Deliberate Practice Drills**

Hands-on kata/challenges aligned to domains (~50 files):
- `backend/`, `game-dev/`, `ai-ml/`, `security/`, `devops-sre/`, `web-ui/`, etc.
- Preferred complement when theory in `domains/` outpaces practice volume

---

### **2.5. `personal/` — Life Data Store**

**Purpose:** Record *your* daily life — meals, macros, body metrics, habits, weekly reviews.

**Separation of concerns:**
| | Knowledge | Records |
|:---|:---|:---|
| Folder | `guides/04-lifestyle-os/` | `personal/` |
| Content | Protocols, frameworks | Dates, numbers, meals |

```
personal/
├── daily/YYYY/YYYY-MM-DD.md
├── nutrition/YYYY/YYYY-MM-DD.md
├── body/metrics.csv
├── habits/{definitions,YYYY-MM}.md
├── weekly/YYYY/YYYY-Www.md
├── dashboard.md
└── new-day.ps1
```

Blank forms: `templates/personal/`. Hub: [`personal/README.md`](./personal/README.md).

---

### **2.5b. `data/expenses/` — Financial working data**

**Purpose:** Sao kê ngân hàng, bảng chi tiêu Excel, export Power BI — tách khỏi markdown logs trong `personal/`.

| Layer | Path |
|:---|:---|
| Raw bank exports | `data/expenses/raw/` |
| Working workbooks | `data/expenses/working/` |
| Power BI exports | `data/expenses/powerbi/` |
| Tooling | `scripts/expenses/` |

Hub: [`data/expenses/README.md`](./data/expenses/README.md). Sensitive xlsx/csv under `raw/`, `working/`, `powerbi/` are gitignored.

---

### **2.6. Agent & RAG navigation layer**

Machine-oriented entrypoints so Cursor / external RAG do not random-walk the corpus:

| Artifact | Role |
|:---|:---|
| [`AGENTS.md`](./AGENTS.md) | Read order, answer policy, `personal/` privacy |
| [`meta/routing.md`](./meta/routing.md) | Topic → canonical human table |
| [`llms.txt`](./llms.txt) | Crawler / LLM entrypoints |
| [`meta/catalog/topics.yaml`](./meta/catalog/topics.yaml) | Machine topic index |
| [`meta/catalog/rag-exclude.txt`](./meta/catalog/rag-exclude.txt) | Globs to skip when embedding |
| [`.cursor/rules/docs-agent-navigation.mdc`](./.cursor/rules/docs-agent-navigation.mdc) | Always-on Cursor rule |
| [`meta/eval/questions.md`](./meta/eval/questions.md) | Retrieval smoke tests |
| [`meta/ops/`](./meta/ops/) | Maintenance, difficulty guide, content roadmap |
| [`meta/domain-guide-map.md`](./meta/domain-guide-map.md) | Tech vs career overlap map |
| `python scripts/check_agent_catalog.py` | Validate catalog paths |
| `python scripts/check_links.py` | Internal link audit → `meta/ops/LINK_AUDIT_REPORT.md` |
| [`meta/README.md`](./meta/README.md) | Agent/RAG + ops hub |

Long health deep-dives expose an **Agent SUMMARY** block under the H1 for quick orientation.

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
- [ ] **Link validation:** 100% valid links (automated via `scripts/check_links.py`)
- [ ] **Glossary integration:** Technical terms defined in `GLOSSARY.md`
- [ ] **Difficulty labeling:** Major domain READMEs include difficulty badges (see `meta/ops/DIFFICULTY-GUIDE.md`)
- [ ] **Breadcrumbs present:** Navigation trail at top
- [ ] **README.md exists:** If creating new directory
- [ ] **Proper categorization:** File in correct `domains/` vs `guides/`

### **5.2. Automated Quality Checks**

**Current tools:**
- `scripts/check_links.py` - Validates all markdown links
- Output: `meta/ops/LINK_AUDIT_REPORT.md` with broken link details

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
4. Run `python scripts/check_links.py` locally
5. Update parent README.md if adding new file
6. Clear, descriptive commit messages

---

## 🔮 7. Future Scalability

### **7.1. Expand Existing Stubs First**

Prefer deepening before adding new top-level domains:

1. `devops-sre/` → deepen (multi-env IaC, more runbooks) toward Stable
2. `data-science/` → end-to-end lakehouse project
3. `iot/` → TinyML lab + fleet ACL deep-dive
4. `data-analytics/` → marketing dashboard case + pandas track

**Only after Drafting domains harden — potential new domains:**
- `domains/cloud-infrastructure/` — multi-cloud deep-dives (if not folded into devops-sre)
- `domains/desktop-dev/` — Electron, Tauri, native desktop apps

### **7.2. Scaling Guidelines**

**Current scale already exceeds 1M words. Operating rules:**

✅ **DO:**
- Update maturity badges when file counts cross thresholds
- Prefer challenges/labs over more un-audited theory in Stable domains
- Keep max practical nesting shallow (`domains/<domain>/<area>/<topic>.md`)

❌ **DON'T:**
- Add Stub domains without a fill plan for the quarter
- Duplicate career content into `domains/` (belongs in `guides/`)
- Split repos until a Stable domain alone becomes unnavigable

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
| **Corpus size** | Tracked quarterly | ✅ ~1,800 `.md` · ~1.2M words |
| **Domain inventory** | Hub matches filesystem | ✅ 15 domains listed |
| **Domain maturity** | Stable labels on hub | ✅ See `domains/README.md` |
| **Link Health** | 100% valid | 🟡 Re-run `scripts/check_links.py` monthly |
| **Glossary Coverage** | 80%+ technical terms | ✅ Comprehensive |
| **Navigation Clarity** | All major dirs have README | ✅ Complete |
| **Content Freshness** | Updated quarterly | 🟡 As needed |
| **User Onboarding** | Quick Start exists | ✅ QUICK-START.md |
| **Practice balance** | Challenges grow with domains | 🟡 ~37 challenges vs large theory base |

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
> *Last major revision: August 2026*
