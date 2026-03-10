---
title: "Calculate Puzzle Game Scope Before Production"
description: "Công thức xác định số level cần build cho D1/D7/D14 test dựa trên hành vi người chơi."
tags:
  - game-design
  - production
  - analytics
updated: 2026-03-11
---

# 📐 How We Calculate Puzzle Game Scope Before Production

> Trước kia chúng tôi đoán: build 50+ level rồi cầu nguyện. Giờ dùng công thức: dựa trên hành vi người chơi top game (40–50 phút/ngày, 2–3 session). Làm vừa đủ để test market fit, tiết kiệm hàng tháng dev.

## 📊 Foundation: baseline hành vi
- 40–50 phút mỗi ngày.
- 2–3 session, mỗi session 15–20 phút.
- **Ý nghĩa:** Đây là mức tiêu chuẩn để ước lượng lượng content cần bao nhiêu.

## 🎯 D1 Build – Hook Test
- **Goal:** Core loop giữ chân không?
- **Target Gameplay:** 60–80 phút.
- **Công thức:** `(50 phút ÷ 3 phút/level) × 2 ngày ≈ 33 level`.
- **Deliverable:** 30–35 level polished.
- **Success:** D1 ≥ 40%. Nếu không đạt, thêm level cũng không cứu được loop.

## 📅 D7 Build – Depth Test
- **Goal:** Người chơi cảm thấy progression/metagame?
- **Target Gameplay:** ~320 phút.
- **Công thức:** `(40 phút × 8 ngày) ÷ 3 ≈ 107 level`.
- **Deliverable:** 70–110 level tổng cộng + mechanic mới + meta đơn giản.
- **Success:** D7 retention 15–20%.

## 🚀 D14 Build – Habit Test
- **Goal:** Động lực dài hạn có hình thành?
- **Target Gameplay:** ~600 phút.
- **Công thức:** `(40 phút × 15 ngày) ÷ 3 ≈ 200 level`.
- **Deliverable:** 150–200 level + meta hấp dẫn (decor, progression, collection).
- **Success:** D14 retention 10–12%.

## 💡 Unique vs Repetitive Content
- Không phải mọi level đều phải mới.
- **Unique:** mechanic mới, visual mới, milestone meta.
- **Repetitive:** layout remix lại mechanic lõi.
- **Benefit:** Giữ sản xuất nhẹ nhưng vẫn duy trì retention.

## ⚡ Pro Tips Từ Build Thực Tế
- Tính cả replay/fail: người chơi fail ăn content nhanh hơn.
- Đa dạng thời lượng hoàn thành: early win ngắn, late thử thách dài.
- Front-load 20 level mạnh nhất.
- QA cực kỹ early level: ấn tượng đầu = trần D1.

## ✅ Rule of Thumb
- Dừng đoán mò.
- Tính dựa trên hành vi thực tế.
- Xây đúng lượng content để validate market fit, rồi mới scale.

### Bạn tính scope thế nào?
- Bạn chia unique vs repeat ra sao?
- Có thêm signal nào (economy depth, meta engagement) trước khi mở rộng không?
- Chia sẻ trong repo/Slack để cả team học.

### Liên kết đề xuất
- [The First 48 Hours Metrics](./puzzle-first-48h-metrics.md) – đối chiếu KPI retention sau khi có build.
- [Pixel Flow Engagement](./pixel-flow-engagement.md) – học cách xây engagement trước khi mở rộng scope.