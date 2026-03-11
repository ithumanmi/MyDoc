---
title: "Hollow Knight Combat Notes"
description: "Cách Team Cherry xử lý input buffer, hitbox/hurtbox và combat feel."
tags:
  - combat
  - case-study
  - hollow-knight
updated: 2026-03-11
---

# ⚔️ Hollow Knight Combat Case Study

## Input Buffer & Feel
- **3-frame grace window**: game nhận input jump/attack tới 3 frame trước landing → cảm giác responsive.
- **Context-aware buffer**: nếu đang knockback vẫn ghi nhận input để thực thi khi recover.
- **Queue priority**: dash > jump > attack, giúp cancel animation hợp lý.

## Hitbox / Hurtbox Architecture
- **Separate Physics Layer** cho nail vs enemy hurtbox, giảm collision check.
- **Dynamic hurtbox scaling**: boss phase thay đổi hurtbox để telegraph rõ hơn.
- **Disjoint hitbox**: nail swing dùng spline data → tránh bị rỗng ở đầu/đuôi animation.

## Tech Notes
- 60fps target, fixed timestep 0.0167s đảm bảo input sampling ổn định.
- Attack data lưu trong **ScriptableObject** (damage, knockback, invuln window).

## Lessons
1. **Grace frames** tăng forgiveness → người chơi cảm giác chính xác.
2. **Priority queue** giúp cancel mượt mà mà không cần animation phức tạp.
3. **Hurtbox scaling** là kỹ thuật rẻ để đánh dấu phase & difficulty.