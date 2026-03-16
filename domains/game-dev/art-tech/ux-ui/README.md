---
title: "UX/UI for Games"
description: "HUD design, accessibility, feedback systems, readability & moment-to-moment clarity."
tags:
  - ux
  - ui
  - game-design
updated: 2026-03-11
---

# 🧭 UX/UI for Games

> Mục tiêu: HUD rõ ràng, thông tin ưu tiên, phản hồi tức thì. Kết hợp accessibility và telegraphing để giảm thất vọng cho người chơi.

## 1) HUD & Information Hierarchy
- Ưu tiên thông tin: máu/đạn/quest → mini-map → buff/debuff.
- Kích thước/contrast đủ đọc trên TV/mobile; safe zone UI.
- Trạng thái quan trọng dùng icon + màu + text ngắn.

## 2) Feedback Systems
- **Triad Feedback:** Visual (flash), Audio (cue), Haptic (nếu có).
- **Telegraphing:** cảnh báo trước đòn đánh AoE; channel time rõ.
- **Cooldown/Reload:** progress indicator, không chỉ disable nút.

## 3) Accessibility
- **Colorblind-friendly:** palette và icon shape; tránh rely vào màu đơn.
- **Subtitles/CC:** cỡ chữ, nền mờ, chỉ speaker.
- **Input remap:** keybinding; toggle/hold cho sprint/aim; stick deadzone config.

## 4) Menu & Flow
- Main → Play → Settings → Quit: depth nông, 3 click tới mục chính.
- Pausable menu cho single-player; snapshot state khi pause.
- Settings: audio mix, gfx preset, controls, accessibility group.

## 5) Metrics & QA
- Time-to-locate (TTL) UI element; error rate (bấm nhầm) trong tutorial.
- Heatmap click/tap nếu mobile; record eye-tracking nếu có.
- A/B HUD layout; retention vs frustration in early sessions.

## ✅ Apply it
- [ ] Ưu tiên 5 thông tin quan trọng nhất lên HUD; test readability 3 mét (TV) & 30 cm (mobile).
- [ ] Thêm telegraphing + audio cue cho đòn mạnh/AoE.
- [ ] Bật colorblind palette + subtitles tùy chỉnh size/nền.
- [ ] Cho phép remap key/binding cơ bản + toggle/hold cho hành động dài.
- [ ] Đo TTL tìm UI chính và tỉ lệ bấm nhầm trong tutorial.

## 🔗 Cross-reference
- [Playtest Framework](../game-design/playtest-framework.md) – đo lường UX định lượng.
- [Audio & Sound Design](../audio/README.md) – đồng bộ cue âm thanh với UI feedback.