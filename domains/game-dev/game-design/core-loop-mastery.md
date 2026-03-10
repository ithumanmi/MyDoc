---
title: "Core Loop Mastery"
description: "Framework thiết kế core loop và KPI đo lường sức khỏe trải nghiệm."
tags:
  - game-design
  - core-loop
updated: 2026-03-11
---

# ♻️ Core Loop Mastery

> Core loop = hành động lặp lại tạo nên 80% thời gian trải nghiệm. Nếu loop chán, mọi feature khác khó cứu.

## 1. Define Player Fantasy
- Fantasy sentence (15 chữ).
- Target session length, platform, audience archetype.
- Emotion target: mastery, relaxation, competitive...

## 2. Loop Diagram
```
Sense → Decide → Execute → Reward → Upgrade → Reset
```

| Step | Hành động | Feedback | KPI chính |
| --- | --- | --- | --- |
| Sense | Player scan thông tin | Highlight mục tiêu | Attention time < 2s |
| Decide | Chọn skill/card | UI affordance | Decision confidence |
| Execute | Action (tap/dash/build) | VFX/SFX/Haptic | Success rate |
| Reward | XP/Loot/Story beat | Drop animation | Reward perception |
| Upgrade | Spend currency | Meta UI | Retention |

## 3. Rulebook
- Input mapping & cooldown.
- Resource cost (stamina, mana).
- Fail states (combo break, HP loss).
- Synergy với loop phụ (economy, narrative).

## 4. KPI & Instrumentation
- Usage rate.
- Success rate.
- Time-to-fun.
- Reward frequency.
- Gắn telemetry: `LoopStart`, `LoopEnd`, `LoopFailReason` → [Unity Impact Metrics](../metrics/unity-impact-metrics.md).

## 5. Iteration Playbook
1. Prototype graybox.
2. Playtest 5 người/ngày.
3. Survey nhanh “Bạn có muốn lặp lại loop này 10 lần nữa?”
4. Update rules + KPI.

## 6. Checklist
- [ ] Loop mô tả bằng 1 câu.
- [ ] Feedback rõ ràng.
- [ ] KPI đo được.
- [ ] Có meta hook trong 5 phút.
- [ ] Doc cập nhật sau mỗi iteration.

## 7. Tools & Links
- Miro loop board, KPI spreadsheet.
- [Core Mechanic GDD](../core-mechanic-design-doc.md)
- [Economy Systems](./economy-systems.md)
- [Playtest Framework](./playtest-framework.md)