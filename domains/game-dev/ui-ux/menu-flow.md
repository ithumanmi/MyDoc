---
title: "Menu Flow"
description: "UX best practices, navigation, input state, focus, back/cancel consistency."
tags:
  - ui
  - ux
  - menu
  - game-dev
updated: 2026-03-11
---

# 🧭 Menu Flow

## 1) Goals
- Dễ điều hướng, back/cancel nhất quán, không mất focus/input.
- Tốc độ: load nhanh, không animation thừa; ưu tiên accessibility (text size/contrast, remap, captions).

## 2) Navigation & Focus
- State machine rõ: main → sub → detail; luôn biết nút Back làm gì.
- Focus ring: luôn hiển thị; tránh focus rơi vào void khi mở/đóng panel.
- Gamepad vs KBM: hỗ trợ cả hai; lock mouse khi cần; hover không phá focus gamepad.
- Skip intro/ads: cho phép skip/log in nhanh; nhớ tài khoản gần nhất.

## 3) Back/Cancel Consistency
- Một nút Back duy nhất (B/O/Esc/Right-click) có hành vi dự đoán được.
- Thoát màn hình nặng (matchmaking/settings chưa apply) → confirm; màn hình nhẹ → back ngay.
- Breadcrumb hoặc header để biết đang ở đâu.

## 4) Information Architecture
- Nhóm theo tác vụ: Play/Continue, Social, Options, Store tách bạch.
- Giảm depth menu: 2–3 tầng tối đa cho tác vụ phổ biến.
- Search/filter/sort cho danh sách dài (inventory/store/server list).

## 5) Performance & Robustness
- Preload data cho màn hình chính; async load list (pagination) tránh freeze.
- Offline/failure: thông báo nhẹ, retry, không kẹt softlock.
- Input buffer/throttle: tránh double-activate khi spam nút.

## 6) Accessibility Hooks
- Text size, high contrast, color-blind friendly; remap input; captions/subtitles (nếu có media).
- Screen reader: cung cấp label/focus order logic nếu hỗ trợ.

## ✅ Apply it
- [ ] Định nghĩa state/back rõ ràng; focus không rơi vào void.
- [ ] Một hành vi Back/Cancel thống nhất; confirm chỉ khi mất dữ liệu/thao tác nặng.
- [ ] Tối ưu load: async list, preload cần thiết; handle offline/failure nhẹ nhàng.
- [ ] Hỗ trợ KBM+pad: hover không phá focus; input prompt theo device.
- [ ] Accessibility: text size/contrast, remap, captions/screen reader (nếu hỗ trợ).