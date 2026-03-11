---
title: "Mobile Game Optimization"
description: "Battery, thermal, touch input patterns, memory & rendering budgets cho mobile."
tags:
  - mobile
  - optimization
  - performance
  - game-dev
updated: 2026-03-11
---

# 📱 Mobile Game Optimization

> Mục tiêu: giữ FPS ổn định, không nóng máy, tiết kiệm pin, và input touch chính xác.

## 1) Performance & Thermal
- **Frame budget:** 16.6ms @60fps, 33ms @30fps; theo dõi frame time histogram.
- **CPU/GPU:** giới hạn draw calls, batching, giảm overdraw UI; bật GPU instancing.
- **Thermal:** test 20-30 phút trên thiết bị mục tiêu; giảm post-process, hạ refresh khi nóng.
- **Thermal throttling plan:** hạ dần refresh/FPS cap theo state (nominal → warm → hot), ưu tiên giảm effect/shadow rồi mới giảm resolution; tắt effect nền khi màn pause.
- **Heatsink-aware design:** đo surface temp vs frame time; tránh burst CPU (job system) và GPU spikes (shader variant strip, simplify particle pass).
- **Unity:** dùng Application.targetFrameRate + QualitySettings.vSyncCount; theo dõi FrameTimingManager, Adaptive Performance (Samsung/Android) để hạ level; bật Dynamic Resolution (URP/HDRP) và Adaptive Performance scaler (CPU/GPU/cluster).

## 2) Memory & Assets
- Texture compression (ASTC/ETC2); atlas UI; limit RTT size.
- Addressables/asset bundle: tải theo scene/region; LOD aggressive; pool object.
- Tránh GC spike: pre-allocate, reuse list, tránh string concat trong Update.
- **Unity:** Scriptable Build Pipeline + Addressables profile per tier; Mesh/Texture import setting per platform; bật mip streaming; sử dụng Object Pool (Collections) và tránh LINQ/boxing trong Update.

## 3) Battery Life
- Giảm tick nền; tắt hệ thống không cần khi pause/menu.
- Adaptive quality: giảm resolution scale hoặc shadow khi FPS tụt.
- Hạn chế vibration/haptics liên tục; batch network call.
- Network batching: gom request theo nhịp (ví dụ 1-2s) thay vì liên tục; hạn chế wake-lock.
- Sensor budget: tắt/giảm sampling gyro/accel khi không cần; giảm GPS polling.
- Background policy: dừng render khi app background; hạ update rate UI khi idle.
- **Unity:** Application.runInBackground = false (mobile), giảm UI update với Canvas batching; sử dụng LateUpdate/FixedUpdate hợp lý; bật Multithreaded Rendering nếu ổn định thermal.

## 4) Touch Input Patterns
- Deadzone & tap-slop hợp lý; tránh multi-touch ghost.
- Gesture priority (swipe vs tap); visual feedback ngay khi nhận input.
- UI safe zone cho màn hình tai thỏ; kiểm tra orientation/rotation lock.
- Latency: giảm input latency bằng việc đọc touch ở đầu frame và áp dụng ngay frame đó; tránh heavy GC giữa input-read và simulation.
- Palm rejection & edge swipe: phân biệt system gesture (Android nav, iOS home bar); safe margin cho gesture cạnh.
- Touch heatmaps: log vị trí touch để chỉnh layout, safe zone theo thiết bị.
- **Unity:** ưu tiên Input System package (Events + EnhancedTouch); đọc input ở đầu Update, áp dụng ở FixedUpdate/Update kế tiếp; dùng EventSystem raycast nhẹ (GraphicRaycaster tối ưu). Kiểm tra Safe Area API (Screen.safeArea) cho notches.

## 5) QA & Telemetry
- Log FPS, frame time P50/P95, thermal state, battery drain (%/10 phút).
- Device matrix: low/mid/high tier Android + iOS.
- Capture crash ANR; monitor hitch >50ms.
- **Unity:** bật Profiler (Standalone/Android/iOS) và Profile Analyzer; build Development + Deep Profiling off khi đo perf; dùng Adaptive Performance stats; capture logcat với Unity tag; bật Crashlytics/Backtrace nếu có SDK.

## ✅ Apply it
- [ ] Thiết lập adaptive quality + FPS cap phù hợp.
- [ ] Bật texture compression + atlas UI; kiểm tra overdraw.
- [ ] Pool object và tránh GC spike trong Update/LateUpdate.
- [ ] Kiểm thử 30 phút trên 3 cấu hình; log thermal/battery/FPS + thermal state.
- [ ] Tune touch gesture (deadzone, tap-slop), safe zone UI, và check palm/system gesture.
- [ ] Thiết lập thermal throttling ladder (FPS cap/quality) và verify không drop frame pacing.
- [ ] Unity: dùng FrameTimingManager + Adaptive Performance scaler; kiểm tra Dynamic Resolution (URP/HDRP) và safe area Screen.safeArea.

## 🔗 Cross-reference
- [Optimization Techniques](../unity-deep-dive/optimization-techniques.md)
- [Unity Impact Metrics](../metrics/unity-impact-metrics.md)