---
title: "Game Testing & Telemetry"
description: "QA automation, playtesting methodology, telemetry instrumentation for game quality."
tags:
  - testing
  - qa
  - telemetry
  - game-dev
updated: 2026-03-11
---

# 🧪 Game Testing & Telemetry

> Mục tiêu: kết hợp QA tự động, playtest có phương pháp, và telemetry để phát hiện lỗi/bottleneck sớm.

## 1) QA Automation
- **Unit/Integration:** tách logic thuần C# khỏi MonoBehaviour để test.
- **Golden recording:** capture input/replay để regression; snapshot test UI.
- **Build validation:** smoke test scene chính, check missing refs/asset GUID.

## 2) Playtesting Methodology
- **Test script:** mục tiêu rõ (onboarding, combat loop, economy); giới hạn 15-30 phút.
- **Think-aloud:** ghi nhận hành vi + câu hỏi; tránh giải thích trước.
- **Metrics định lượng:** time-to-first-fun, fail/quit point, success rate per mission.

## 3) Telemetry Instrumentation
- **Event schema:** session start/end, death, checkpoint, loot, economy sink/source.
- **Performance:** FPS, frame time histogram, memory spike, crash dump.
- **Sampling:** tránh spam log; batch upload; respect privacy/consent.

## 4) Tools & Pipelines
- Unity Test Runner, PlayMode tests; CI chạy headless build.
- Crash reporting (Backtrace/Sentry), analytics (Unity Analytics, Firebase).
- Profiling capture (GPU/CPU) theo milestone build.

## ✅ Apply it
- [ ] Viết 3 PlayMode tests cho core mechanic và 1 golden recording.
- [ ] Thiết kế event schema (session, death, loot, checkpoint) và gửi thử lên analytics.
- [ ] Thu metrics TTF (time-to-first-fun) và điểm quit trong tutorial.
- [ ] Thiết lập crash reporting + sample rate phù hợp.
- [ ] Chạy smoke test tự động trên build mỗi commit main.

## 🔗 Cross-reference
- [Playtest Framework](../game-design/playtest-framework.md) – quy trình test định tính + định lượng.
- [Unity Impact Metrics](../metrics/unity-impact-metrics.md) – KPI LiveOps và hiệu năng.