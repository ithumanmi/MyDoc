## 🧩 Integration Layer — Stacking Mental Models (1–2 pages)

> Mục đích: biến mental models thành workflow hành động ngắn gọn. Ba lớp vấn đề: **Quyết định**, **Con người**, **Hệ thống**.

### 1) Vấn đề quyết định (Decision Surface)
- **FMS + Razors:** Fast Correction Mindset + Occam/Hanlon + Prior (chọn giả thuyết đơn giản, ưu tiên lỗi rẻ và dễ rollback).
- **Xác suất & EV:** Base rates, Expected Value, confidence bands; chọn phương án tối giản đủ an toàn.
- **Checklist triển khai:**
  1) Viết 2–3 giả thuyết cạnh tranh (simple vs robust).
  2) Đặt base rate & worst-case; thêm rollback path.
  3) Chốt phương án có EV dương và chi phí thử nghiệm thấp.

### 2) Vấn đề con người (Human Layer)
- **Psychology + Behavioral Econ + Stoicism:** Giảm bias/cảm xúc, thiết kế incentive rõ ràng.
- **Incentives / Opportunity Cost / Elasticity:** Kiểm tra động cơ, chi phí cơ hội và độ nhạy phản hồi (elasticity) trước khi chọn giải pháp.
- **Checklist triển khai:**
  1) Liệt kê stakeholders + incentive của từng bên.
  2) Đánh giá bias chính (loss aversion, sunk cost, overconfidence).
  3) Thiết kế incentive alignment và kênh phản hồi ngắn.

### 3) Vấn đề hệ thống (System Layer)
- **Feedback loops + Biology/Entropy + Second-order effects:** Chống khuếch đại lỗi, bảo toàn năng lượng/hạ tầng, tránh externalities.
- **Guardrails:** Rate limits, circuit breakers, fallback tiers, sampling giám sát.
- **Checklist triển khai:**
  1) Vẽ luồng input→output, đánh dấu loop khuếch đại.
  2) Thêm cơ chế giảm chấn (throttle, backpressure, cache TTL).
  3) Định nghĩa health metrics + chu kỳ review (vd: weekly ops review).

### Cách dùng nhanh (3 bước)
1) Xác định loại vấn đề (Decision / Human / System).
2) Áp checklist tương ứng, ghi 3 bullet hành động.
3) Chạy thử nhỏ (cheap test), review sau 1–2 chu kỳ; cập nhật checklist.

> Gợi ý mở rộng: thêm ví dụ cụ thể cho dự án đang làm (RAG chatbot, MLOps pipeline, multi-agent system) để biến thành SOP nội bộ.