# 🔧 Repository Maintenance Guide

> **Purpose:** Guidelines for keeping the MyDoc repository fresh, accurate, and up-to-date.

> **Last Updated:** February 2026

---

## 📅 Quarterly Content Review Process

### **Overview**

To maintain content quality and relevance, we perform quarterly reviews (every 3 months) to:
- Update outdated information
- Refresh "Last Updated" dates
- Verify external links still work
- Remove deprecated content
- Add new industry trends

---

## 🗓️ Quarterly Review Schedule

| Quarter | Months | Review Period | Focus Areas |
|:---|:---|:---|:---|
| **Q1** | Jan-Mar | Late March | AI/ML, Backend (new frameworks) |
| **Q2** | Apr-Jun | Late June | Mobile, Web (new libraries) |
| **Q3** | Jul-Sep | Late September | Security, Blockchain (threats/updates) |
| **Q4** | Oct-Dec | Late December | Game Dev, Data Analytics (tools) |

---

## ✅ Review Checklist (Per Domain)

When reviewing a domain README (e.g., `domains/ai-ml/README.md`):

### **1. Content Accuracy Check**
- [ ] **Tech stack versions:** Are frameworks/libraries still current?
  - Example: Check if "PyTorch 2.0" is outdated → Update to "PyTorch 2.5"
- [ ] **Tool recommendations:** Are suggested tools still industry standard?
  - Example: Replace deprecated tools with modern alternatives
- [ ] **Salary ranges:** Update based on market research (quarterly trend)
- [ ] **Job market reality:** Update "Cơ hội việc làm" ratings if market shifts
- [ ] **Meta header consistency:** Each domain README must include breadcrumb, Difficulty, Prerequisites, Time to Master, Knowledge Audit, Glossary link, and **Curated Links** pointing to `resources/collected_links/<domain>.md`.

### **2. Link Health**
- [ ] Run `python check_links.py` to verify all internal/external links
- [ ] Fix any broken links (especially external resources)
- [ ] Remove dead project/tool links, add alternatives

### **3. Completeness**
- [ ] Check for "Coming soon" sections older than 6 months
  - Either complete them or remove if no longer relevant
- [ ] Add new industry trends/technologies if applicable
  - Example: New AI frameworks, security vulnerabilities, game engines

### **4. Update "Last Updated" Date**
- [ ] If ANY content was modified → Update the date at bottom:
  ```markdown
  > **Last Updated:** [Current Month] 2026
  ```
- [ ] If NO changes needed → Keep existing date (shows stability)

---

## 📝 Files Requiring Regular Updates

### **High Priority (Update Quarterly)**

These files contain time-sensitive information:

| File | Why Update? | Last Review |
|:---|:---|:---:|
| `domains/ai-ml/README.md` | Fast-moving field (new models/frameworks) | Mar 2026 |
| `domains/backend-dev/README.md` | Framework versions, cloud services | Mar 2026 |
| `domains/blockchain/README.md` | Market volatility, new protocols | Feb 2026 |
| `domains/network-security/README.md` | New vulnerabilities, security tools | Feb 2026 |
| `guides/03-career-skills/career/*.md` | Salary trends, market conditions | Feb 2026 |
| `guides/02-wealth-business/finance/*.md` | Economic cycles, monetary policy | Feb 2026 |

### **Medium Priority (Update Bi-Annually)**

Stable content, but needs occasional refresh:

| File | Why Update? | Last Review |
| File | Why Update? | Last Review |
|:---|:---|:---:|
| `domains/data-analytics/README.md` | BI tool updates, SQL standards | Feb 2026 |
| `guides/03-career-skills/growth/*.md` | New personal development research | Feb 2026 |
| `guides/02-wealth-business/entrepreneurship/*.md` | Startup trends, funding landscape | Feb 2026 |

### **Low Priority (Annual Review)**

Foundational content that rarely changes:

| File | Why Update? | Last Review |
|:---|:---|:---:|
| `chapters/*.md` | Core principles remain stable | Feb 2026 |
| `templates/*.md` | Templates are evergreen | Feb 2026 |
| `ARCHITECTURE.md` | Only update if structure changes | Feb 2026 |

---

## 🤖 Automated Maintenance Tools

### **1. Link Checker (Already Available)**

**Script:** `check_links.py`

**Usage:**
```bash
cd c:\Projects\Docs
python check_links.py
```

**Output:** `LINK_AUDIT_REPORT.md` with broken link details

**Frequency:** Run monthly or before major commits

---

## 2. Last Updated Date Checker (New Script)

**Script:** `check_dates.py` (see below for implementation)

**Purpose:** Find files with "Last Updated" dates older than 3 months

**Usage:**
```bash
cd c:\Projects\Docs
python check_dates.py
```

**Expected Output:**
```
🔍 Checking "Last Updated" dates...
============================================================
⚠️ FILES NEEDING REVIEW (>3 months old):

domains/ai-ml/README.md
  Last Updated: November 2025 (4 months ago)
  
domains/backend-dev/README.md
  Last Updated: October 2025 (5 months ago)

============================================================
✅ FRESH FILES (≤3 months old): 15
⚠️ NEEDS REVIEW: 2
```

---

## 🔄 Monthly Maintenance Routine

**Time Required:** ~30 minutes

### **Week 1 of Each Month:**

1. **Run link checker:**
   ```bash
   python check_links.py
   ```
   - Fix any broken links
   - Update `LINK_AUDIT_REPORT.md`

2. **Check GitHub Issues:**
   - Review community feedback
   - Prioritize content requests

3. **Monitor industry news:**
   - Subscribe to tech newsletters (e.g., TLDR, ByteByteGo)
   - Note major framework releases or security alerts

---

## 📊 Quarterly Deep Review (Every 3 Months)

**Time Required:** ~4 hours per quarter

### **Phase 1: Data Collection (30 min)**
- [ ] Run `python check_dates.py` to find outdated content
- [ ] Gather industry news from last 3 months
- [ ] Check job boards (VietnamWorks, TopCV) for salary trends

### **Phase 2: Content Updates (2 hours)**
- [ ] Review 2-3 priority domains from schedule
- [ ] Update tech stack versions
- [ ] Refresh salary ranges if market shifted
- [ ] Add new tools/frameworks if they gained traction

### **Phase 3: Link Maintenance (30 min)**
- [ ] Run link checker
- [ ] Replace dead links
- [ ] Add new high-quality resources

### **Phase 4: Documentation (30 min)**
- [ ] Update "Last Updated" dates on modified files
- [ ] Document changes in `CHANGELOG.md` (optional)
- [ ] Commit with clear message:
  ```
  feat: Q1 2026 content refresh - AI/ML domain
  
  - Updated PyTorch to v2.5
  - Added new RAG techniques
  - Refreshed salary data
  - Fixed 3 broken links
  ```

### **Phase 5: Quality Check (30 min)**
- [ ] Final link check: `python check_links.py`
- [ ] Read through changes for consistency
- [ ] Verify all dates updated

---

## 🚨 Emergency Updates (Ad-hoc)

Some events require immediate updates outside the quarterly cycle:

### **Triggers for Emergency Updates:**

1. **Major Framework Release:**
   - Example: Unity 6 LTS released → Update `domains/game-dev/`
   - Timeline: Within 2 weeks of release

2. **Critical Security Vulnerability:**
   - Example: New OWASP Top 10 published → Update `domains/network-security/`
   - Timeline: Within 1 week

3. **Market Disruption:**
   - Example: Major company layoffs affecting job market
   - Timeline: Within 1 month

4. **Broken Links Reported:**
   - User reports dead link via GitHub Issue
   - Timeline: Within 3 days

---

## 📜 Change Log Template

When making significant updates, document in commit message:

```markdown
## Q1 2026 Content Review (March 2026)

### Updated Domains:
- **AI/ML:** Added LangGraph framework, updated LLM pricing
- **Backend:** Node.js 22 LTS released, added Bun runtime

### Link Maintenance:
- Fixed 5 broken external links
- Replaced deprecated tool: Heroku → Railway

### Salary Updates:
- Backend Senior: $3k-$8k → $3.5k-$9k (market increase)
- AI/ML Junior: $1k-$2k → $1.2k-$2.5k (demand surge)

### Removed:
- "Coming soon" sections older than 6 months
```

---

## 🎯 Success Metrics

Track these metrics to measure maintenance quality:

| Metric | Target | Current |
|:---|:---:|:---:|
| **Link Health** | 100% valid | ✅ 242/242 (100%) |
| **Content Freshness** | 80%+ ≤3 months old | 🟡 To be measured |
| **Community Feedback** | <7 days response time | ⏳ N/A yet |
| **Completeness** | <10 "Coming soon" sections | ✅ 8 sections |

---

## 👥 Maintenance Responsibilities

### **If Solo Maintainer:**
- Follow quarterly schedule strictly
- Use reminder tool (Google Calendar, Notion)
- Allocate 1 day per quarter for deep review

### **If Team of Contributors:**
- **Assign domain owners:**
  - AI/ML: @contributor1
  - Backend: @contributor2
  - Security: @contributor3
- Each owner reviews their domain quarterly
- Coordinate via GitHub Projects/Issues

---

## 🔧 Automation Ideas (Future)

### **Potential Automations:**

1. **GitHub Action: Link Checker**
   - Auto-run `check_links.py` on every commit
   - Fail PR if broken links detected

2. **GitHub Action: Date Reminder**
   - Weekly check for files >3 months old
   - Auto-create GitHub Issue with list

3. **External Link Monitoring:**
   - Use service like `linkchecker.github.io`
   - Email alert when external link dies

4. **Salary Data API:**
   - Scrape VietnamWorks/TopCV quarterly
   - Auto-suggest salary range updates

---

## 📞 Questions?

- **Where to report outdated content?** Open a GitHub Issue with label `content-refresh`
- **How to contribute updates?** See [CONTRIBUTING.md](./CONTRIBUTING.md)
- **Who maintains this?** Check [CONTRIBUTORS.md](./CONTRIBUTORS.md) (if exists)

---

> **Remember:** Fresh content = Trustworthy content. Users rely on accurate, up-to-date information for career decisions!

> *Last major revision: February 2026*
