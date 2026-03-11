---
title: "Console Development"
description: "Certification, TRC/TCR/XR, platform features (achievements, cloud save), performance on consoles."
tags:
  - console
  - certification
  - platform
  - game-dev
updated: 2026-03-11
---

# 🎮 Console Development

> Mục tiêu: vượt qua certification (TRC/TCR/XR), tận dụng feature platform (achievement, cloud save), và đảm bảo hiệu năng console.

## 1) Certification Readiness
- Đọc checklist TRC/TCR/XR theo platform (PS/Xbox/Switch).
- Handle suspend/resume, network disconnect, storage full, account/sign-in flow.
- Region/age rating; parental control; seizure warning.
- Save/Resume matrix: verify save integrity trên suspend/resume, profile switch, storage gần đầy; test clock change/timezone.
- Error handling: map error code → thông điệp user theo guideline platform; không crash app khi mất network/peripheral disconnect.
- Media compliance: capture/stream restriction, spoiler protection nếu platform yêu cầu.
- **Unity:** dùng Platform SDK plugin (PS/Xbox/Switch) đúng version; test Application.pause/suspend/resume callback, OnApplicationFocus; serialize save với Application.persistentDataPath + versioning để tránh corruption khi resume.

## 2) Platform Features
- Achievements/Trophies API; cloud save; leaderboards.
- Controller features: rumble, adaptive triggers (PS5), gyro (Switch).
- Rich presence/activity cards; capture/stream compliance.
- Cross-save/x-play: nếu hỗ trợ, kiểm tra format save và entitlement mapping.
- Entitlement & commerce: ownership check, DLC entitlement refresh khi offline/online.
- Voice/party chat compliance: tuân thủ policy platform; parental control respect.
- **Unity:** dùng Services wrapper (Unity Gaming Services nếu cross-platform; native plugin nếu platform-specific); controller qua Input System với layout cho DualSense/XSX/Pro Controller; map haptics qua platform API (DualSense adaptive trigger via plugin). Presence/Activity Card cần metadata đúng schema của platform SDK.

## 3) Performance & Build
- Target 60fps (hoặc 30fps lock ổn định) với frame pacing tốt.
- Memory budget cố định; async loading; asset bundle split theo mode/region.
- Patch/DLC pipeline; delta patch size nhỏ; save compatibility.
- Frame pacing: kiểm tra 16.6ms/33ms histogram; hạn chế shader compilation runtime (strip variant, prebake PSO/XSO).
- I/O: dùng async I/O API đặc thù (PS5/Xbox Velocity); align block size để giảm seek.
- Build configs: dev/test/release flag rõ; capture perf overlay build cho QA (fps/mem/drawcall).
- **Unity:** bật IL2CPP, strip engine code, bật Burst + Jobs nếu phù hợp; dùng Addressables + Scriptable Build Pipeline cho split package. Prewarm ShaderVariantCollection, bật Load/Build Player setting cho PSO cache. Async load bằng Addressables + SceneManager.LoadSceneAsync additive.

## 4) Compliance & UX
- Safe area & overscan; text legibility trên TV.
- Localization file per region; font fallback; profanity filter nếu có UGC.
- Error code mapping & user-facing message theo guideline platform.
- HDR/SDR: tone-map và calibration theo platform; đảm bảo UI text legible cả SDR/HDR.
- Accessibility: remap input, subtitles/captions, color-blind filters theo yêu cầu platform.
- Storage policy: thông báo dung lượng cần thiết, xử lý graceful khi full, không soft-lock.
- **Unity:** hỗ trợ HDR trong Render Pipeline asset (URP/HDRP), test color buffer format; UI scale cho 1080p/4K với Canvas Scaler; font fallback per locale; profanity filter server-side + client regex lightweight. Kiểm tra TV overscan bằng safe zone (Platform SDK + in-game option).

## ✅ Apply it
- [ ] Làm TRC/TCR pass list cho build; test suspend/resume + disconnect.
- [ ] Tích hợp achievements + cloud save + presence.
- [ ] Kiểm soát FPS/frame pacing (histogram) và memory budget theo platform target; strip shader variant.
- [ ] Đảm bảo safe area, text legibility, HDR/SDR, accessibility, và thông báo lỗi theo guideline.
- [ ] Test save/resume matrix (suspend/resume, profile switch, storage full) và entitlement refresh.
- [ ] Unity: bật IL2CPP, Burst/Jobs khi phù hợp; prewarm ShaderVariantCollection; test Application.pause/focus + Addressables async load trên devkits.

## 🔗 Cross-reference
- [Localization](../localization/README.md)
- [Unity Impact Metrics](../metrics/unity-impact-metrics.md)