---
title: "Mobile Touch UX"
description: "Gesture patterns, thumb zones, target size, latency, comfort."
tags:
  - mobile
  - ux
  - ui
  - game-dev
updated: 2026-03-11
---

# 📱 Mobile Touch UX

## 1) Goals
- Tương tác thoải mái một tay/hai tay; tránh che nội dung quan trọng.
- Giảm latency cảm nhận; target dễ chạm; gesture rõ ràng, không xung đột.

## 2) Thumb Zones & Layout
- Khu vực thuận: góc dưới/trung tâm hai bên; khó với góc trên đối diện.
- Đặt nút chính trong vùng thuận; tránh đặt action quan trọng ở góc xa.
- Split input: joystick ảo bên trái, action bên phải; cho phép reposition/resize nếu được.

## 3) Target Size & Spacing
- Kích thước tối thiểu 44–48px; spacing đủ để tránh chạm nhầm.
- Multi-action cluster: ưu tiên 2–3 nút chính; nút phụ dùng radial/hold menu.
- Avoid edge swipe conflict (OS gesture); chừa mép hoặc đổi gesture trong game.

## 4) Gesture Patterns
- Tap/Double-tap/Hold: rõ ràng, có feedback (glow/timer) khi hold.
- Swipe/Flick: hướng rõ; đừng lạm dụng khi màn hình đông ngón.
- Pinch/Rotate: dùng cho camera/zoom; đừng yêu cầu độ chính xác cao trong combat.
- Cancel: cho phép drag-out-to-cancel khi đang hold/charge.

## 5) Feedback & States
- Visual: highlight khi touch down; progress ring cho hold/charge.
- Audio/haptic: tick nhẹ khi nhận input; rung nhẹ khi success; tắt/giảm được.
- Error: báo khi input bị chặn (cooldown/energy) thay vì im lặng.

## 6) Performance & Latency
- Giảm input latency: ưu tiên thread/input update; giảm post-processing nặng.
- Culling UI update không cần thiết; limit layout rebuild.
- Check thermal: UI animation nhẹ, tránh loop nặng.

## 7) Accessibility (Mobile)
- Left-handed mode: hoán đổi cụm nút; remap cơ bản.
- Text size/contrast cao; icon rõ trên nền sáng/tối.
- Assist: auto-run, auto-pickup, aim assist nhẹ; toggle tùy người chơi.

## ✅ Apply it
- [ ] Bố trí nút chính trong thumb zone thuận; tránh góc xa.
- [ ] Target ≥44–48px, spacing đủ; tránh xung đột gesture mép màn.
- [ ] Feedback rõ cho tap/hold/swipe; haptic nhẹ, tắt được.
- [ ] Tối ưu latency/UI perf; tránh animation nặng, rebuild UI liên tục.
- [ ] Hỗ trợ left-handed mode, text size/contrast, assist tùy chọn.