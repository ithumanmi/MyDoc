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

---

## 5. Notebook LM – Trợ lý ghi chú & học tập dựa trên dữ liệu riêng

Notebook LM của Google được thiết kế riêng cho việc tổng hợp kiến thức từ **chính dữ liệu bạn upload**. Khác với ChatGPT/Gemini (có thể trả lời lệch ngữ cảnh vì tra cứu Internet), Notebook LM cam kết: **“Không trích nguồn ngoài – chỉ trả lời từ dữ liệu của bạn.”**

### 🧩 Vấn đề & Giải pháp
*   **Vấn đề:** Người sáng tạo nội dung / giảng viên thường bị hỏi đi hỏi lại cùng một câu hỏi, dù thông tin đã có trong khóa học hoặc tài liệu nội bộ. Các AI chung chung hay trả lời sai vì lấy nguồn từ Internet.
*   **Giải pháp:** Notebook LM tạo một “sổ tay AI” chỉ đọc dữ liệu bạn cung cấp. Mọi câu trả lời đều dựa trên tài liệu đã được upload → đảm bảo chính xác, tiết kiệm thời gian.

### 🏢 Ứng dụng trong doanh nghiệp
*   **Onboarding nhân viên mới:** Upload SOP, hướng dẫn nội bộ → nhân viên hỏi gì AI cũng trả lời đúng theo quy trình công ty.
*   **Chăm sóc khách hàng:** Tạo chatbot FAQ bám sát tài liệu sản phẩm, giảm tải đội hỗ trợ.

### 🎓 Ứng dụng trong học tập
*   Upload slide/ebook → yêu cầu AI tóm tắt, tạo mind map, trích xuất flashcard.
*   Sinh câu hỏi ôn tập, quiz theo từng chương.

### ⚙️ Quy trình sử dụng
1.  **Sources:** Kéo thả tài liệu (PDF, Google Docs, transcript video...).
2.  **Chat:** Hỏi đáp tự nhiên, luôn được trích nguồn từ tài liệu.
3.  **Studio/Notes:** Tự động sinh các artefacts như outline bài giảng, brief, bảng ghi chú.

### ✨ Tính năng nổi bật
*   **Audio Overview:** Tạo bản tóm tắt bằng giọng nói.
*   **Study Guide / Brief Docs:** Sinh tài liệu học tập hoặc executive summary.
*   **Mind Map:** Xuất bản đồ tư duy trực quan.
*   **Tone & Length Controls:** Điều chỉnh phong cách trả lời (ngắn/gọn, hướng dẫn, phân tích chuyên sâu).

> 📌 **Điểm mấu chốt:** Notebook LM = “LLM chuyên biệt cho dữ liệu cá nhân/đội ngũ”. Dùng nó để tự động hóa việc trả lời câu hỏi lặp lại, tổng hợp giáo trình, hoặc hỗ trợ học tập theo tốc độ riêng.
