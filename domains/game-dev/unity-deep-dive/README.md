---
title: "Unity Deep Dive Module"
description: "Architecture, clean code, tooling và tối ưu hóa để ship game production."
tags:
  - unity
  - architecture
updated: 2026-03-11
---

# 🧠 Unity Deep Dive Module

| File | Nội dung | Khi nào dùng |
| --- | --- | --- |
| [architecture-patterns.md](./architecture-patterns.md) | ScriptableObject architecture, event channel, DI | Refactor dự án scale > 10k LOC |
| [unity-clean-code-solid.md](./unity-clean-code-solid.md) | SOLID, anti-pattern và guideline coding style | Training team, review code |
| [optimization-techniques.md](./optimization-techniques.md) | Memory, batching, GC, Addressables | Chuẩn bị launch mobile/console |
| [optimize-unity-playbook.md](./optimize-unity-playbook.md) | Playbook 5 pha đo → tối ưu → guardrail | Lặp lại mỗi sprint để giữ FPS ổn định |
| [editor-scripting.md](./editor-scripting.md) | Custom Inspector, tool automation | Tạo pipeline build/QA riêng |
| [profiler-dev-build-mastery.md](./profiler-dev-build-mastery.md) | Sử dụng Profiler, capture Dev build | Điều tra drop FPS, memory leak |
| [vfx-lighting-mastery.md](./vfx-lighting-mastery.md) | Lighting, VFX sync | Kết hợp Tech Art + Gameplay |
| [module-roadmap-unity-build-system.md](./module-roadmap-unity-build-system.md) | Checklist build pipeline | Team LiveOps cần CI/CD |
| [game-quality-playbook.md](./game-quality-playbook.md) | QA checklist, telemetry loop | Đóng gói để gửi publisher |

**Guided flow:** Architecture → Clean code → Tooling → Optimization → QA/Build.

> Kết hợp với [Game Server Guide](../game-server-guide.md) nếu dự án có multiplayer.