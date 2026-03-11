---
title: "Accessibility"
description: "Color blind, subtitles/captions, remapping, text size, screen reader hooks."
tags:
  - accessibility
  - ui
  - ux
  - game-dev
updated: 2026-03-11
---

# ♿ Accessibility

## 1) Goals
- Cho phép nhiều đối tượng chơi được: nhìn, nghe, vận động, nhận thức.
- Tùy biến theo nhu cầu: màu, chữ, input, tốc độ game.

## 2) Color & Contrast
- Color-blind safe: không dựa chỉ màu; thêm icon/shape/pattern.
- Palette: kiểm tra protan/deutan/tritan; có chế độ color-blind preset.
- Contrast: text ≥ WCAG AA; outline/shadow cho text/reticle trên nền sáng.

## 3) Text & UI
- Text size: slider scale; tránh cố định pixel; wrap hợp lý, không cắt chữ.
- Font: hỗ trợ ký tự đa ngôn ngữ; tránh font quá mảnh; kerning rõ.
- High contrast mode: nền tối, text sáng; hoặc ngược lại tùy người chơi.

## 4) Input & Control
- Remap: full remap KBM/pad; swap stick, invert axis.
- Toggle vs Hold: cho phép chọn toggle aim/sprint/crouch; deadzone/curves chỉnh được.
- QTE/masher: cho phép hold thay vì mash; giảm yêu cầu spam.

## 5) Audio & Captions
- Subtitles & captions: kích thước, background box, speaker label, SFX captions (door slam, explosion).
- Volume mix: master/music/SFX/VO riêng; dynamic range (night mode) giảm chênh lệch lớn.
- Mono/stereo: tùy chọn mono; hướng dẫn loa/tai nghe.

## 6) Motion & Comfort
- Screen shake: slider hoặc toggle; motion blur toggle; FOV chỉnh được.
- Camera bob/roll: giảm/tắt; tránh lắc mạnh.
- Photosensitivity: cảnh flash/strobe cần cảnh báo; giảm intensity hoặc skip.

## 7) Cognitive Load
- HUD noise: giảm clutter; tắt tooltip lặp; highlight chính.
- Tutorials: có thể xem lại; tốc độ text chậm/tua.
- Hint timer: cho puzzle; assist mode (giảm sát thương, kéo dài slow-mo) nếu phù hợp.

## ✅ Apply it
- [ ] Color-blind safe + high contrast option; test với protan/deutan/tritan.
- [ ] Text size/scale, font dễ đọc, wrap không cắt.
- [ ] Remap input, toggle vs hold, deadzone/curve chỉnh được.
- [ ] Subtitles/captions đầy đủ; volume mix + dynamic range.
- [ ] Comfort: shake/blur/FOV chỉnh; cảnh báo flash/photosensitivity.