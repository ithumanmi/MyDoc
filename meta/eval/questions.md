# Agent eval set — expected retrieval paths

> Smoke-test Cursor / RAG: agent should open **Expected canonical** first.
> Last updated: 2026-08-07
>
> Static path check: `python scripts/check_agent_eval_paths.py`  
> Manual scoring: copy [`scorecard.md`](./scorecard.md)

| # | Question (user) | Expected canonical | Acceptable related |
| ---: | --- | --- | --- |
| 1 | Repo này tổ chức thế nào? | `OVERVIEW.md` | `ARCHITECTURE.md`, `AGENTS.md` |
| 2 | Agent nên đọc file nào trước? | `AGENTS.md` | `meta/routing.md`, `llms.txt`, `meta/README.md` |
| 3 | Domain nào Stable? | `domains/README.md` | `domains/INDEX.md` |
| 4 | Làm sao học nhanh mọi thứ? | `guides/03-career-skills/productivity/meta-skills/learning-os-framework.md` | `guides/03-career-skills/productivity/meta-skills/learning-how-to-learn.md` |
| 5 | Feynman / active recall là gì? | `guides/03-career-skills/productivity/meta-skills/learning-how-to-learn.md` | `guides/03-career-skills/productivity/meta-skills/learning-os-framework.md` |
| 6 | Bản đồ hormone ở đâu? | `guides/04-lifestyle-os/health/endocrine-hormone-map.md` | `guides/04-lifestyle-os/health/health-os-overview.md` |
| 7 | Kiểm soát từng hormone thế nào? | `guides/04-lifestyle-os/health/endocrine-control-playbook.md` | `guides/04-lifestyle-os/health/endocrine-hormone-map.md` |
| 8 | Cortisol / melatonin? | `guides/04-lifestyle-os/health/cortisol-melatonin-system.md` | `guides/04-lifestyle-os/health/sleep-optimization.md`, `guides/04-lifestyle-os/health/endocrine-control-playbook.md` |
| 9 | Dopamine động lực? | `guides/04-lifestyle-os/health/dopamine-system.md` | `guides/04-lifestyle-os/health/neurotransmitters-guide.md` |
| 10 | Insulin / glucose? | `guides/04-lifestyle-os/health/glucose-insulin-system.md` | `guides/04-lifestyle-os/health/nutrition-for-brain.md` |
| 11 | Testosterone tối ưu? | `guides/04-lifestyle-os/health/testosterone-system.md` | `guides/04-lifestyle-os/health/cortisol-melatonin-system.md` |
| 12 | Ghi daily/nutrition ở đâu? | `personal/README.md` | `personal/dashboard.md` |
| 13 | System design interview? | `domains/system-design/README.md` | `challenges/system-design/README.md`, `domains/backend-dev/system-design-guide.md` |
| 14 | Backend roadmap? | `domains/backend-dev/README.md` | `challenges/backend/README.md` |
| 15 | K8s / DevOps lab? | `domains/devops-sre/README.md` | `challenges/devops-sre/README.md` |
| 16 | AI/ML RAG? | `domains/ai-ml/README.md` | `challenges/ai-ml/README.md` |
| 17 | IoT MQTT lab? | `domains/iot/README.md` | `challenges/iot/README.md` |
| 18 | Blockchain escrow practice? | `challenges/blockchain/challenge-solidity-escrow.md` | `challenges/blockchain/README.md`, `domains/blockchain/README.md` |
| 19 | Deliberate practice? | `chapters/02-luyen-tap-co-chu-dich.md` | `guides/03-career-skills/productivity/meta-skills/learning-os-framework.md` |
| 20 | Game Unity technical vs career? | `domains/game-dev/README.md` | `guides/03-career-skills/game-dev/README.md` |
| 21 | Định nghĩa ACID? | `GLOSSARY.md` | `domains/backend-dev/database-fundamentals.md` |
| 22 | Lakehouse ELT project? | `domains/data-science/projects/lakehouse-ecommerce-elt.md` | `domains/data-science/README.md` |
| 23 | URL shortener design drill? | `challenges/system-design/challenge-design-url-shortener.md` | `domains/system-design/README.md` |
| 24 | Sleep protocol? | `guides/04-lifestyle-os/health/sleep-optimization.md` | `guides/04-lifestyle-os/health/cortisol-melatonin-system.md` |
| 25 | Hormone overview (generic) — không đọc metrics cá nhân | `guides/04-lifestyle-os/health/endocrine-hormone-map.md` | `guides/04-lifestyle-os/health/endocrine-control-playbook.md` |
| 26 | full-pack / phân tích game đủ models nằm đâu? | `domains/game-dev/analyses/README.md` | `domains/game-dev/game-design/templates/game-analysis-pack-readme.md`, `domains/game-dev/analyses/honkai-star-rail/README.md` |
| 27 | Systems teardown template / Infect Them All style essay? | `domains/game-dev/game-design/templates/game-systems-teardown.md` | `domains/game-dev/analyses/README.md`, `.cursor/skills/game-systems-teardown/SKILL.md` |

## Pass criteria
- ≥80% hit Expected canonical **or** Acceptable related in first 3 tool opens (scale with row count; currently 27 → ≥22).
- Q25 must **not** open `personal/body/metrics.csv` unless user asked for personal logs.
- Q26 must land in `analyses/` (not Games OS Play).

## How to run
1. `python scripts/check_agent_eval_paths.py` — verify all expected paths exist.
2. `python scripts/smoke_agent_routing.py` — routing/catalog coverage → fills [`scorecard.md`](./scorecard.md).
3. (Optional) Ask each question in a fresh Cursor agent turn; override scorecard if live behavior differs.
