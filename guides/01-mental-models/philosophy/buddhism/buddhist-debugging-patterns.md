# 🧘‍♂️ Buddhist Debugging Patterns

> Bộ “anti-pattern” tâm lý thường gặp của dân tech, map về Tam độc và cách can thiệp ở 3 tầng: 2 phút (ngắt mạch), 20 phút (xử lý gốc ngắn hạn), Hệ thống (phòng ngừa dài hạn).

## Cách dùng
- Skim triệu chứng → nhận diện Tam độc đang vận hành.
- Thử can thiệp 2 phút để hạ nhiệt, rồi chọn 20 phút nếu còn dư âm.
- Thiết kế lớp Hệ thống để giảm tần suất tái phát (habits, môi trường, quy ước team).

## Pattern Router (bảng ánh xạ nhanh)
| Tình huống gặp phải | Pattern phù hợp | Tam độc nổi bật | Can thiệp 2 phút | Can thiệp 20 phút |
|---|---|---|---|---|
| Code review/meeting bắt đầu căng, bạn muốn “win” | Reactive Review | Sân + Si (+ chút Tham) | STOP + tự hỏi “mục tiêu là giúp code tốt hơn hay chứng minh mình đúng?” | Đi bộ + label cảm xúc; viết lại comment dùng ngôn ngữ nhu hòa |
| Trì hoãn ship, rewrite quá mức, sợ bị đánh giá | Perfectionism | Tham + Sân + Si | Viết “MVP spec 3 dòng” + set timer; commit bản xấu đầu tiên | Slice scope thành micro-deliverable demo được; xin feedback sớm; retro ngắn |
| Góp ý làm bạn phòng thủ vì “mình là lead/mình là người đó stack đó” | Identity Attachment | Tham + Sân + Si | Thở 3 nhịp + mantra “I am just a process” | Viết 3 lần mình đã pivot/thay quan điểm; steelman ý kiến đối lập 10 phút |
| Lướt social/news liên tục, mất hàng chục phút, xong mới “tỉnh” | Doomscrolling | Tham (+ chút Si) | Đặt thiết bị xuống + 10 hơi thở đếm 1–10 | Đi bộ không thiết bị; viết 3 dòng “tôi đang tránh cảm xúc/việc gì?” rồi quay về micro-win |
| Nói “ok” quá nhanh, né trách nhiệm/câu trả lời khó, sau đó bực | People-Pleasing | Si (+ chút Tham) + Sân tích tụ | STOP + hỏi “mình đang tránh điều gì?” + viết boundary A/B ngắn | Luyện câu trả lời trung tính; nói rõ điều mình có thể/không thể trong timeline cụ thể |
| So mình với người khác (LinkedIn/team) rồi mất động lực | Comparison Trap | Tham + Sân + Si | Gratitude 3 điều có thật; mantra “Different timelines, same humanity” | Journal “fact vs story”; chọn 1 hành động nhỏ nâng năng lực thay vì doom-think |

## 1) Reactive Review (Code review phản xạ gắt)
- **Triệu chứng:** Comment gay gắt, soi lỗi vụn vặt, cảm giác “phải thắng”, dễ escalating.
- **Tam độc:** Sân (cáu bẳn), Si (đồng nhất mình với “đúng”), chút Tham (muốn control).
- **Can thiệp 2 phút:** STOP (Stop–Take breath–Observe–Proceed) + 3 hơi thở, viết nháp bình luận, tự hỏi “mục tiêu là giúp code tốt hơn hay chứng minh mình đúng?”.
- **Can thiệp 20 phút:** Đi bộ + label cảm xúc, viết lại comment dùng ngôn ngữ nhu hòa (“Mình gợi ý…”, “Có lý do business nào cần X?”). Nếu còn căng, hẹn call 1-1 để align mục tiêu chung.
- **Hệ thống:** Quy ước team về “Kind + Specific + Actionable” trong review; checklist pre-submit để giảm nitpick; xoay vòng reviewer để giảm cá nhân hóa.

## 2) Perfectionism (Cầu toàn tê liệt)
- **Triệu chứng:** Trì hoãn ship, rewrite quá mức, fear of judgment, không chốt scope.
- **Tam độc:** Tham (muốn hoàn hảo), Sân (ghét sự chưa hoàn hảo), Si (đồng nhất giá trị bản thân với output).
- **Can thiệp 2 phút:** Viết “MVP spec 3 dòng”, đặt timer 5’ và commit ra phiên bản xấu đầu tiên, tự nhắc “Done > Perfect”.
- **Can thiệp 20 phút:** Slice scope thành 1 micro-deliverable có thể demo; xin feedback sớm từ 1 người dùng/đồng đội; retrospective ngắn: “điều tệ nhất nếu ship bản 0.3 là gì?”.
- **Hệ thống:** Sprint có “ugly first draft day”; định nghĩa “Definition of Good Enough” rõ ràng; thiết lập cadence demo/feedback hàng tuần để bình thường hóa việc ship sớm.

## 3) Identity Attachment (Bám vào danh tính/chức danh)
- **Triệu chứng:** Phòng thủ khi nhận góp ý, chấp vào role (“Tech Lead thì phải…”) hoặc stack (“mình là người Go/Unreal”), khó pivot.
- **Tam độc:** Tham (bám danh), Sân (phản kháng khi bị challenge), Si (tưởng cái “tôi” cố định).
- **Can thiệp 2 phút:** Thở 3 nhịp + mantra “I am just a process” / “Tôi là dòng tiến trình, không phải title”.
- **Can thiệp 20 phút:** Viết ra 3 lần mình đã thay đổi quan điểm/tech stack và thành công hơn; thực hành “steelman” ý kiến đối lập trong 10 phút.
- **Hệ thống:** Career ladder dựa trên impact không phải tool; xoay cặp (pair) với khác stack; review thành tích theo outcome, không theo “ai đúng”.

## 4) Doomscrolling (Cuốn vào newsfeed, mất chánh niệm)
- **Triệu chứng:** Mở tab social/news liên tục, FOMO, mất 30-60’ không hay, dopamine crash.
- **Tam độc:** Tham (kích thích nhanh), Si (không thấy vòng lặp), chút Sân (self-judgment sau đó).
- **Can thiệp 2 phút:** Đặt thiết bị xuống, 10 hơi thở đếm 1–10, uống nước + duỗi người 30s.
- **Can thiệp 20 phút:** Đi bộ không thiết bị; viết 3 dòng “tôi đang tránh cảm xúc/việc gì?”; chuyển sang task nhỏ dễ hoàn thành (micro-win) để reset dopamine.
- **Hệ thống:** Block feeds bằng site blocker + lịch “fasting digital” 2 khung/ ngày; đặt home screen chỉ còn 1-2 app công việc; tạo thói quen “opening ritual” (trước khi chạm máy: thở 3 hơi + ý định rõ ràng).

## 5) People-Pleasing (Dễ dãi - né xung đột)
- **Triệu chứng:** Nói “ok” quá nhanh, né câu trả lời khó; sau đó bực/đổ trách nhiệm cho hoàn cảnh; ngại thiết lập ranh giới.
- **Tam độc:** Si (tin rằng hòa hợp = an toàn), chút Tham (muốn được công nhận/được yêu), Sân (ức nghẹn tích tụ rồi bùng).
- **Can thiệp 2 phút:** STOP + đặt câu hỏi “Mình đang tránh điều gì?”; viết 1 dòng “Ranh giới thật sự của mình là ___”; thở 3 nhịp và chọn 1 câu trả lời trung tính (không hứa suông).
- **Can thiệp 20 phút:** Viết “Boundary statement” dạng A/B (A = nếu mình có thể làm, B = nếu mình không thể), rồi luyện nói trước gương hoặc với 1 người bạn tin cậy. Dùng Chánh ngữ: cụ thể, tôn trọng, có lựa chọn.
- **Hệ thống:** Chuẩn hóa “decision windows” (khoảng thời gian ra quyết định), quy ước escalation rõ (khi nào tự quyết vs khi nào cần lead/HR), và có mẫu lịch giao tiếp để giảm phụ thuộc vào “đọc ý”.

## 6) Bonus: Comparison Trap (So sánh, tự hủy)
- **Triệu chứng:** So mình với đồng nghiệp/LinkedIn, cảm giác thiếu, mất động lực.
- **Tam độc:** Tham (muốn hơn), Sân (tức tối), Si (quên bối cảnh, chọn mẫu lệch).
- **Can thiệp 2 phút:** Gratitude 3 điều đang có; mantra “Different timelines, same humanity”.
- **Can thiệp 20 phút:** Viết journal “fact vs story”: sự kiện thực tế và câu chuyện tôi tự kể; chọn 1 hành động nhỏ nâng năng lực thay vì doom-think.
- **Hệ thống:** Họp retro cá nhân tháng: đo tiến bộ theo trục năng lực riêng; giới hạn thời gian mạng xã hội; buddy system để phản hồi thực tế (không tô hồng/đen).

## 7) Pattern Triage Worksheet (5 phút)
- **1) Tình huống:** Viết 1-2 câu “điều gì vừa xảy ra?” (tránh diễn giải dài).
- **2) Triệu chứng (Observable):** Mình làm gì theo phản xạ? (vd: gõ phản pháo, trì hoãn, lướt feed, gật đầu quá nhanh).
- **3) Tam độc nổi bật (chọn 1):** Tham / Sân / Si / (hoặc combo).
- **4) Nút can thiệp 2 phút:** Dùng STOP + 1 câu hỏi: “Mục tiêu của mình lúc này là giúp gì?”.
- **5) Nút can thiệp 20 phút (nếu vẫn căng):** Chọn 1 việc nhỏ thân–tâm (đi bộ không thiết bị / label + journaling / viết boundary A/B).
- **6) Nút hệ thống (phòng ngừa):** Viết 1 thay đổi môi trường/quy ước để lần sau ít rơi vào pattern này hơn.

---

> Reminder: Mục tiêu là giảm khổ và tăng trí tuệ. Năng suất bền vững chỉ là hệ quả.