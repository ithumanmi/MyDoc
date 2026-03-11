---
title: "Feedback Systems"
description: "Juice, screen shake, hit stop, VFX/SFX/UI feedback có kiểm soát."
tags:
  - feedback
  - juice
  - game-dev
  - ui
updated: 2026-03-11
---

# ⚡ Feedback Systems (Juice)

## 1) Goals
- Phản hồi rõ, thỏa mãn nhưng không gây chóng mặt/mệt.
- Phân cấp: hit nhẹ, hit mạnh, crit, kill, bị trúng, cảnh báo.

## 2) Hit Stop & Screen Shake
- Hit stop: dừng 50–200ms tùy đòn; dùng selective (attacker/target) để giữ camera mượt.
- Screen shake: biên độ nhỏ, duration ngắn; cho phép slider/toggle. Đừng áp dụng lên UI text.
- Stacking: clamp shake/hit stop khi nhiều event; ưu tiên đòn mạnh nhất.

## 3) VFX/SFX
- Layered VFX: impact sprite, sparks, debris, light flash; opacity và scale theo cường độ.
- SFX: pitch/volume theo lực; sidechain ducking nhẹ music khi impact lớn.
- Spatial: đặt nguồn âm hợp lý; tránh spam âm cao tần gây mệt.

## 4) UI Feedback
- Damage numbers: scale màu/size cho crit; fade nhanh; toggle được.
- Crosshair: expand khi bắn, recover khi nghỉ; đổi màu khi hit; đổi icon khi crit/weak spot.
- State: buff/debuff icon pulse nhẹ; cooldown fill; warning flash có giới hạn thời gian.

## 5) Input & Responsiveness
- Buffering & cancel window: giảm cảm giác “ăn nút”; telegraph rõ khi input bị khóa.
- Haptic: rung ngắn cho hit; cường độ thấp cho action nhẹ; cho phép tắt/giảm.

## 6) Performance & Comfort
- Pooling VFX/UI; tránh tạo destroy liên tục.
- Cap particle count; LOD VFX trên mobile/low-end.
- Photosensitivity: tránh flash trắng full-screen; dùng mask nhỏ/gradient; cảnh báo nếu cần.

### Checklist A/B (shake / hit stop)
- Mục tiêu: tăng cảm giác impact nhưng không gây mệt/nhức đầu.
- Thử các biến: biên độ shake (px/deg), duration (ms), falloff, axis (x/y vs roll), hit stop duration/target (attacker/target/global), clamp khi nhiều event.
- Đo lường:
  - Player discomfort survey (Likert 1-5): chóng mặt/mệt/khó đọc.
  - Combat clarity: % trượt input (buffer) khi hit stop xảy ra; % miss telegraph do shake.
  - Session length/quit rate sau combat dày.
  - Perf: frame time spike khi spam VFX/shake.
- Quy tắc an toàn: có slider/toggle; giới hạn shake tổng; skip shake khi photosensitivity mode.
- Chốt: chọn cấu hình đạt điểm impact cao mà discomfort thấp; giữ clamp mặc định, slider cho người chơi.

## ✅ Apply it
- [ ] Thiết lập hit stop/shake có clamp và slider/toggle.
- [ ] Crosshair/damage number phản hồi rõ, tắt được.
- [ ] VFX/SFX layer theo cường độ; sidechain ducking nhẹ.
- [ ] Haptic có mức; tắt được; input buffer/cancel rõ.
- [ ] Perf/comfort: pooling, cap particle, tránh flash gắt.