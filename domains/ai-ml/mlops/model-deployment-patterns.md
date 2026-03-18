# Model Deployment Patterns (Kiến Trúc Triển Khai Thực Chiến)

> [← Back to MLOps Roadmap](./README.md) | [Home](../../../README.md)

Deploy 1 model MNIST trên Flask app cho thầy giáo chấm thi là 1 chuyện. 
Deploy Llama 3 8B cho 10,000 công nhân viên xài mà không bị crash Out-Of-Memory, hay Update thuật toán Khuyến mãi (Recommendation Model) trực tiếp lên sàn TMĐT mùa Sale mà không sập Web, đó gọi là **Model Deployment Patterns**.

Thuật ngữ của thế giới DevOps / MLOps Software Architecture.

---

## 🚦 1. Các Chiến Lược Phát Hành (Release Strategies)

Đừng bao giờ update/chọn Model mới rồi đút nóng đè Model cũ `(In-place Deployment)`. Thảm họa rủi ro 100%.

### 1.1. Blue/Green Deployment (Xanh/Chín Toàn Diện)
*   **Khái niệm:** Có 2 môi trường giống hệt nhau về Hạ tầng GPU Server. Môi trường Blue (Cũ) đang chạy 100% khách hàng. Bạn deploy Model Ver 2.0 lên môi trường Green (Mới). Đảm bảo Green chạy chơn chu ngon lành, **Router Load Balancer bật công tắc cái cạch**: Chuyển luồng 100% User từ Môi trường cũ sang Môi trường Mới.
*   **Lợi ích:** Rollback (Thoái lùi) cái một (Bật công tắc lại). Zero downtime (Không thời gian chờ). Tốn X2 tiền server duy trì tạm thời vài tiếng thôi.

### 1.2. Canary Release (Chim Yến Dò Mìn)
Từ khóa này bắt nguồn từ việc chôn một con chim Yến trong lồng mỏ than. Nếu chim nghẹt thở chết, mỏ than có khí độc.
*   **Khái niệm:** Model Ver 2.0 mới update lên, lỡ dính phốt phân biệt chủng tộc do Code Data lỗi thì sao? Dùng Load Balancer điều phối: **Đẩy chỉ 5% traffic Random (Hoặc nội bộ IP công ty) vào Model Ver Mới**. 95% khách hàng còn lại xài hàng Ver cũ.
*   **Lợi ích:** Test phản ứng kinh doanh thực (A/B Testing Error Rate). Nếu hệ thống Report Log mượt, từ từ nâng volumn lên 10% -> 50% -> 100%.

### 1.3. Shadow Deployment (Chiến Binh Đóng Thế)
Xịn xò nhất cho Machine Learning Trading (Trái tim tài chính).
*   **Khái niệm:** Model Ver 2.0 nằm im đó gọi là Shadow. Backend hứng 100% Traffic mua hàng. Backend tự Copy nhân đôi cái Gói Packet Request: **Đẩy 1 gói cho Model Hiện tại Real (Phản hồi lại Khách), Gói bản sao nhét vào Model Shadow Mới (Tính toán ra Dự Đoán, nhưng Vứt đi không hiện lên, chỉ Âm thầm Lưu vào Log File Server).**
*   **Lợi ích:** Kỹ sư MLOps cầm cái Dashboard so sánh Log 1 tuần ròng rã. Khảo sát Độ Chính Xác Model mới ngấm ngầm ngoài Đời thực mà KHÔNG tác động tới bất kỳ user/tiền thật nào ngoài đời.

---

## 🚀 2. So Sánh Các Cỗ Máy Lõi Serving (LLM Inference Engines)

Kế tiếp về Backend Architecture. Nếu bạn Self-Host Llama 3 trên Con T4 Google Cloud rẻ bèo, Code PyTorch bình thường của bạn chỉ chịu nổi 2 người Nhắn Tin Song Song (Batching lỗi, Memory Fragmentation cháy). Đây là các Engine tối ưu Serving Mức thấp:

| Serving Engine | Của Ai | Tại Sao Phải Xài Nó (Superpower) | Nhược điểm |
| :--- | :--- | :--- | :--- |
| **vLLM** | ĐH Berkeley Open-source | Tái kiến trúc PagedAttention đỉnh cao mạng xã hội. Chia bộ nhớ VRAM thành các khối OS nhỏ, đẩy tốc độ Throughput (Lưu lượng xử lý Token) **gấp 2-4 Lần** thư viện cũ HuggingFace. Support mô hình LLM đại chúng nhất. Lựa chọn tiêu chuẩn SaaS 2026. | Đóng gói tuỳ chỉnh thuật toán quá mới thì support chậm. |
| **TGI (Text Generation Inference)** | HuggingFace | Sức mạnh native từ Huggingface, support Tensor Parallelism tốt để xẻ LLM bự thành nhiều GPU Node chia tải. | License lằng nhằng vụ Commercial use cho hãng cực Bự. |
| **Triton Inference Server** | NVIDIA (Cha Đẻ Của Card Màn Hình) | Quái vật hạng nặng. Không ngán LLM, CV ảnh, hay Âm Thanh. Nó tối ưu tới tận chân Răng nhân xử lý Cuda Core. Dynamic Batching siêu việt dành cho Traffic Scale chục Triệu Request/s (Shopee/Grab). | Tổ ong học thuật rối nùi. Cần Engineer Master học Config file nặng não. |

> **Thực chiến cho Startup / Indie Hacker SaaS AI:** Đóng Code LLM mô hình vô `vLLM` Docker image. Deploy lên RunPod/Vast.ai, mở Endpoint tương thích với chuẩn OpenAPI lên gọi như ChatGPT. Finish.
