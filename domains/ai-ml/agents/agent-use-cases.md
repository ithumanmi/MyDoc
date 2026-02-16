# 💼 AI Agent Use Cases: Ứng dụng Thực chiến

> [← Back to AI/ML Roadmap](../README.md)

Đừng chỉ đọc lý thuyết. Hãy xem các Agent đang kiếm tiền như thế nào.

---

## 1. Coding Assistant (Trợ lý Code)

Không chỉ là Copilot (Gợi ý dòng code). Agent có thể tự động sửa lỗi và refactor cả Project.

### **Quy trình:**
1.  **Analyze:** Đọc toàn bộ file code trong repo. Hiểu cấu trúc Project.
2.  **Plan:** Lên kế hoạch sửa lỗi (Ví dụ: Thêm hàm check null, Viết unit test mới).
3.  **Execute:** Tự động sửa file code.
4.  **Verify:** Chạy test case để đảm bảo code chạy đúng.

---

## 2. Customer Support (Hỗ trợ Khách hàng)

Thay thế nhân viên trực chat 24/7. Không biết mệt mỏi.

### **Cơ chế RAG (Retrieval Augmented Generation):**
1.  Khách hỏi: "Chính sách đổi trả hàng như thế nào?"
2.  **Agent Search:** Tìm kiếm trong tài liệu nội bộ (Knowledge Base).
3.  **Answer:** Trả lời dựa trên thông tin tìm được.
4.  **Escalate:** Nếu câu hỏi quá khó -> Chuyển cho nhân viên thật xử lý.

---

## 3. Personal Shopper (Trợ lý Mua sắm)

Tìm deal ngon nhất trên Internet.

### **Quy trình:**
1.  **User Request:** "Tìm cho tôi iPhone 15 Pro Max giá rẻ nhất."
2.  **Search Agent:** Quét các trang TMĐT (Shopee, Lazada, Tiki, CellphoneS).
3.  **Filter:** Lọc ra các sản phẩm chính hãng (Mall), còn hàng.
4.  **Compare:** So sánh giá + khuyến mãi + phí ship.
5.  **Report:** Trả về bảng so sánh chi tiết kèm link mua hàng.

---

## 4. Market Research (Nghiên cứu Thị trường)

Tự động tổng hợp tin tức và viết báo cáo.

### **Quy trình:**
1.  **Topic:** "Phân tích xu hướng AI năm 2024."
2.  **Search:** Tìm kiếm các bài báo uy tín (TechCrunch, TheVerge, Papers).
3.  **Summarize:** Tóm tắt nội dung chính của từng bài.
4.  **Synthesize:** Tổng hợp thành một báo cáo hoàn chỉnh (Markdown/PDF).
5.  **Analyze:** Đưa ra nhận định cá nhân về xu hướng (Bullish/Bearish).
