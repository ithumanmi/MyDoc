# Multimodal AI Agents: Trợ Lý Đa Phương Thức 

> [← Back to Agents Module](../README.md) | [Home](../../../README.md)

Khi các kiến trúc LLM tiến hóa thành **LMMs** (Large Multimodal Models - ví dụ như GPT-4o, Gemini 1.5 Pro, Claude 3.5 Sonnet), kỷ nguyên của các Agents chỉ biết "đọc và phun text" đã kết thúc.
Tương lai thuộc về **Multimodal Agents**, những hệ thống tự trị có khả năng Nhìn (Vision), Nghe (Audio), và Tương Tác Cảm Nhận Vật Lý (Robotics/Computer Use).

---

## 👁️ 1. Vision Agents: Agent biết Nhìn

Thay vì mỏi tay mô tả giao diện lỗi cho GPT, bạn ném vào một screenshot và Agent tự hiểu. Khả năng "Nhìn màn hình" (Screen parsing) là chìa khóa thăng hạng.

### Computer Use (Điều Khiển Máy Tính Tự Động)
Một trong những bước tiến vĩ đại nhất của Claude 3.5 là khả năng "Sử Dụng Máy Tính".
*   **Trình tự hoạt động:**
    1. Agent yêu cầu chụp ảnh màn hình hiện tại.
    2. Vision Model quét hình ảnh, định vị trí các bounding boxes ở tọa độ pixel chính xác của các Nút, Input Text, Menu (Nhận dạng UI elements).
    3. Trả ra Tool Call: `click_mouse(x=345, y=510)` hoặc `type_text(element_id="search_box", text="...")`.
    4. Hệ điều hành thực thi hành động đó qua thư viện giả lập (như PyAutoGUI hoặc Puppeteer).
    5. Cứ thế tạo nên vòng lặp tự động đóng/mở App, bấm, kéo thả như con người!

### Visual Document Analysis (RAG Đa Phương Thức)
Nếu bạn đẩy một file PDF đầy biểu đồ tài chính vào chuẩn Text-RAG, cái bảng sẽ bị "nghiền" thành rác.
*   **Thực thi:** Dùng Vision Model (như ColPali) mã hóa toàn bộ hình ảnh của trang giấy (nguyên vẹn từng pixel) ra thành Embedding. Khi tìm kiếm, nó lục ở Level hình ảnh, gọi bức hình đó lên và cho LMM đọc trực tiếp. Nó có thể trả lời "Cái cột màu xanh lam ở góc phải năm 25 là bao nhiêu tỷ".

---

## 🎧 2. Audio/Voice Agents: Voice-to-Voice Trực Tiếp

Các dự án Bot điện thoại đời cũ sử dụng Pipeline ASR-LLM-TTS (Voice->Text, Text->LLM->Text, Text->Voice). Pipeline này cực chậm, mất 3-4 giây, và "rơi mất linh hồn âm thanh" (sự ngắt giọng, cường độ, cảm xúc người gọi).

### Cuộc Cách Mạng Native Voice-to-Voice
Mô hình như GPT-4o Realtime API hoặc Gemini Flash xử lý **âm thanh đầu vào (Audio In) trực tiếp thành âm thanh đầu ra (Audio Out)** — bỏ qua khâu dịch ra chữ.
*   **Độ trễ (Latency):** < 300ms (giống với tốc độ đàm thoại qua điện thoại bình thường).
*   **Hiểu được "Tần số":** Agent có thể thay đổi giọng điệu nếu người nói đang khóc, đang hoảng loạn, đang trêu đùa, huýt sáo.
*   **Ứng dụng:** Customer Support đa tầng, Luyện tập phỏng vấn/ngoại ngữ, Trợ lý Voice AI điều khiển trên rảnh tay trong vận tải/Logistics.

### Kỹ thuật kết nối (WebRTC)
Để đạt <300ms, bạn không thể gửi request qua HTTP thông thường được. Developer lập trình Audio Agent hiện nay dùng chuẩn **WebRTC** để mở đường truyền audio sinh học 2 chiều liên tục (như Zoom/Google Meet) giữa Browser user và Server của AI.

---

## 🧠 3. Thiết kế Vòng Suy Luận (Reasoning Cycle) Của Multimodal Agent

Đưa vào Mắt, Tai, nhưng Não bộ phân bổ như thế nào? Cấu trúc của 1 Multimodal Agent xịn trong Production:

1.  **Sensory Input Layer:** Thu thập Microphone, Webcam snapshot, Screen recording streams theo Window/Batch.
2.  **Multimodal Embedder:** Biến tất tật (Video chunk 3s, Bức ảnh 2MB, Đoạn Audio 10s) vào chung 1 "Không Gian Vector Liên Hiệp".
3.  **Core LMM (Brain):** GPT-4o phân tích: "Dựa vào ảnh màn hình này [Image], và câu nói bực bội của user là [Audio], tôi hiểu giao diện đang bị đơ ở nút X".
4.  **Action Layer (Hands):** LMM phản ra API call. Framework điều khiển trỏ chuột tới X, nhấp chuột, hoặc sinh ra đoạn Voice xin lỗi xoa dịu khách hàng.
5.  **Feedback/Reflection:** Sau khi Action, chụp ảnh màn hình lại, so sánh. "Nút X đã click nhưng Popup lại đè lên! Cần hủy và click chéo". (Tự phán đoán khi lỗi).

---

## 💡 4. Ứng Dụng Thực Chiến (Use Cases)

> [!TIP]
> **Hướng tiếp cận Multimodal khi xây ứng dụng:**
>
> ✓ Xây AI QA Tester (Test Bug phần mềm): Bật video quay lại thao tác máy người dùng đang test App, đẩy vào cho Vision Agent, nó tự soi ra cái App bị overflow UI ở Mobile.
> ✓ Xây AI Bán Hàng Trực Tiếp (Voice Sales): Kết hợp WebRTC Voice Agent kết nối với kho hàng ERP của bạn (Tool Calling) qua điện thoại 100% tự động đàm phán chốt đơn.
> ✓ AI Camera Giám Sát: Vision LLMs kết nối stream IP Camera. Prompt: "Gửi ảnh vào Slack nếu thấy có xe container biển lạ tiếp cận kho hàng phía bắc."
