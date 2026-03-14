# Primary Research 101 (Interview & Survey)

## Khi nào dùng & chọn phương pháp
- **Chưa có dữ liệu thị trường đáng tin** hoặc cần hiểu động cơ/hành vi sâu → ưu tiên **interview (qual)**.
- **Cần test nhanh giả thuyết / thông điệp** trước build → phỏng vấn định tính + survey nhẹ để đo ưu tiên.
- **Cần số liệu định lượng nhỏ** (không phải census) để ưu tiên tính năng → **survey** 3-5 phút.
- **Secondary research đủ?** Nếu đã có data công khai/tin cậy (report, analytics) thì **secondary** trước, primary chỉ để lấp gap.

## Quy trình rút gọn
1) **Xác định mục tiêu**: 3-5 decision questions (“người dùng trả tiền vì A hay B?”).
2) **Chọn phương pháp**: interview để hiểu “tại sao”; survey để đo “tỷ lệ/ưu tiên”.
3) **Thiết kế công cụ**:
   - **Interview**: script bán cấu trúc; hỏi hành vi quá khứ (Mom Test); 30-45 phút; tránh bán hàng.
   - **Survey**: ≤ 10 câu, 3-5 phút; tránh leading; randomize order; bắt buộc câu chính.
4) **Tuyển mẫu**: kênh đúng ICP; quota tối thiểu; ghi rõ nguồn; tránh bias kênh.
5) **Thu thập & ghi chép**: record (có consent), note hành vi, không hứa hẹn tính năng.
6) **Phân tích nhanh**: mã hóa chủ đề (themes), đếm tần suất; survey tính tỷ lệ, ưu tiên top 3.
7) **Ra quyết định**: mapping insight ↔ decision questions; log “chọn X vì insight Y”.

## Interview (Qual)
- **Cỡ mẫu**: 5-8/segment đủ để bão hòa chủ đề (thematic saturation).
- **Tuyển**: warm intro, cộng đồng niche, panel (UserTesting/PlaytestCloud); B2B: outbound nhẹ (LinkedIn/cold email) + referral.
- **Bias cần tránh**: leading, selling, confirmation bias.
- **Lưu ý**: hỏi hành vi đã xảy ra; ghi quote thực; tag theo pain/gain/JTBD/willingness-to-pay.

## Survey (Quant nhỏ)
- **Mục tiêu**: đo ưu tiên, tỷ lệ, không thay thế census.
- **Cỡ mẫu gợi ý**: 50-200 để nhìn khuynh hướng; nếu segment nhỏ có thể 30-50 pilot.
- **Thiết kế**:
  - Screening lọc đúng ICP.
  - Câu định lượng: Likert, ranking; tránh câu kép và leading.
  - Random hóa đáp án; attention check nhẹ; giới hạn 3-5 phút.
- **Bias cần tránh**: self-selection (kênh tuyển), order bias, wording bias.

## Tool gợi ý
- **Survey**: Google Forms, Typeform (logic), native in-product survey.
- **Interview**: Zoom/Meet (record), Notion/Sheets để tag theme, Grain/Fathom/Fireflies (auto-transcript).

## Phân tích nhanh
- **Interview**: thematic coding (pain, workaround, WTP); heatmap tần suất theo segment.
- **Survey**: tỷ lệ %, trung vị; cắt theo segment (new vs power user, geo).
- **Quyết định**: chuyển insight thành yêu cầu sản phẩm, thông điệp marketing, ưu tiên backlog.

## Checklist
- [ ] Mục tiêu rõ ràng (decision questions)
- [ ] Script/Survey ≤ 10 phút, không leading
- [ ] Tuyển đúng ICP, ghi nguồn kênh
- [ ] Consent + lưu trữ dữ liệu an toàn
- [ ] Bản tóm tắt 1 trang: ai được hỏi, insight chính, quyết định gì

## Template nhanh
- **Interview invite:** “Mình đang phỏng vấn 20-30 phút về cách bạn làm X, tặng voucher $10 cảm ơn thời gian của bạn.”
- **Survey open:** “Survey 3-5 phút cho người đang dùng công cụ X/Y; có quà nhỏ cho 50 bạn đầu tiên.”

---

> Xem thêm: [User Research & Persona](./user-research-persona.md) để gắn insight vào persona/segment.