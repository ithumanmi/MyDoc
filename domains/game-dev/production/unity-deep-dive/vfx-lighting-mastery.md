# ✨ VFX & Lighting Mastery: Nghệ thuật Ánh sáng

> [← Back to Game Development Roadmap](../README.md)

Một game có đồ họa đẹp hay xấu phụ thuộc 70% vào Ánh sáng (Lighting) và Hiệu ứng (VFX).

---

## 1. Lighting (Ánh sáng)

### **A. Baked Lighting (Ánh sáng nướng)**
*   Tính toán trước ánh sáng và bóng đổ, lưu vào Texture (Lightmap).
*   **Ưu điểm:** Rất nhẹ lúc chạy game (vì đã tính xong rồi). Đẹp (có GI - Global Illumination).
*   **Nhược điểm:** Không thay đổi được (Tĩnh). Vật thể di chuyển sẽ không có bóng đẹp.

### **B. Realtime Lighting (Ánh sáng thời gian thực)**
*   Tính toán mỗi frame.
*   **Ưu điểm:** Động, tương tác tốt.
*   **Nhược điểm:** Nặng máy.

### **C. Mixed Lighting (Kết hợp)**
*   Vật tĩnh dùng Baked. Vật động dùng Realtime (kết hợp Light Probes để vật động nhận ánh sáng từ môi trường tĩnh).

---

## 2. Post-processing (Hậu kỳ)

Giống như chỉnh filter Instagram cho game.

*   **Bloom:** Hiệu ứng tỏa sáng (cho đèn neon, kiếm laze).
*   **Color Grading:** Chỉnh màu sắc (Tone lạnh kinh dị, Tone ấm ấm cúng).
*   **Vignette:** Làm tối 4 góc màn hình (tăng sự tập trung).
*   **Depth of Field (DOF):** Làm mờ hậu cảnh (như máy ảnh xóa phông).

---

## 3. VFX Graph (Visual Effect Graph)

Công cụ mạnh nhất của Unity để làm hạt (Particles).

*   **GPU Power:** Chạy trên GPU, có thể render hàng triệu hạt cùng lúc.
*   **Node-based:** Kéo thả logic.
*   **Tương tác:** Hạt có thể tương tác với môi trường (nảy trên sàn, bị gió thổi).

---

## 4. Shader Graph (Tạo chất liệu)

*   **Fresnel Effect:** Hiệu ứng viền sáng (dùng cho khiên năng lượng, bóng ma).
*   **Dissolve:** Hiệu ứng tan biến (dùng khi quái vật chết).
*   **Vertex Displacement:** Làm mặt nước gợn sóng, lá cờ bay.
