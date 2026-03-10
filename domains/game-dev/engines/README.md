---
title: "Game Engines Module"
description: "So sánh Unity DOTS/ECS và Unreal Engine 5 để chọn nền tảng phù hợp."
tags:
  - engines
  - unity
  - unreal
updated: 2026-03-11
---

# 🛠️ Game Engines Module

| File | Nội dung | Khi nào dùng |
| --- | --- | --- |
| [unity-advanced.md](./unity-advanced.md) | DOTS, ECS, Burst, job system | Cần tối ưu hiệu năng cao, server logic | 
| [unreal-engine-5.md](./unreal-engine-5.md) | Nanite, Lumen, Blueprint vs C++ | Đánh giá khi team chuyển sang UE5 |

**Decision tips:**
- Unity DOTS cho mobile/indie cần kiểm soát chi phí.
- Unreal 5 mạnh ở AAA visual, nhưng cần pipeline khác (C++, build farm).

> Kết hợp với [Game Server Guide](../game-server-guide.md) để chọn kiến trúc phù hợp từng engine.