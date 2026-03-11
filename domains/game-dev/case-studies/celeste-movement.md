---
title: "Celeste Movement Study"
description: "Phân tích input buffering, coyote time và juice của Celeste."
tags:
  - platformer
  - case-study
  - celeste
updated: 2026-03-11
---

# 🧗 Celeste Movement Case Study

## Core Systems
- **Coyote Time**: ~6 frame window sau khi rời platform vẫn nhảy được.
- **Jump Buffer**: 4 frame trước khi chạm đất, input jump được giữ lại.
- **Dash Queue**: nếu dash đang cooldown, input dash sẽ thực thi khi reset.

## Juice Techniques
- Camera **screen shake micro** khi dash/land.
- Sprite squash & stretch 10% khi nhảy/đáp.
- Trail render + particle để đọc hướng dash.

## Code Architecture
- Movement update theo state machine: `Grounded`, `Airborne`, `Climbing`, `Dash`.
- Physics timestep fixed 60Hz; visual interpolation cho cảm giác mượt.
- Input xử lý qua **Command Buffer** để unify keyboard/controller.

## Lessons
1. **Coyote + buffer** tạo cảm giác chính xác dù level khó.
2. **Micro juice** (shake, trail) giúp người chơi đọc trạng thái tốt hơn.
3. **State machine rõ ràng** cho phép bổ sung mechanic (feather, wind) mà không phá codebase.