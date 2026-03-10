---
title: "Game AI Module"
description: "Behavior Tree, steering, GOAP và các mẫu AI cho gameplay."
tags:
  - game-ai
  - unity
updated: 2026-03-11
---

# 🤖 Game AI Module

| File | Nội dung | Khi nào dùng |
| --- | --- | --- |
| [game-ai-patterns.md](./game-ai-patterns.md) | FSM, Behavior Tree, GOAP overview | Build hệ AI đa dạng cho NPC |
| [steering-behaviors.md](./steering-behaviors.md) | Seek/Flee/Arrive/Formation bằng lực | Làm AI di chuyển tự nhiên, tránh chướng ngại |
| [behavior-tree/](./behavior-tree/) | Core concepts + editor GraphView | Khi cần flow AI phức tạp, dễ debug |

**Gợi ý workflow:**
1. Đọc `game-ai-patterns.md` để chọn mô hình phù hợp.
2. Prototype với Steering Behaviors để có chuyển động mượt.
3. Nâng cấp sang Behavior Tree khi NPC cần nhiều mục tiêu & trạng thái.

> Tham khảo thêm: [Unity AI Toolkit](../unity-deep-dive/architecture-patterns.md) để tích hợp event system & telemetry.