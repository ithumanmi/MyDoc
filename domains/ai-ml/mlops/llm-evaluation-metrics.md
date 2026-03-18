# LLM Evaluation Metrics (Đánh giá chất lượng mô hình)

> [← Back to MLOps Roadmap](./README.md) | [Home](../../../README.md)

Khi ứng dụng LLM (chatbot, RAG) từ bản prototype chuyển lên Production, câu hỏi lớn nhất của sếp là: *"Trả lời nghe có vẻ hay đấy, nhưng làm sao biết nó đúng 100% hay đang bịa chuyện (Hallucination)?"*.

Việc "nhìn bằng mắt thường" vài trăm câu là vô ích. Ta cần hệ thống chấm điểm định lượng (Quantitative Evaluation). Bài viết này mô tả các ma trận và framework chấm điểm MLOps cho LLM (LLMOps).

---

## 📉 1. Tại Sao Metrics Truyền Thống Của MLOps Lại Thất Bại?

Ở Machine Learning cổ điển, ta dùng F1-Score, RMSE, hay Accuracy. Có một Đáp Án Đúng duy nhất.
Nhưng với LLM, "Tóm tắt bài viết này" có 1000 cách tóm tắt đúng khác nhau.
Các chỉ số NLP truyền thống như **BLEU** hay **ROUGE** (so khớp từ vựng) cũng thất bại thảm hại, vì nó phạt mô hình chỉ vì AI dùng từ đồng nghĩa, dù ngữ nghĩa là Hoàn Toàn Chính Xác.

---

## 🎯 2. Phương Pháp Chấm Điểm "LLM-as-a-Judge" (Dĩ Độc Trị Độc)

Giải pháp tốt nhất hiện tại: **Dùng một mô hình siêu thông minh (như GPT-4o, Claude 3.5 Sonnet) để đóng vai Trọng Tài, chấm điểm câu trả lời của hệ thống ứng dụng.**

Trong pipeline CI/CD, sau khi RAG của bạn sinh ra 100 câu trả lời test, ta đổ 100 tổ hợp (Câu hỏi, Document Ngữ Cảnh, Câu Trả Lời) vào GPT-4o và bắt nó chấm dựa trên thang điểm 1-5 theo 3 quy tắc vàng dưới đây (Được tiêu chuẩn hóa bởi rủi ro RAG).

---

## 📐 3. Bộ Chỉ Số Đánh Giá Chuẩn Công Nghiệp (Triad Metrics)

Được phổ biến bởi framework TruLens / RAGAS. Mọi pipeline LLM đều phải đo 3 cạnh tam giác này:

### 3.1. Context Relevance (Độ Liên Quan Của Ngữ Cảnh)
*   **Trọng tâm:** Chấm điểm hệ thống Retrieval (Vector Database) của bạn có lôi Nhầm Rác lên hay không?
*   **Prompt Trọng Tài:** "So sánh Câu Hỏi (Query) này và Đoạn Văn Bản (Retrieved Context) này. Đoạn văn này có chứa thông tin để trả lời câu hỏi kia không? Chấm điểm 0-10."

### 3.2. Groundedness / Faithfulness (Độ Trung Thực)
*   **Trọng tâm:** Chấm điểm LLM. Nó dựa vào Ngữ cảnh lấy về để trả lời, hay nó đang "Bốc Phét" kiến thức ngoài lề?
*   **Prompt Trọng Tài:** "Đọc câu trả lời này lập luận. Tất cả những facts (sự thật) trong câu trả lời có được Tìm Thấy, Backup y chang trong cái Ngữ Cảnh phía dưới hay không? Bịa 1 phát là cho 0 điểm ngay lập tức."

### 3.3. Answer Relevance (Độ Trọng Tâm Của Đáp Án)
*   **Trọng tâm:** Chấm Điểm Chất Lượng Output Trả Về user. Cấm nói vòng vo lang man.
*   **Prompt Trọng Tài:** Câu Trả lời này có "Đi thẳng vào vấn đề hỏi không". Nếu câu hỏi là Giá Bao nhiêu, câu trả lời là "Công ty tôi rất tốt" -> 0/10.

---

## 🛠️ 4. Các Framework Đánh Giá Uy Tín (Công Cụ MLOps)

*   **[Ragas](https://docs.ragas.io/):** Thư viện Python nổi tiếng nhất chuyên trị kiến trúc RAG pipeline. Đổ test data Pandas Dataframe vào, gọi `evaluate()`. Nó gọi GPT API và đẻ ngược ra 1 cái báo cáo Dashboard 5 chỉ số cho toàn bộ Database ảo.
*   **[TruLens](https://www.trulens.org/):** Code sạch đẹp, chuyên để Log trực tiếp vòng đời gọi App LangChain/LlamaIndex. Vẽ ra Dashboard TruLens Report trên máy Local xuất sắc.
*   **[DeepEval](https://github.com/confident-ai/deepeval):** Design theo phong cách PyTest. Bạn viết Unit Test như Coder truyền thống, check độ Toxicity (Độc hại / bias), check Tone (Giọng điệu), rồi chạy Github Actions CI block Pull Request lập tức nếu Trọng tài GPT chấm Pass-rate dưới 80%.

---

## 🚦 5. Checklist Vận Hành Production Của Một Team

> Khi bạn ra mắt mô hình:
> 1. Xây **Golden Dataset** (100-500 dòng ví dụ chuẩn cơm mẹ nấu do chuyên gia đánh chữ bằng tay - Lọc các câu hỏi khó nhất lịch sử cty).
> 2. Kẹp thẳng mã `DeepEval` vào Github Actions. Mỗi lần Merge code thay lệnh Prompt hệ thống -> CI/CD kích hoạt -> Gọi App test lại 500 dòng kia -> Ra Report Groundedness.
> 3. Giảm >10% score -> Fail PR, cấm merge code hệ thống ra ngoài (Automation Prevent Hallucination).
