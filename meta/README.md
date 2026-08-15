# Meta — Agent & RAG navigation

Machine-oriented layer for Cursor agents and external RAG. Human landing still starts at [`../README.md`](../README.md) / [`../QUICK-START.md`](../QUICK-START.md).

**Root entrypoints (do not move):**
- [`../AGENTS.md`](../AGENTS.md) — mandatory agent instructions
- [`../llms.txt`](../llms.txt) — crawler / LLM map

## Contents

| Path | Role |
| --- | --- |
| [`routing.md`](./routing.md) | Topic → canonical docs (human table) |
| [`catalog/`](./catalog/) | `topics.yaml`, frontmatter schema, RAG exclude |
| [`eval/`](./eval/) | Smoke questions + scorecard |
| [`ops/`](./ops/) | Maintenance, difficulty guide, content roadmap, community |
| [`domain-guide-map.md`](./domain-guide-map.md) | Tech (`domains/`) vs Career (`guides/`) overlaps |
| [`retrieval-plan.md`](./retrieval-plan.md) | Hardening plan / status |
| [`../tools/telegram-docs-bot/`](../tools/telegram-docs-bot/) | Telegram Q&A bot (catalog retrieval + LLM) |

## Validate

```bash
python scripts/check_agent_catalog.py
python scripts/check_vn_law_catalog.py
python scripts/check_agent_eval_paths.py
python scripts/smoke_agent_routing.py
python scripts/check_links.py
```

Prefer this `meta/` tree over thin redirects left at some old root paths.
