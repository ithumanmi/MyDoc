# 🛡️ Responsible AI: Sử Dụng Generative AI Có Trách Nhiệm

> **Nguyên tắc cốt lõi:** Lợi ích của người dùng = Kết quả tốt nhất cho ứng dụng của bạn.
> Generative AI có thể tạo ra giá trị khổng lồ, nhưng giá trị đó có thể mất đi trong chớp mắt nếu không được sử dụng có trách nhiệm!

---

## 1. Tại Sao Phải Ưu Tiên Responsible AI?
*   **Giám sát tác động:** Chỉ có "ý định tốt" là chưa đủ. Cần có hệ thống giám sát thực tế.
*   **Phòng ngừa rủi ro:** Không ai cố tình xây dựng ứng dụng tồi, nhưng rủi ro vẫn xảy ra nếu thiếu cơ chế kiểm soát phù hợp.

## 2. Ba Rủi Ro Tiềm Ẩn Chính ⚠️

### 1️⃣ Ungrounded Outputs (Kết quả không có căn cứ)
Thường gọi là **Hallucinations** (Ảo giác AI) - khi AI bịa đặt thông tin.
*   **Hậu quả nhẹ:** Câu trả lời vô nghĩa, kỳ quặc, gây cười.
*   **Hậu quả nghiêm trọng:**
    *   Thông tin sai sự thật lan truyền trong hệ thống.
    *   Tư vấn y tế/pháp lý sai lệch.
    *   Mâu thuẫn nội dung trong cùng một câu trả lời.

### 2️⃣ Harmful Content (Nội dung có hại)
Các mô hình ngôn ngữ lớn (LLM) có thể bị lợi dụng để tạo ra:
*   Hướng dẫn tự gây hại (self-harm).
*   Nội dung kỳ thị, thù ghét (hate speech).
*   Hướng dẫn thực hiện hành vi bất hợp pháp (cyberattack, chế tạo vũ khí...).

### 3️⃣ Lack of Fairness (Thiếu công bằng)
> "Cuộc sống không công bằng, nhưng hệ thống AI phải công bằng!"
*   **Yêu cầu:** Không có thiên kiến (bias) và phân biệt đối xử.
*   **Biểu hiện:** Không thiên vị bất kỳ nhóm người nào (giới tính, chủng tộc, tôn giáo...). Đặc biệt quan trọng trong các ứng dụng tuyển dụng, cho vay, hoặc tạo hình ảnh con người.

---

## 3. Sáu Nguyên Tắc Responsible AI (Theo Microsoft) ⚖️

1.  **Fairness (Công bằng):** Hệ thống AI phải đối xử công bằng với tất cả mọi người.
2.  **Reliability & Safety (Đáng tin cậy & An toàn):** Hoạt động ổn định và an toàn trong mọi điều kiện.
3.  **Privacy & Security (Riêng tư & Bảo mật):** Bảo vệ dữ liệu người dùng tuyệt đối.
4.  **Inclusiveness (Toàn diện):** Phục vụ mọi đối tượng, kể cả người khuyết tật.
5.  **Transparency (Minh bạch):** Người dùng phải hiểu được cách hệ thống hoạt động và ra quyết định.
6.  **Accountability (Trách nhiệm giải trình):** Con người phải chịu trách nhiệm về hoạt động của hệ thống AI.

---

## 4. Quy Trình Triển Khai Responsible AI 📊

### BƯỚC 1: Đo Lường Rủi Ro (Risk Measurement)
Thực hiện **[Prompt Testing](./prompt-testing.md)** (Kiểm thử prompt) kỹ lưỡng:
*   **Đa dạng hóa:** Test cả "happy path" (trường hợp lý tưởng) và "adversarial path" (cố tình tấn công/gây lỗi).
*   **Quy trình:**
    *   *Thủ công:* Gửi từng prompt -> Đánh giá kết quả -> Hiểu hành vi mô hình.
    *   *Tự động:* Batch hàng loạt prompt -> Dùng tool đánh giá tự động (khi đã ổn định).

### BƯỚC 2: Bốn Lớp Giảm Thiểu Rủi Ro (Mitigation Layers)

#### 🔹 Layer 1: Model Level (Cấp độ mô hình)
*   **Chọn đúng mô hình:** Không phải lúc nào model mạnh nhất cũng tốt nhất. Chọn model phù hợp use-case.
*   **Fine-tuning:** Tinh chỉnh model với dữ liệu sạch để giảm bias.
*   **Parameters:** Điều chỉnh `temperature`, `top_p` để kiểm soát độ sáng tạo/ngẫu nhiên.

#### 🔹 Layer 2: Safety System (Hệ thống an toàn)
*   **[Content Filtering](./content-safety.md):** Bộ lọc đầu vào/đầu ra để chặn nội dung độc hại (Hate, Violence, Jailbreak).
*   **Monitoring:** Giám sát liên tục các chỉ số an toàn.

#### 🔹 Layer 3: Meta Prompts (System Prompts)
*   **Định hướng hành vi:** Dùng System Message để quy định rõ model được làm gì và không được làm gì.
*   **Grounding:** Sử dụng RAG (Retrieval-Augmented Generation) để buộc model trả lời dựa trên dữ liệu thật, giảm ảo giác.

#### 🔹 Layer 4: User Experience (Trải nghiệm người dùng)
*   **Transparency:** Thông báo rõ ràng "Bạn đang chat với AI".
*   **Constraints:** Giới hạn độ dài hoặc loại input người dùng có thể nhập.
*   **Feedback Loop:** Cho phép người dùng báo cáo câu trả lời sai/xấu.

---

## 5. Công Cụ Hỗ Trợ (Microsoft Stack) 🔧

### 1️⃣ Azure AI Content Safety
API giúp kiểm duyệt nội dung tự động:
*   **Text Analysis:** Phát hiện Hate, Violence, Self-harm, Sexual content.
*   **Prompt Shields:** Chặn Jailbreak attacks (cố tình bẻ khóa model).
*   **Groundedness Detection:** Kiểm tra xem câu trả lời có dựa trên nguồn tin cậy không.

### 2️⃣ Responsible AI Dashboard
"Bảng điểm sức khỏe" cho model:
*   Theo dõi tương tác thực tế với user.
*   Đánh giá performance theo thời gian (tránh model drift).

### 3️⃣ Prompt Flow
Công cụ Open-source để xây dựng và monitor luồng AI với 5 metrics quan trọng:
1.  **Coherence:** Mạch lạc.
2.  **Fluency:** Trôi chảy.
3.  **Groundedness:** Có căn cứ.
4.  **Relevance:** Liên quan đúng câu hỏi.
5.  **Similarity:** Độ tương đồng với các mẫu chuẩn.
