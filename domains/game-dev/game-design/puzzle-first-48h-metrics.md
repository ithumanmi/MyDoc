---
title: "The First 48 Hours: 7 Metrics That Predict Puzzle Game Success"
description: "Bộ chỉ số UGI dùng sau 1.000 installs đầu tiên để quyết định tiếp tục hay kill."
tags:
  - game-design
  - analytics
  - puzzle
updated: 2026-03-11
---

# ⏱️ The First 48 Hours: 7 Metrics That Predict Puzzle Game Success

> Đây là 7 tín hiệu UGI đo ngay sau 48 giờ để biết nên đầu tư thêm hay dừng lại. Dữ liệu càng sớm, quyết định càng rẻ.

## 1. D0 Session Length
- **Target:** >15 phút.
- **Ý nghĩa:**
  - <12 phút ⇒ Core loop yếu, chưa “hook” được.
  - 12–15 phút ⇒ Trung bình, cần polish.
  - >15 phút ⇒ Tín hiệu engagement mạnh.
  - >20 phút ⇒ Có tiềm năng hit.
- **Vì sao quan trọng:** Dự đoán retention dài hạn tốt hơn bất kỳ early metric nào.
- **Hành động:**
  - <12 phút ⇒ sửa core loop trước khi mở rộng nội dung.
  - >15 phút ⇒ ưu tiên scale, test thêm UA nhỏ.

## 2. Level 1–5 Completion Rate
- **Target:** >90%.
- **Ý nghĩa:**
  - <80% ⇒ Tutorial rối hoặc quá khó.
  - 80–90% ⇒ Chấp nhận được nhưng cần rõ ràng hơn.
  - >90% ⇒ Người chơi hiểu ngay.
  - >95% ⇒ Onboarding xuất sắc.
- **Vì sao quan trọng:** Không qua nổi level 5 thì chẳng ai tới level 100.
- **Hành động:**
  - <85% ⇒ đơn giản hóa level 1, thêm hint.
  - >90% ⇒ onboarding ổn, chuyển sang polish reward.

## 3. Retry Rate After First Fail
- **Target:** >65%.
- **Ý nghĩa:**
  - <50% ⇒ Fail cảm giác bị phạt, không công bằng.
  - 50–65% ⇒ Tạm chấp nhận, nhưng feedback còn thiếu.
  - >65% ⇒ Người chơi thấy đáng thử lại.
  - >75% ⇒ Hook “one more try” rất tốt.
- **Vì sao quan trọng:** Retry = nghiện. Quit = cảm giác bị phạt.
- **Hành động:**
  - <60% ⇒ đổi copy “Failed” thành “Almost!”, thêm slow-mo replay.
  - >70% ⇒ giữ nguyên experience, cân nhắc thêm social brag.

## 4. Session 2 Return Rate
- **Target:** >55%.
- **Ý nghĩa:**
  - <45% ⇒ Không có lý do quay lại.
  - 45–55% ⇒ Mức trung bình.
  - >55% ⇒ Retention mạnh.
  - >65% ⇒ Hình thành thói quen.
- **Vì sao quan trọng:** Là dự báo sớm nhất của D1 retention.
- **Hành động:**
  - <50% ⇒ để lại “next goal” rõ ràng trước khi session 1 kết thúc.
  - >60% ⇒ loop đã có lực kéo, chuẩn bị live ops nhẹ.

## 5. Time To First Confusion
- **Target:** Không xuất hiện trong 10 level đầu.
- **Theo dõi:** Khi nào người chơi pause >10 giây không hành động? Khi nào tap loạn? Khi nào 30% cùng fail một level?
- **Vì sao quan trọng:** Confusion còn tệ hơn khó, vì nó phá flow ngay lập tức.
- **Hành động:**
  - Confusion ở level 1–5 ⇒ sửa ngay UI/FX/goal.
  - Xuất hiện sau level 15 ⇒ chấp nhận được, coi như thử thách.

## 6. Organic Level Continuation
- **Target:** >80%.
- **Ý nghĩa:**
  - <70% ⇒ Level thiếu liên kết.
  - 70–80% ⇒ Flow chấp nhận được.
  - >80% ⇒ “One more level” hoạt động.
  - >85% ⇒ Momentum cực tốt.
- **Vì sao quan trọng:** Đo “can’t stop” factor của loop.
- **Hành động:**
  - <75% ⇒ tease level kế tiếp (preview mechanic, reward).
  - >80% ⇒ progression ổn, tập trung nội dung mid-game.

## 7. D1 Retention (>=1.000 installs)
- **Target:** >40%.
- **Ý nghĩa:**
  - <30% ⇒ Vấn đề cốt lõi, cân nhắc kill.
  - 30–35% ⇒ Cần iterate mạnh.
  - 35–40% ⇒ Chấp nhận được, tiếp tục tối ưu.
  - >40% ⇒ Có thể greenlight soft launch.
  - >45% ⇒ Tiềm năng hit.
- **Vì sao quan trọng:** Tín hiệu tối thượng trước khi bơm UA lớn.
- **Hành động:**
  - <35% ⇒ sửa core loop và content early game.
  - 35–40% ⇒ nâng onboarding, thêm meta hứng thú.
  - >40% ⇒ chuẩn bị kế hoạch soft launch.

---

### Cách sử dụng
1. **Thu thập ngay sau 1.000 installs đầu tiên.** Không chờ thêm nội dung nếu metric đỏ.
2. **Nhìn trend, không chỉ snapshot.** D0 dài nhưng D1 tụt ⇒ investigate day 1 friction.
3. **Đính kèm video/screen.** Mỗi insight nên có minh họa, giúp debate nhanh hơn.

> “Trust early data. Đừng hy vọng thêm content sẽ cứu core loop. Nếu level 10 đã gãy, level 100 cũng gãy.”

### Bạn đang đo gì?
- Metric nào làm bạn bất ngờ nhất? D0 session length hay retry rate?
- Bạn có thêm chỉ số sớm nào khác (ví dụ: puzzle solve hint usage, economy delta)?
- Chia sẻ trong repo/Slack để cả team học lẫn nhau.

### Liên kết đề xuất
- [Playtest Framework](./playtest-framework.md) – thiết lập telemetry và survey để lấy dữ liệu trên.
- [Core Loop Mastery](./core-loop-mastery.md) – nếu metric đỏ, quay lại chỉnh fantasy + loop.