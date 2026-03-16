# 🤖 Steering Behaviors: The Art of Intelligent Movement

> [← Back to Game AI Patterns](./game-ai-patterns.md) | [← Back to Advanced Trigonometry](../../guides/01-mental-models/mathematics/advanced-trigonometry.md)
>
> *"Steering Behaviors không điều khiển vị trí trực tiếp, chúng điều khiển **Lực (Forces)**. Thay vì bảo AI 'đi đến đây', chúng ta bảo AI 'hãy tạo ra một lực đẩy về phía này'. Chính điều này tạo ra sự mượt mà và tự nhiên như sinh vật thật."*

Để kẻ thù rượt đuổi hoặc né tránh người chơi một cách thông minh, chúng ta dùng **Lượng giác** để tính toán các Vector lực dựa trên các góc nhìn và khoảng cách.

---

## 1. Seek (Rượt đuổi) & Flee (Né tránh)

Đây là hai hành vi cơ bản nhất, dựa trên hiệu số giữa vị trí hiện tại và mục tiêu.

*   **Seek:** `DesiredVelocity = (TargetPos - CurrentPos).Normalized * MaxSpeed`
*   **Flee:** `DesiredVelocity = (CurrentPos - TargetPos).Normalized * MaxSpeed` (Ngược lại với Seek).

**Lượng giác ở đâu?** Khi bạn muốn giới hạn tầm nhìn (Field of View - FOV), bạn dùng **Tích vô hướng (Dot Product)**:
*   `Angle = acos(DotProduct(ForwardVector, DirectionToTarget))`
*   Nếu `Angle < FOV / 2`, kẻ thù mới bắt đầu rượt đuổi.

---

## 2. Arrival (Hành vi "Cập bến" mượt mà)

Seek thông thường sẽ khiến AI bị "vọt" quá mục tiêu và quay lại liên tục (overshooting). **Arrival** giải quyết điều này bằng cách giảm tốc độ khi gần đến đích.

1.  **Tính khoảng cách $D$** đến mục tiêu.
2.  **Xác định bán kính hãm phanh (Slowing Radius $R$):**
    *   Nếu $D > R$: Tốc độ = `MaxSpeed`.
    *   Nếu $D \le R$: Tốc độ = `MaxSpeed * (D / R)`.

---

## 🎡 3. Wander (Đi lang thang tự nhiên)

Đây là nơi lượng giác thể hiện sức mạnh tuyệt đối. Để AI đi lang thang không bị "máy móc", chúng ta dùng một **Đường tròn ảo** phía trước AI.

1.  **Tạo một điểm trên đường tròn:** Dùng $\sin, \cos$ để tìm tọa độ điểm trên vòng tròn ảo.
    *   `Target.x = cos(WanderAngle) * Radius`
    *   `Target.z = sin(WanderAngle) * Radius`
2.  **Cập nhật góc:** Mỗi khung hình, thay đổi `WanderAngle` một lượng nhỏ ngẫu nhiên.
3.  **Di chuyển:** AI sẽ "Seek" về phía điểm này.

**Kết quả:** AI di chuyển mượt mà, uốn lượn thay vì đi theo những đường thẳng giật cục.

---

## 🛡️ 4. Obstacle Avoidance (Né tránh chướng ngại vật)

Để AI không đâm vào tường, chúng ta dùng **Raycasting** kết hợp với lượng giác để "quét" không gian phía trước.

*   **Quét góc (Scanning):** AI có thể bắn 3-5 tia theo các góc khác nhau (ví dụ: $-30^\circ, 0^\circ, 30^\circ$).
*   **Lực đẩy (Avoidance Force):** Nếu tia bên trái chạm tường, tạo một lực đẩy sang bên phải (dùng ma trận quay hoặc $\sin, \cos$ để tính vector lực mới).

---

## 🛠️ Code Snippet: Wander Behavior (C#)

```csharp
void ApplyWander(float deltaTime) {
    // 1. Thay đổi góc lang thang ngẫu nhiên
    wanderAngle += Random.Range(-jitter, jitter);

    // 2. Tính vị trí mục tiêu trên đường tròn ảo
    Vector3 circleCenter = transform.position + transform.forward * distance;
    Vector3 targetOnCircle = new Vector3(
        Mathf.Cos(wanderAngle) * radius,
        0,
        Mathf.Sin(wanderAngle) * radius
    );
    
    Vector3 targetWorldPos = circleCenter + targetOnCircle;

    // 3. Seek về phía mục tiêu đó
    Seek(targetWorldPos);
}
```

---

## 🧠 Mental Model: Lực kéo và Đẩy (Tug-of-War)

Hãy coi AI như một vật thể bị kéo bởi nhiều sợi dây thun:
*   **Seek:** Sợi dây thun kéo về phía người chơi.
*   **Avoidance:** Sợi dây thun đẩy ra xa khỏi tường.
*   **Wander:** Sợi dây thun kéo về một hướng ngẫu nhiên.
*   **Result:** Vector lực tổng hợp (`SteeringForce`) sẽ quyết định hướng đi thông minh nhất.

---

## 🚀 Lộ trình Thực hành

1.  **Level 1:** Viết script Seek đơn giản. Thêm FOV để AI chỉ đuổi khi thấy người chơi.
2.  **Level 2:** Thực hiện Wander dùng đường tròn ảo. Quan sát sự khác biệt so với việc chọn điểm ngẫu nhiên trên bản đồ.
3.  **Level 3:** Kết hợp Seek + Obstacle Avoidance. Thử thách: AI phải rượt đuổi người chơi xuyên qua một mê cung đơn giản.

---

## 🔗 Liên kết mở rộng
*   **[Game AI Patterns](./game-ai-patterns.md):** Tổng quan về FSM và Behavior Trees.
*   **[Simple Physics Engine Guide](../physics/simple-physics-engine.md):** Cách áp dụng lực (`AddForce`) vào chuyển động.
*   **[Advanced Trigonometry Guide](../../guides/01-mental-models/mathematics/advanced-trigonometry.md):** Hiểu sâu về Dot Product và các hàm xoay.
