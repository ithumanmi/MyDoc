# ⚠️ Common Data Biases & Antidotes

| Bias | Dấu hiệu | Tình huống mẫu | Cách xử lý |
| --- | --- | --- | --- |
| **Confirmation Bias** | Chỉ tìm insight khớp giả định | Marketing chỉ chọn channel đã yêu thích | Bắt buộc trình bày cả giả thuyết đối lập, peer review |
| **Selection Bias** | Dataset không đại diện | Survey chỉ lấy khách hàng trả lời email | Kiểm tra coverage, bổ sung weighting, thu thập thêm |
| **Survivorship Bias** | Bỏ qua trường hợp thất bại | Phân tích chỉ người dùng còn lại sau 90 ngày | Bao gồm dữ liệu churn, so sánh cohort |
| **Simpson’s Paradox** | Xu hướng đảo ngược khi gộp nhóm | Conversion tổng tăng nhưng từng khu vực giảm | Luôn kiểm tra subgroup, dùng pivot/cube |
| **Availability Bias** | Ra quyết định dựa trên ví dụ nổi bật | Nhắc tới một sự cố lớn → áp dụng cho tất cả | Đánh giá baseline và phân bố, không dựa vào outlier |
| **P-hacking** | Chạy nhiều test cho đến khi ra kết quả đẹp | Thử 20 biến AB cho tới khi p < 0.05 | Đặt giả thuyết trước, chỉnh p-value (Bonferroni) |
| **Data Freshness Bias** | Dựa vào số liệu lỗi thời | Báo cáo ghi “Last updated 2022” | Ghi timestamp, auto-refresh, nhắc nhở kiểm tra |

## Checklist phòng tránh

1. **Source Audit:** Ghi rõ nguồn, thời gian cập nhật, mức tin cậy.
2. **Experiment Hygiene:** Pre-register giả thuyết, metric, guardrail.
3. **Stakeholder Review:** Trình bày kết quả với đội khác để kiểm tra blind spot.
4. **Explainability:** Giải thích bằng văn bản/slide tại sao insight hợp lý, giả định nào còn yếu.
5. **Documentation:** Lưu lại quyết định, dữ liệu sử dụng trong repo/Notion.

## Habits giúp giảm bias

- Viết “bias log” mỗi khi phát hiện sai lệch trong dự án.
- Khi đọc dashboard, hỏi: *“Nếu số này sai 20%, mình xử lý thế nào?”*.
- Thực hành red-team/blue-team: một người tìm insight, người kia cố gắng phản bác.

> 🧭 *Reminder:* Dữ liệu không tự động khách quan; Độ chính xác phụ thuộc cách thu thập, phân tích và quyết định của con người.