# AGENTS.md — Instructions for AI coding / research agents

You are operating in the **Docs** repository: a hybrid **knowledge library** + **personal life-data store**.

## 0. Read order (always)

1. This file (`AGENTS.md`)
2. [`OVERVIEW.md`](./OVERVIEW.md) — architecture map
3. [`AGENT-ROUTING.md`](./AGENT-ROUTING.md) — topic → canonical paths
4. Hub README for the relevant area (`domains/README.md`, `guides/…`, `personal/README.md`)
5. Canonical deep-dive / challenge — **cite paths in answers**

Do **not** start by grepping random long files unless routing fails.

## 1. Corpus map

| Path | Role | Agent priority |
| --- | --- | --- |
| `domains/` | Technical curricula (15 domains) | High for tech Qs |
| `guides/` | Career, wealth, mental models, lifestyle **theory** | High for soft/life theory |
| `personal/` | **User’s private records** (meals, sleep, habits) | Only when asked about *their* logs |
| `challenges/` | Practice drills | After theory, for “how do I practice” |
| `templates/` | Blank forms | When scaffolding |
| `chapters/` | Linear beginner path | Beginner onboarding |
| `case-studies/` | Audits & stories | Self-test / examples |
| `resources/` | External links + PDFs | Low; prefer md guides first |
| `catalog/` | Machine-oriented topic index | High for routing |
| `AGENT-ROUTING.md` | Human-readable routing | High |

Maturity of domains: see [`domains/README.md`](./domains/README.md) (Stable / Drafting). Prefer Stable unless user asks for a Drafting domain.

## 2. Answer policy

- **Cite** markdown paths (and section headings when helpful).
- Prefer **canonical** docs marked in `AGENT-ROUTING.md` / `catalog/topics.yaml`.
- If sources conflict, prefer: `*-map.md` / README hub → playbook/checklist → deep-dive → older duplicate.
- **Do not invent** lab values, medical advice as diagnosis, or “facts” not in repo. Lifestyle docs are educational; escalate to “see a doctor” when symptoms are clinical.
- For overlapping topics (e.g. game-dev tech vs career):  
  - *How to build* → `domains/`  
  - *How to earn / career* → `guides/03-career-skills/`
- Learning-method questions → [`guides/03-career-skills/productivity/meta-skills/learning-os-framework.md`](./guides/03-career-skills/productivity/meta-skills/learning-os-framework.md)
- Hormone control → map then playbook:  
  [`endocrine-hormone-map.md`](./guides/04-lifestyle-os/well-being/biohacking/endocrine-hormone-map.md) →  
  [`endocrine-control-playbook.md`](./guides/04-lifestyle-os/well-being/biohacking/endocrine-control-playbook.md)

## 3. `personal/` rules

- Treat as **sensitive life data**.
- Do not summarize or expose personal metrics unless the user explicitly asks.
- Do not mix personal CSV rows into general advice answers.
- When improving life systems, link theory in `guides/04-lifestyle-os/` and record location in `personal/`.

## 4. Long files

Deep-dives may exceed 500–800 lines. Use the **Agent SUMMARY** block at the top when present; then jump to needed `##` sections. Do not dump entire files into the answer.

## 5. Editing conventions

- Keep kebab-case paths; English filenames OK with Vietnamese body.
- Update routing (`AGENT-ROUTING.md` + `catalog/topics.yaml`) when adding a **canonical** topic doc.
- New domains: update `domains/README.md` maturity table.
- Prefer relative links; breadcrumbs on new pages.
- Frontmatter schema: [`catalog/FRONTMATTER.md`](./catalog/FRONTMATTER.md)

## 6. Retrieval / RAG notes

- Entry for crawlers: [`llms.txt`](./llms.txt)
- Topic machine index: [`catalog/topics.yaml`](./catalog/topics.yaml)
- Exclude patterns: [`catalog/rag-exclude.txt`](./catalog/rag-exclude.txt)
- Eval questions: [`agent-eval/questions.md`](./agent-eval/questions.md)
- Validate topic paths: `python scripts/check_agent_catalog.py`

## 7. Anti-patterns

- Answering from `guides/INDEX.md` alone if it may be stale — verify filesystem / hub README.
- Preferring PDF under `resources/Tech/` over markdown guides.
- Treating marketing tone in READMEs as procedural truth without checking linked modules.
