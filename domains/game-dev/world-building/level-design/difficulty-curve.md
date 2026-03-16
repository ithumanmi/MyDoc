---
title: "Difficulty Curve"
description: "Tutorial in-context, challenge ramp, pacing, skill checks, fairness."
tags:
  - level-design
  - difficulty
  - game-dev
updated: 2026-03-11
---

# 📈 Difficulty Curve

## 1) Goals
- Onboarding mượt, dạy cơ chế trong ngữ cảnh, tăng độ khó có kiểm soát.
- Công bằng: lỗi do người chơi, không do camera/điều khiển/telegraph kém.

## 2) Tutorial & Onboarding
- Teach-by-doing: giới thiệu cơ chế trong không gian an toàn, không chết ngay.
- Một lúc một ý: không dồn nhiều mechanic cùng lúc; dùng signage/VO/ngữ cảnh.
- Repeat-to-learn: lặp nhẹ 2-3 lần trong tình huống biến thể.

## 3) Ramp & Pacing
- Mẫu phổ biến: Intro (dễ) → Build → Mid-test → Climax → Cooldown.
- Xen kẽ nhịp: combat ↔ puzzle ↔ traversal để tránh fatigue.
- Boss/skill check: kiểm tra cơ chế đã dạy; telegraph rõ; checkpoint trước cửa.

## 4) Fairness & Telegraph
- Telegraph rõ (animation, VFX, audio) cho đòn nguy hiểm; tránh hitbox mập mờ.
- Camera/readability: đảm bảo FOV/độ sáng cho phản xạ; tránh kẻ địch tấn công từ off-screen nếu không báo trước.
- Input buffer: cho phép nhỏ (100–200ms) với game hành động; giảm cảm giác “ăn nút”.

## 5) Data & Iteration
- Telemetry: death heatmap, time-to-first-success, retry count; phân đoạn theo room/encounter.
- A/B: thử vị trí checkpoint/health pickup; thử giảm số kẻ địch trong lần đầu.
- Playtest mới: người chơi chưa biết game; đo thời gian hiểu mechanic.

### Checklist Playtest / Telemetry Template
- Scope: chọn 1-2 level hoặc encounter đại diện; khóa build.
- Người chơi: mới (chưa biết game) + quen (đã chơi) để so sánh.
- Ghi nhận:
  - Time-to-first-success, số lần death/retry per room/encounter.
  - Death heatmap; damage source (projectile/melee/trap) và có telegraph không.
  - Checkpoint effectiveness: % người chơi dùng checkpoint gần nhất.
  - Pickup/loot rate; % miss ở side path.
  - Pathing: % người chơi đi main path vs lạc; thời gian tìm đường > ngưỡng?
  - Tutorial comprehension: người chơi có thực hiện đúng mechanic sau khi dạy?
- Quan sát định tính: cảm nhận nhịp (mệt/nhạt), điểm bực tức, chỗ camera xấu.
- Sau test: A/B thay đổi nhỏ (checkpoint, kẻ địch đầu tiên), chạy lại trên nhóm mới.

## 6) Accessibility
- Tùy chọn hỗ trợ: aim assist, puzzle hint timer, slow mode tạm; không phá vỡ thử thách cốt lõi.
- Color/contrast: kẻ địch/bẫy nổi bật; hỗ trợ color-blind nếu cần.

## ✅ Apply it
- [ ] Thiết kế tutorial in-context (an toàn, một cơ chế một lần).
- [ ] Đặt ramp theo nhịp: Intro → Build → Mid-test → Climax → Cooldown.
- [ ] Skill check/boss với telegraph rõ + checkpoint gần.
- [ ] Thu telemetry (death/time-to-first-success) và A/B checkpoint/health.
- [ ] Thêm tùy chọn hỗ trợ (aim assist/slow/hint) mà không phá core challenge.