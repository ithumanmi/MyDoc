# 🎨 Generative AI: Sức mạnh của Sự sáng tạo (Level 6)

> [← Back to AI/ML Roadmap](../README.md)

GAN (Generative Adversarial Networks) từng là vua.
Nhưng Diffusion Models (Stable Diffusion, Midjourney) đã lật đổ ngai vàng và tạo ra cuộc cách mạng nghệ thuật AI.

---

## 1. Diffusion Models (Mô hình Khuếch tán)

**Nguyên lý:**
1.  **Forward Process (Phá hủy):** Thêm nhiễu (Noise) vào bức ảnh đẹp từ từ cho đến khi nó thành nhiễu trắng hoàn toàn.
2.  **Reverse Process (Khôi phục):** Dạy mô hình AI cách loại bỏ nhiễu từng chút một để phục hồi lại bức ảnh gốc.
3.  **Generation (Tạo mới):** Bắt đầu từ nhiễu trắng hoàn toàn -> Áp dụng Reverse Process -> Ra bức ảnh mới tinh chưa từng tồn tại.

### **A. Stable Diffusion (SD)**
*   Mã nguồn mở (Open Source). Chạy được trên PC cá nhân (VRAM 4GB+).
*   **Text-to-Image:** Gõ "A cat in space suit" -> Ra ảnh.
*   **Image-to-Image:** Vẽ phác thảo xấu xí -> Ra tranh sơn dầu tuyệt đẹp.
*   **ControlNet:** Kiểm soát dáng pose nhân vật, bố cục tranh chính xác từng pixel.

### **B. Midjourney (MJ)**
*   Dịch vụ trả phí trên Discord. Chất lượng ảnh (Esthetic) cao nhất hiện nay.
*   Không cần biết kỹ thuật Prompt phức tạp vẫn ra ảnh đẹp.

---

## 2. Prompt Engineering (Kỹ sư ra lệnh)

AI rất thông minh nhưng cũng rất ngây thơ. Bạn cần biết cách ra lệnh.

### **Cấu trúc một Prompt chuẩn:**
1.  **Subject (Chủ thể):** A cute girl, a futuristic city.
2.  **Medium (Chất liệu):** Digital painting, oil painting, 3D render.
3.  **Style (Phong cách):** Anime style, Cyberpunk, Ghibli studio.
4.  **Artist (Họa sĩ):** Art by Greg Rutkowski, Alphonse Mucha.
5.  **Quality Boosters (Chất lượng):** 4k, 8k, masterpiece, highly detailed, trending on ArtStation.
6.  **Negative Prompt (Những thứ không muốn):** Ugly, bad anatomy, extra fingers, blurry.

---

## 3. LoRA (Low-Rank Adaptation)

Bạn muốn AI vẽ mặt của bạn? Hay vẽ theo phong cách truyện tranh Việt Nam?
-> Dùng LoRA.

*   Một file nhỏ (vài chục MB) chứa thông tin bổ sung cho mô hình gốc (Checkpoint vài GB).
*   **Training LoRA:** Chỉ cần 20-30 bức ảnh mẫu của bạn + 15 phút training trên Google Colab.
