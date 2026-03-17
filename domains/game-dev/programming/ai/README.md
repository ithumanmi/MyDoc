---
title: "Programming / AI"
description: "Hub: AI gameplay (Steering, Behavior Tree, GOAP) cho NPC."
tags: [game-ai, unity, steering, behavior-tree, goap]
updated: 2026-03-17
---

# 🤖 Programming / AI Hub

Tóm tắt: Thiết kế AI NPC có di chuyển mượt (steering) và ra quyết định rõ ràng (BT/GOAP), tránh if-else spaghetti, dễ debug/log.

## Nội dung chính
| File | Nội dung | Khi nào dùng |
| --- | --- | --- |
| [game-ai-patterns.md](./game-ai-patterns.md) | FSM, Behavior Tree, GOAP overview | Chọn kiến trúc AI phù hợp scope dự án |
| [steering-behaviors.md](./steering-behaviors.md) | Seek/Flee/Arrive/Formation, obstacle avoidance | Làm chuyển động tự nhiên, tránh va chạm |
| [behavior-tree/](./behavior-tree/) | Core concepts + GraphView editor | NPC nhiều mục tiêu, cần debug luồng hành vi |

## Khi nào dùng
- NPC patrol/chase/flee/combat cần mở rộng nhanh.
- Boss/companion/crowd AI vượt quá if-else.
- Muốn log, quan sát tick và tối ưu hiệu năng AI.

## Workflow gợi ý
1) Chọn kiến trúc trong `game-ai-patterns.md` (FSM/BT/GOAP).  
2) Prototype steering để đạt feel mượt.  
3) Nâng cấp sang BT/GOAP, thêm telemetry (state transitions, tick time).  
4) Review perf & hành vi với designer trước khi ship.