---
title: "Game Design Module"
description: "Lý thuyết core loop, economy, narrative và playtest framework cho indie/game studio."
tags:
  - game-design
  - gameplay
updated: 2026-03-11
---

# 🧩 Game Design Module

## 🧠 1. Core Game Design (Hệ thống Cốt lõi)

*   **[Core Loop Mastery](./core-loop-mastery.md):** Thiết kế vòng lặp vỡ lòng (Core Loop) giữ chân người chơi.
*   **[Advanced Core Loops & Meta-Game ✨](./advanced-core-loops.md):** Đi sâu vào khung thiết kế 3 C's, Xung đột hệ thống và móc nối Meta-Game (Case Study: Hades, Genshin).
*   **[Level Design Flow ✨](./level-design-flow.md):** Áp dụng tâm lý học (Tension & Release), Kỹ thuật dẫn đường (Breadcrumbing) vào màn chơi.
*   **[Mechanics & Economy](./economy-systems.md):** Xây dựng hệ thống tiền tệ, vòi hút/xả (sources/sinks) cân bằng trong game.
*   **[Game Economics & Monetization](./game-economics-monetization.md):** Lập mô hình Excel chống lạm phát, phân tích Gacha Pity System.
| [narrative-toolkit.md](./narrative-toolkit.md) | Story bible, quest arc, branching | Dự án story-driven hoặc hybrid casual có lore |
| [playtest-framework.md](./playtest-framework.md) | Quy trình playtest, survey, telemetry | Trước milestone alpha/beta |
| [game-review-checklist.md](./game-review-checklist.md) | Checklist review build 9 hạng mục + scoring | Chuẩn bị demo stakeholder, soft-launch |
| [puzzle-first-48h-metrics.md](./puzzle-first-48h-metrics.md) | 7 metric quyết định puzzle game trong 48h đầu | Sau 1.000 installs, quyết định pivot/kill |
| [pixel-flow-engagement.md](./pixel-flow-engagement.md) | Bài học từ Pixel Flow: copy engagement, không copy mechanic | Khi benchmark hybrid casual hit |
| [puzzle-scope-calculator.md](./puzzle-scope-calculator.md) | Công thức tính số level cho D1/D7/D14 build | Lập kế hoạch content trước production |
| [puzzle-hidden-systems.md](./puzzle-hidden-systems.md) | 10 hệ thống vô hình giữ puzzle game sống | Khi audit cảm xúc & retention |
| [game-designer-knowledge.md](./game-designer-knowledge.md) | Kiến thức & lộ trình năng lực Game Designer | Khi chuẩn bị vào nghề hoặc nâng cấp skill |
| [player-psychology.md](./player-psychology.md) | Flow state, SDT, loss aversion | Khi cần map feature → nhu cầu cảm xúc |
| [metagame-design.md](./metagame-design.md) | Progression, collection, social layer | Thiết kế meta giữ retention + monetization |
| [balancing-methodology.md](./balancing-methodology.md) | Excel modeling, Monte Carlo, KPI | Balancing combat/economy có số liệu |
| [live-ops-design.md](./live-ops-design.md) | Event cadence, limited-time content, ethics | Vận hành Live Service/GaaS |
| [genre-deep-dives/](./genre-deep-dives/README.md) | Phân tích roguelike, idle, puzzle... | Khi cần chuẩn hóa pillar theo genre |
| **Design docs kit** ⭐ | Pitch · GDD · Systems/economy · Postmortem · Playtest · **full-pack** | Skill `game-design-docs` |
| **[Analysis packs](../analyses/README.md)** ⭐ | Một folder/game đủ mọi model | `full-pack` khi phân tích title |
| … [pack hub template](./templates/game-analysis-pack-readme.md) | README + status matrix | Scaffold `analyses/<slug>/` |
| … [pitch one-pager](./templates/game-pitch-one-pager.md) | Hook, loop, pillars, scope, ask | Greenlight / align |
| … [GDD](./templates/game-gdd.md) | Thin living bible + systems index | Production handoff |
| … [systems map / economy](./templates/game-systems-map-economy.md) | Currencies, source/sink, gates, KPIs | Balance & monetization model |
| … [postmortem](./templates/game-postmortem.md) | Facts, causes, lessons, actions | Sau milestone / ship |
| … [playtest / review](./templates/game-playtest-review.md) | Protocol, survey, scores, actions | Trước/sau build review |
| **[Systems teardown template](./templates/game-systems-teardown.md)** ⭐ | Essay systems: loop physics, axes, tiers, economy, UX | Trong pack → `systems-teardown.md` |
| **Example pack:** [Triangle Strategy](../analyses/triangle-strategy/) · [Honkai: Star Rail](../analyses/honkai-star-rail/) | Pitch→GDD→Economy→Teardown→Playtest→Postmortem | Mẫu full-pack |
| Legacy HSR teardown path | → redirect vào pack | [case-studies stub](../case-studies/honkai-star-rail-systems-teardown.md) |

**Workflow gợi ý:** *“full-pack cho &lt;game&gt;”* → đọc Pitch + Teardown → port qua GDD/Economy → Playtest → Postmortem.  
**Đọc máy / viết máy:** skill `game-systems-teardown` (essay) nằm trong `full-pack`; skill `game-design-docs` điều phối cả bộ.

> Cross-link: dùng [Unity Impact Metrics](../metrics/unity-impact-metrics.md) để đo KPI được định nghĩa trong các tài liệu game design.