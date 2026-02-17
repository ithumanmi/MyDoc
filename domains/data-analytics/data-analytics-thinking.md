# 🧠 Data Analytics Thinking: Tư Duy Phân Tích Dữ Liệu

> [← Back to Data Analytics Roadmap](./README.md)

## Tại sao Tư duy quan trọng hơn Công cụ?
Biết dùng SQL hay Python chỉ giúp bạn lấy được dữ liệu. Nhưng **Tư duy Phân tích (Analytics Thinking)** mới giúp bạn biết cần lấy dữ liệu gì và dùng nó để làm gì.

> *"If you torture the data long enough, it will confess to anything."* - Ronald Coase

---

## 1. Quy trình 6 bước (Google Data Analytics Framework) 🔄
Đừng bao giờ nhảy vào phân tích ngay. Hãy tuân thủ quy trình:

1.  **Ask (Đặt vấn đề):** Xác định rõ câu hỏi kinh doanh. (VD: Tại sao doanh số giảm?)
2.  **Prepare (Chuẩn bị):** Thu thập dữ liệu cần thiết. (Dữ liệu bán hàng, marketing, kho...)
3.  **Process (Xử lý):** Làm sạch dữ liệu (Clean), xử lý lỗi, định dạng lại.
4.  **Analyze (Phân tích):** Tìm kiếm mẫu hình (Patterns), xu hướng (Trends), mối quan hệ.
5.  **Share (Chia sẻ):** Trực quan hóa (Visualize) và kể chuyện (Storytelling).
6.  **Act (Hành động):** Đưa ra đề xuất giải pháp dựa trên insight.

---

## 2. Nghệ thuật đặt câu hỏi (Art of Asking Questions) ❓
Một Data Analyst giỏi là người biết đặt câu hỏi hay.

### 4 Loại câu hỏi phân tích:
1.  **Descriptive (Mô tả):** *Chuyện gì đã xảy ra?* (Doanh thu tháng trước là bao nhiêu?)
2.  **Diagnostic (Chẩn đoán):** *Tại sao nó xảy ra?* (Tại sao doanh thu giảm? Do Marketing hay do Sản phẩm?)
3.  **Predictive (Dự báo):** *Chuyện gì sẽ xảy ra?* (Doanh thu tháng tới sẽ là bao nhiêu?)
4.  **Prescriptive (Đề xuất):** *Chúng ta nên làm gì?* (Có nên chạy khuyến mãi không?)

---

## 3. Các bẫy tư duy cần tránh (Logical Fallacies) ⚠️

### Correlation != Causation (Tương quan không phải Nhân quả)
*   *Ví dụ:* Số người ăn kem tăng -> Số vụ chết đuối tăng.
*   *Kết luận sai:* Ăn kem gây chết đuối.
*   *Sự thật:* Cả hai đều tăng do trời nóng (Biến thứ 3 - Confounding Variable).

### Survivorship Bias (Thiên kiến kẻ sống sót)
*   *Ví dụ:* Phân tích những startup thành công để tìm công thức thành công.
*   *Lỗi:* Bỏ qua hàng ngàn startup thất bại cũng làm y hệt nhưng chết.

### Simpson's Paradox (Nghịch lý Simpson)
*   *Ví dụ:* Xu hướng chung cho thấy A tốt hơn B, nhưng khi chia nhỏ dữ liệu ra từng nhóm thì B lại tốt hơn A.
*   *Bài học:* Luôn nhìn dữ liệu ở nhiều góc độ (Granularity).

---

## 4. Data Storytelling: Kể chuyện bằng dữ liệu 📖
Insight không tự nói lên lời. Bạn phải là người phiên dịch.
*   **Context (Bối cảnh):** Cho người nghe biết tại sao họ cần quan tâm.
*   **Visuals (Hình ảnh):** Chọn biểu đồ đúng (So sánh -> Bar chart, Xu hướng -> Line chart).
*   **Narrative (Cốt truyện):** Dẫn dắt từ Vấn đề -> Nguyên nhân -> Giải pháp.

👉 **[Mẫu thực hành: Data Analysis Framework Template](./templates/data-analysis-framework.md)**
