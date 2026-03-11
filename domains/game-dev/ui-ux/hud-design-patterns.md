---
title: "HUD Design Patterns"
description: "Diegetic vs non-diegetic, priority, readability, configurability."
tags:
  - ui
  - hud
  - game-dev
updated: 2026-03-11
---

# 🎯 HUD Design Patterns

## 1) Goals
- Truyền thông tin cốt lõi (health/ammo/objective) rõ ràng, không lấn át cảnh.
- Phân cấp thông tin: trọng yếu (always visible), thứ cấp (contextual), tùy chọn (toggle).
- Hỗ trợ platform khác nhau (pad/KBM/mobile) và tùy biến (scale/opacity/bindings).

## 2) Diegetic vs Non-diegetic
- Diegetic: UI trong thế giới (hologram trên vũ khí, visor). Ưu: immersive; Nhược: readability tùy camera.
- Non-diegetic: overlay 2D. Ưu: rõ, kiểm soát; Nhược: có thể phá nhập vai.
- Hybrid: critical overlay + diegetic flavor (ví dụ health rõ ràng, ammo trên súng).

## 3) Priority & Layout
- Rule of proximity: nhóm thông tin liên quan; tránh dàn quá rộng.
- Eye travel: đặt thông tin quan trọng gần tâm/crosshair (FPS) hoặc gần nhân vật (TPP/action).
- Safe area: tuân thủ TV safe area (console); cho phép người chơi chỉnh.

### Safe-area preset (ví dụ)
- Console TV: mặc định 90–92% viewport; preset: Compact 95%, Standard 92%, Safe 88%; slider tùy chỉnh.
- Mobile notch/punch-hole: auto đọc safe inset (OS); preset: Standard (inset + 12–16px), Tight (inset + 8px), Loose (inset + 20px) cho người thích không che cạnh.
- PC: full 100% nhưng vẫn có slider cho màn nhỏ/streamer; lưu per-device.

## 4) Readability
- Contrast & size: text ≥ 18–24px ở 1080p; icon có silhouette rõ; outline/border nếu nền phức tạp.
- Color coding + shape: đừng chỉ dựa vào màu (color-blind). Thêm icon/shape.
- Motion discipline: hạn chế animation lặp; dùng micro-movement cho thông tin mới/cảnh báo.

## 5) Contextual & State
- Contextual hints: chỉ xuất hiện khi gần interactable/low health/reload.
- State clarity: cooldown timers, stack, buff/debuff với phân loại màu/shape.
- Damage direction: indicator rõ, fade nhanh; tránh spam.

## 6) Configurability
- Scale/opacity: slider; toggle shake/glow; layout preset (compact/expanded).
- Toggle elements: minimap on/off, quest tracker, damage numbers.
- Input prompt swap: auto đổi icon (Xbox/PS/KBM) và tắt khi user disable tutorial.

## 7) Performance & Tech
- Batch UI draw calls; atlas; tránh overdraw nền phức tạp.
- Update interval: giảm tick UI cho info không cần realtime; throttle layout rebuilds.
- Localization: fit text; fallback font; tránh text truncation.

## ✅ Apply it
- [ ] Xác định thông tin trọng yếu vs contextual; đặt gần khu vực nhìn chính.
- [ ] Chọn hybrid diegetic/overlay nếu cần immersion nhưng vẫn đọc được.
- [ ] Safe area chỉnh được; scale/opacity và prompt swap theo input device.
- [ ] Color-blind safe: icon/shape bổ trợ; text size/outline đủ rõ.
- [ ] Kiểm tra perf: atlas/batching, hạn chế overdraw/animation spam.