# 🦶 Inverse Kinematics (IK): The Math of Natural Movement

> [← Back to Game Dev Roadmap](../README.md) | [← Back to Advanced Trigonometry](../../guides/01-mental-models/mathematics/advanced-trigonometry.md)
>
> *"Forward Kinematics (FK) là cách robot di chuyển: xoay vai, rồi xoay khuỷu tay để bàn tay chạm vào vật. Inverse Kinematics (IK) là cách con người di chuyển: xác định vị trí bàn tay trước, sau đó để vai và khuỷu tay tự động xoay theo một cách tự nhiên."*

Để chân nhân vật bám sát địa hình (Foot Placement) hoặc tay cầm chính xác một vật thể, chúng ta dùng **Lượng giác** để giải ngược các góc xoay của khớp xương.

---

## 1. Bài toán IK 2 xương (The 2-Bone IK Problem)

Đây là trường hợp phổ biến nhất (Đùi - Cẳng chân, Bắp tay - Cẳng tay).
*   **Dữ liệu đầu vào:** Độ dài xương đùi ($L_1$), xương cẳng chân ($L_2$), và vị trí mục tiêu ($Target$).
*   **Mục tiêu:** Tìm góc $\alpha$ (hông) và $\beta$ (đầu gối).

---

## 2. Công thức cốt lõi: Định lý Hàm số Cos (Law of Cosines)

Đây là "chìa khóa vàng" để giải IK. Trong một tam giác có các cạnh $a, b, c$:
$$c^2 = a^2 + b^2 - 2ab \cos(C)$$

Áp dụng vào chân nhân vật:
1.  **Tính khoảng cách $D$:** Từ hông đến mục tiêu (bằng định lý Pythagoras 3D).
2.  **Tính góc đầu gối ($\beta$):** 
    $$\cos(\beta) = \frac{L_1^2 + L_2^2 - D^2}{2 L_1 L_2}$$
3.  **Tính góc hông ($\alpha$):** Kết hợp giữa góc hướng về mục tiêu và góc trong tam giác tạo bởi $L_1, L_2, D$.

---

## ⛰️ 3. Ứng dụng: Bám sát địa hình (Foot Placement)

Để chân nhân vật đứng vững trên bậc thang hoặc dốc:

1.  **Raycasting:** Bắn một tia từ trên xuống dưới tại vị trí mỗi bàn chân.
2.  **Xác định Target:** Điểm va chạm của tia với mặt đất chính là `Target` mới cho bàn chân.
3.  **Giải IK:** Truyền `Target` này vào hàm giải IK 2 xương ở trên.
4.  **Điều chỉnh hông (Pelvis):** Nếu chân bị kéo quá căng hoặc quá trùng, ta phải hạ thấp hoặc nâng cao trọng tâm (Pelvis) của cả nhân vật.

---

## 🛠️ Code Snippet: Giải IK 2 xương đơn giản (C#)

```csharp
// Giải IK 2D/3D đơn giản cho 2 đoạn xương
void SolveIK(float L1, float L2, Vector3 targetPos) {
    float dist = Vector3.Distance(hipPos, targetPos);
    
    // Giới hạn khoảng cách (không để chân bị kéo quá dài)
    dist = Mathf.Clamp(dist, 0.0001f, L1 + L2);

    // Tính góc đầu gối (Beta) bằng định lý hàm Cos
    float cosBeta = (L1*L1 + L2*L2 - dist*dist) / (2 * L1 * L2);
    float angleBeta = Mathf.Acos(cosBeta) * Mathf.Rad2Deg;

    // Tính góc hông (Alpha)
    float cosAlpha = (L1*L1 + dist*dist - L2*L2) / (2 * L1 * dist);
    float angleAlpha = Mathf.Acos(cosAlpha) * Mathf.Rad2Deg;

    // Áp dụng xoay cho xương (đã đơn giản hóa)
    UpperLeg.localRotation = Quaternion.Euler(angleAlpha, 0, 0);
    LowerLeg.localRotation = Quaternion.Euler(180 - angleBeta, 0, 0);
}
```

---

## 🧠 Mental Model: Tam giác thích nghi (The Adaptive Triangle)

Hãy coi chân nhân vật như một **Tam giác có thể co giãn**:
*   Một cạnh là khoảng cách từ hông đến mặt đất (luôn thay đổi theo địa hình).
*   Hai cạnh còn lại là chiều dài xương (cố định).
*   **Nhiệm vụ của lượng giác:** Tìm ra các góc bên trong để tam giác đó luôn khép kín và chạm đúng vào mục tiêu.

---

## 🚀 Lộ trình Thực hành

1.  **Level 1:** Tạo 2 khối Cube kết nối với nhau. Dùng code trên để làm cho đầu khối thứ 2 luôn "nhìn" và chạm vào một quả cầu mục tiêu.
2.  **Level 2:** Dùng Raycast để phát hiện độ cao mặt đất và gán nó làm mục tiêu cho bàn chân.
3.  **Level 3:** Thêm **Look-at Constraint** cho bàn chân để nó nằm phẳng theo độ nghiêng của mặt dốc (dùng Vector Normal từ Raycast).

---

## 🔗 Liên kết mở rộng
*   **[Simple Physics Engine Guide](../physics/simple-physics-engine.md):** Cách dùng Raycasting để xác định địa hình.
*   **[Advanced Trigonometry Guide](../../guides/01-mental-models/mathematics/advanced-trigonometry.md):** Nắm vững hàm `Acos` và các biến đổi góc.
