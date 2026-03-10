---
title: "Playtest Framework"
description: "Quy trình playtest định tính/định lượng + telemetry và survey template."
tags:
  - game-design
  - playtest
updated: 2026-03-11
---

# 🧪 Playtest Framework

> Playtest = cảm nhận + số liệu. Cần cả hai để biết core loop thành công.

## 1. Loại Playtest
| Type | Khi nào | Mục tiêu |
| --- | --- | --- |
| Paper/Prototype | Rất sớm | Validate fantasy |
| Alpha internal | Features hợp nhất | Tìm blocker bug, UX issue |
| Closed beta | Người chơi mục tiêu | Đo retention, monetization |

## 2. Pipeline 5 bước
1. Define Goal.
2. Recruit đúng persona.
3. Protocol rõ nhiệm vụ, câu hỏi.
4. Observe & record (video, telemetry).
5. Synthesize insight + action.

## 3. Telemetry Pack
- Events: `LoopStart`, `LoopFail`, `CurrencySpent`, `DialogueChoice`, `SessionEnd`.
- Metrics: Avg session length, fail reason distribution, economy delta.
- Dashboard: [Unity Impact Metrics](../metrics/unity-impact-metrics.md).

## 4. Survey Template
- Hiểu mục tiêu level? (1-5)
- Muốn tiếp tục chơi sau 10 phút? (1-5)
- Economy công bằng? (1-5)
- Open-ended: Khoảnh khắc nhớ nhất?

## 5. Insight Board
- Tag theo lĩnh vực (Loop/Economy/Narrative/UX).
- Severity + owner + due date.
- Highlight reel video cho team.

## 6. Checklist
- [ ] Goal/KPI rõ ràng.
- [ ] Build dev bật logging.
- [ ] Survey & consent form sẵn.
- [ ] Telemetry gửi được về dashboard.
- [ ] Retro sau mỗi đợt playtest.

## 7. Links
- [Core Loop Mastery](./core-loop-mastery.md)
- [Economy Systems](./economy-systems.md)
- [Narrative Toolkit](./narrative-toolkit.md)