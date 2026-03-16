# 🎨 Graphics & Shaders: Phù thủy hình ảnh (Level 8)

> [← Back to Game Development Roadmap](../README.md)

Làm sao để nước biển lấp lánh? Làm sao để cỏ đung đưa trong gió?
Đó là ma thuật của **Shader**.

---

## 1. Shader là gì?

Là những chương trình nhỏ chạy trên GPU (Card đồ họa) để quyết định màu sắc của từng điểm ảnh (Pixel) trên màn hình.

### **A. Vertex Shader (Đỉnh)**
*   Xử lý các đỉnh của vật thể 3D.
*   **Ứng dụng:** Làm cỏ đung đưa (dịch chuyển đỉnh), làm lá cờ bay, làm mặt nước gợn sóng.

### **B. Fragment/Pixel Shader (Điểm ảnh)**
*   Xử lý màu sắc của từng pixel.
*   **Ứng dụng:** Ánh sáng, bóng đổ, phản xạ gương, hiệu ứng cháy.

---

## 2. Shader Graph (Node-based)

Dành cho Artist hoặc Designer không thích code.
*   Kéo thả các node (Texture, Multiply, Add, Time) để tạo hiệu ứng.
*   Trực quan, thấy ngay kết quả (WYSIWYG).
*   Có sẵn trong Unity (Shader Graph) và Unreal (Material Editor).

---

## 3. HLSL / GLSL (Code tay)

Dành cho Tech Artist hoặc Graphics Programmer.
*   Kiểm soát tối đa hiệu năng.
*   Thực hiện các thuật toán toán học phức tạp mà Node không làm được.

```glsl
// Ví dụ GLSL đơn giản: Tô màu đỏ cho mọi thứ
void main() {
    gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
}
```

---

## 4. VFX Graph (Hiệu ứng hạt)

Tạo ra hàng triệu hạt (Particles) để mô phỏng:
*   Mưa, Tuyết, Bụi.
*   Vụ nổ, Tia lửa điện.
*   Phép thuật (Fireball, Healing Aura).
*   Chạy trên GPU -> Hiệu năng cực cao (so với hệ thống Particle cũ chạy trên CPU).
