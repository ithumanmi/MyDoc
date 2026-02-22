# 🏗️ Building a Simple 3D Physics Engine with Trigonometry

> [← Back to Game Dev Roadmap](../README.md) | [← Back to Advanced Trigonometry](../../guides/01-mental-models/mathematics/advanced-trigonometry.md)
>
> *"Lượng giác không chỉ là toán học khô khan; nó là 'xương sống' của mọi thế giới ảo 3D. Nếu không có nó, các nhân vật không thể quay, ánh sáng không thể chiếu, và vật thể không thể va chạm."*

Để xây dựng một **Physics Engine** đơn giản từ con số 0, bạn cần làm chủ cách lượng giác điều khiển không gian 3 chiều. Dưới đây là lộ trình kỹ thuật thực chiến.

---

## 1. Công cụ cơ bản: Vector & Góc

Trong 3D, mọi thứ đều là Vector $(x, y, z)$. Lượng giác giúp chúng ta chuyển đổi giữa **Góc (Angles)** và **Hướng (Directions)**.

*   **Chuyển Góc sang Hướng (2D Example):**
    *   $x = \cos(\theta)$
    *   $y = \sin(\theta)$
*   **Chuyển Hướng sang Góc:**
    *   $\theta = \arctan2(y, x)$

**Ứng dụng:** Khi bạn nhấn phím mũi tên để xoay nhân vật, bạn đang thay đổi $\theta$. Để di chuyển nhân vật tiến lên, bạn cần dùng $\cos, \sin$ để tính toán $x, y$ mới.

---

## 2. Xoay vật thể: Ma trận quay (Rotation Matrices)

Để xoay một điểm $(x, y, z)$ quanh một trục, chúng ta dùng ma trận chứa các hàm lượng giác.

*   **Xoay quanh trục Z (Roll):**
    $$x' = x \cos(\theta) - y \sin(\theta)$$
    $$y' = x \sin(\theta) + y \cos(\theta)$$
    $$z' = z$$

**💡 Pro Tip:** Trong các engine hiện đại như Unity, việc này được xử lý bởi **Quaternion**, nhưng hiểu ma trận quay giúp bạn debug các lỗi về "Gimbal Lock" và tự viết các hiệu ứng quay tùy chỉnh.

---

## 3. Raycasting: "Tia mắt" của vật lý

Raycasting là kỹ thuật quan trọng nhất để phát hiện va chạm, nhặt đồ vật, hoặc AI nhìn thấy người chơi.

1.  **Xác định hướng tia:** Dùng lượng giác để tính toán vector hướng từ góc quay của camera.
    *   `Direction.x = cos(yaw) * cos(pitch)`
    *   `Direction.y = sin(pitch)`
    *   `Direction.z = sin(yaw) * cos(pitch)`
2.  **Kiểm tra va chạm:** Tia sẽ di chuyển từng bước nhỏ hoặc dùng các phép toán hình học để tìm điểm giao nhau với mặt phẳng/khối cầu.

---

## 4. Va chạm & Phản xạ (Collision & Reflection)

Khi một quả bóng đập vào tường, làm sao để nó nảy ra đúng góc?

*   **Pháp tuyến (Normal):** Mỗi bề mặt có một vector pháp tuyến $\vec{n}$ vuông góc với nó.
*   **Tích vô hướng (Dot Product):** $\vec{a} \cdot \vec{b} = |\vec{a}| |\vec{b}| \cos(\theta)$.
*   **Công thức phản xạ:** $\vec{r} = \vec{v} - 2(\vec{v} \cdot \vec{n})\vec{n}$.

**Lượng giác ở đâu?** Tích vô hướng thực chất là phép chiếu lượng giác. Nó giúp xác định góc giữa vector vận tốc và mặt phẳng va chạm để tính lực phản hồi.

---

## 5. Mô phỏng Dao động (Harmonic Motion)

Để làm cho cỏ đung đưa, nước dập dềnh, hoặc nhân vật thở nhẹ khi đứng yên:
*   `position.y = offset + amplitude * sin(time * frequency)`

Đây là cách đơn giản nhất để tạo ra chuyển động trông "tự nhiên" mà không cần tính toán vật lý phức tạp (RigidBody).

---

## 🛠️ Code Example đơn giản (Pseudocode)

```csharp
// Di chuyển nhân vật dựa trên góc quay (Yaw)
void UpdateMovement(float speed, float deltaTime) {
    float angleRad = rotationAngle * Mathf.Deg2Rad;
    
    // Tính hướng tiến lên bằng lượng giác
    float forwardX = Mathf.Cos(angleRad);
    float forwardZ = Mathf.Sin(angleRad);
    
    // Cập nhật vị trí
    position.x += forwardX * speed * deltaTime;
    position.z += forwardZ * speed * deltaTime;
}
```

---

## 🧠 Mental Model: Phép chiếu (Projection)

Hãy coi lượng giác như một **Máy chiếu**. Nó lấy một "ý định" (Góc quay) và chiếu nó lên "thực tại" (Tọa độ $x, y, z$).
*   **Tội lỗi lớn nhất:** Dùng quá nhiều hàm `sin/cos` trong vòng lặp lớn (Update) có thể làm giảm hiệu năng.
*   **Giải pháp:** Cache các giá trị hoặc dùng bảng Lookup Table (LUT) nếu làm hệ thống cực thấp cấp.

---

## 🚀 Lộ trình Thực hành

1.  **Level 1:** Tự viết script xoay một khối lập phương quanh tâm mà không dùng `transform.Rotate`.
2.  **Level 2:** Làm một hệ thống Camera Top-down luôn hướng về nhân vật dùng `Atan2`.
3.  **Level 3:** Tự viết hệ thống nảy bóng (Simple Reflection) trên một mặt phẳng nghiêng.

---

## 🔗 Liên kết mở rộng
*   **[Advanced Trigonometry Guide](../../guides/01-mental-models/mathematics/advanced-trigonometry.md):** Nắm vững lý thuyết chuỗi Taylor và Euler.
*   **[Game AI Patterns](../ai/game-ai-patterns.md):** Dùng lượng giác để tính tầm nhìn (Field of View).
