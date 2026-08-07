# Agent eval set — expected retrieval paths

> Use to smoke-test Cursor / RAG: for each question, agent should open **Expected canonical** first.
> Last updated: 2026-08-07

| # | Question (user) | Expected canonical | Acceptable related |
| ---: | --- | --- | --- |
| 1 | Repo này tổ chức thế nào? | `OVERVIEW.md` | `ARCHITECTURE.md`, `AGENTS.md` |
| 2 | Agent nên đọc file nào trước? | `AGENTS.md` | `AGENT-ROUTING.md` |
| 3 | Domain nào Stable? | `domains/README.md` | `domains/INDEX.md` |
| 4 | Làm sao học nhanh mọi thứ? | `.../learning-os-framework.md` | `learning-how-to-learn.md` |
| 5 | Feynman / active recall là gì? | `learning-how-to-learn.md` | `learning-os-framework.md` |
| 6 | Bản đồ hormone ở đâu? | `endocrine-hormone-map.md` | `health-os-overview.md` |
| 7 | Kiểm soát từng hormone thế nào? | `endocrine-control-playbook.md` | hormone map |
| 8 | Cortisol / melatonin? | `cortisol-melatonin-system.md` | playbook, sleep-optimization |
| 9 | Dopamine động lực? | `dopamine-system.md` | neurotransmitters-guide |
| 10 | Insulin / glucose? | `glucose-insulin-system.md` | nutrition-for-brain |
| 11 | Testosterone tối ưu? | `testosterone-system.md` | cortisol-melatonin |
| 12 | Ghi daily/nutrition ở đâu? | `personal/README.md` | `personal/dashboard.md` |
| 13 | System design interview? | `domains/system-design/README.md` | `challenges/system-design/` |
| 14 | Backend roadmap? | `domains/backend-dev/README.md` | challenges/backend |
| 15 | K8s / DevOps lab? | `domains/devops-sre/README.md` | challenges/devops-sre |
| 16 | AI/ML RAG? | `domains/ai-ml/README.md` | challenges/ai-ml |
| 17 | IoT MQTT lab? | `domains/iot/README.md` | challenges/iot |
| 18 | Blockchain escrow practice? | `challenges/blockchain/` | domains/blockchain |
| 19 | Deliberate practice? | `chapters/02-luyen-tap-co-chu-dich.md` | learning-os-framework |
| 20 | Game Unity technical vs career? | tech→`domains/game-dev/`; career→`guides/03-career-skills/game-dev/` | — |
| 21 | Định nghĩa ACID? | `GLOSSARY.md` | backend database docs |
| 22 | Lakehouse ELT project? | `domains/data-science/projects/lakehouse-ecommerce-elt.md` | data-science README |
| 23 | URL shortener design drill? | `challenges/system-design/challenge-design-url-shortener.md` | system-design README |
| 24 | Sleep protocol? | `sleep-optimization.md` | cortisol-melatonin |
| 25 | Không trộn personal metrics vào câu hỏi generic hormone? | Theory from guides; not `personal/body/metrics.csv` unless asked | playbook |

## Pass criteria
- ≥80% questions hit Expected canonical (or Acceptable related) in first 3 tool opens.
- No answer that treats `personal/metrics.csv` as curriculum.

## How to run manually
Ask each question in a fresh agent turn with repo open; score path hits.
