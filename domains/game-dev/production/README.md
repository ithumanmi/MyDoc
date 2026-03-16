---
title: "Production & Ops"
description: "Unity deep dive, engine comparisons, metrics và QA testing."
tags:
  - production
  - unity
  - qa
updated: 2026-03-16
---

# 🏭 Production & Ops

| Module | Nội dung | Khi nào dùng |
| --- | --- | --- |
| [unity-deep-dive/](./unity-deep-dive/README.md) | Architecture, clean code, profiling, editor tools | Khi bước vào production dài hạn |
| [engines/](./engines/README.md) | Unity DOTS vs Unreal (Nanite/Lumen) | Đánh giá engine hoặc tối ưu dự án lớn |
| [metrics/](./metrics/README.md) | Unity Impact Metrics, genre cheat sheet | Đo lường KPI, chuẩn bị soft-launch |
| [qa-testing/](./qa-testing/README.md) | QA workflow, test plan, automation | Thiết lập quy trình QA nội bộ |

## Workflow gợi ý
1) Chốt kiến trúc & coding standard → [unity-deep-dive](./unity-deep-dive/README.md)
2) Định nghĩa KPI & thiết lập telemetry → [metrics](./metrics/README.md)
3) Build pipeline & perf budget → engines/optimization docs
4) QA checklist & automation → [qa-testing](./qa-testing/README.md)

## Cross-links
- [Programming / Networking](../programming/networking/game-server-guide.md)
- [Art-Tech / Graphics](../art-tech/graphics/README.md)
- [Cheatsheets / Optimization](../cheatsheets/optimization-checklist.md)