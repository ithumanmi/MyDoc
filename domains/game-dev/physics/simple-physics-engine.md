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

## ⚙️ Unity Physics Deep Dive

### 1. Hiểu hệ tọa độ & đơn vị
- **1 đơn vị Unity = 1 mét** (theo mặc định). Điều này ảnh hưởng trực tiếp đến trọng lực (`-9.81 m/s²`) và vận tốc. Nếu nhân vật manh mún (0.1m) nhưng dùng trọng lực mặc định, bạn sẽ thấy chuyển động “nhanh như chớp”.
- **Fixed Timestep:** `Edit > Project Settings > Time > Fixed Timestep` mặc định 0.02s (50Hz). Tăng lên 0.01s để có vật lý chính xác hơn nhưng tốn CPU.

### 2. Rigidbody Tips
- **Rigidbody vs Rigidbody2D:** Không trộn lẫn. Physics 2D hoàn toàn khác pipeline so với 3D.
- **Kinematic vs Dynamic:** Dùng `isKinematic` cho vật thể di chuyển bằng code (animation) nhưng vẫn trigger va chạm. Dùng Dynamic cho vật thể chịu lực tự nhiên.
- **Interpolation:** Nếu camera rung khi Rigidbody di chuyển nhanh, bật `Interpolate` để Unity nội suy giữa các frame vật lý.

### 3. Lực, mô-men & damping
- **AddForce:** Dùng cho chuyển động vật lý chân thực. `AddForce(force, ForceMode.Impulse)` phù hợp cho jump/đạn.
- **Torque:** `AddTorque` để xoay vật thể theo mô-men xoắn (ví dụ bánh xe, cửa).
- **Drag vs Angular Drag:** Dùng để mô phỏng lực cản không khí. Giá trị lớn = giảm tốc nhanh, giá trị 0 = trượt mãi.

### 4. Collision Layers & Contact Modification
- **Physics Layers:** Định nghĩa ma trận va chạm trong `Project Settings > Physics`. Ví dụ layer “Player” không va chạm “Player” để tránh đồng đội đẩy nhau.
- **Continuous Collision Detection:** Tránh xuyên tường khi Rigidbody tốc độ cao. Chọn `Continuous` hoặc `Continuous Dynamic` cho đối tượng nhanh (đạn, xe). Shader-based Raycast hỗ trợ kiểm soát thêm.
- **Contact Modification:** Unity 2022+ cho phép chỉnh sửa tiếp xúc trong runtime để tạo các hiệu ứng như surface trơn, lực đè đặc biệt.

### 5. Character Controller vs Rigidbody
- **CharacterController:** Dùng cho nhân vật người (FPS/TPS) cần kiểm soát chính xác. Nó không dùng physics simulation mà yêu cầu bạn tính toán `Move` thủ công, phù hợp khi cần phản hồi nhanh.
- **Rigidbody Controller:** Dùng cho game cần tương tác vật lý tự nhiên (đẩy thùng, ragdoll). Khi code, áp dụng lực thay vì set vị trí để Unity xử lý va chạm đúng.

### 6. Debug Tools
- **Physics Debugger:** `Window > Analysis > Physics Debugger` hiển thị collider, joint, contact.
- **Gizmos:** Dùng `OnDrawGizmos` để vẽ raycast, vector normal trong Scene view.
- **Profiler > Physics:** Theo dõi thời gian CPU dành cho `Physics.Simulate`. Nếu spike, xem có collider quá phức tạp hoặc quá nhiều `FixedUpdate`.

### 7. Ứng dụng nâng cao
- **Constraint Solver:** Khi cần vật thể “cứng” (ví dụ robot arm), chỉnh `Solver Iteration Count` của Rigidbody để hệ thống ổn định hơn.
- **Articulation Body (Robot/Vehicle):** Unity giới thiệu hệ mới cho robotics, mô phỏng khớp chính xác hơn Rigidbody + Joint. Dùng cho xe tăng, cánh tay máy.
- **DOTS Physics:** Nếu cần 10.000 vật thể va chạm cùng lúc, cân nhắc chuyển sang Unity Physics/Burst (ECS) để tận dụng SIMD.

> 🔁 **Workflow gợi ý:** Prototype với Rigidbody chuẩn → Khi project lớn, chuyển phần cần hiệu năng cao sang DOTS Physics → Dùng Articulation cho hệ máy móc chuyên biệt.

### 8. Joint Systems & Constraints
- **Fixed/Configurable Joint:** Dùng cho cửa, bập bênh, robot arm. Configurable Joint cho phép khóa/giới hạn từng trục chuyển động và xoay (Linear/Angular Limit). Khi thấy joint rung, tăng `Solver Iteration Count` hoặc bật `Projection`.
- **Hinge Joint:** Thêm motor và limits để tạo bánh xe, bản lề. Đừng quên set `Use Motor` và `Max Torque` đủ lớn, nếu không bánh xe sẽ không quay.
- **Spring Joint:** Tạo hiệu ứng dây thun, grappling hook. Kết hợp với `LineRenderer` để hiển thị dây.

### 9. Substepping & Stability
- Unity cho phép bật **Auto Simulation** hoặc bạn có thể tự gọi `Physics.Simulate(deltaTime)` để thực hiện substep thủ công.
- Khi game chạy ở 120 FPS nhưng FixedUpdate chỉ 50Hz, hãy cân nhắc **multiple substeps** trong một khung hình để vật lý ổn định hơn (đặc biệt với trò đua xe hoặc ragdoll).
- Pseudocode:
```csharp
float accumulator;
void Update() {
    accumulator += Time.deltaTime;
    while (accumulator >= fixedDeltaTime) {
        Physics.Simulate(fixedDeltaTime);
        accumulator -= fixedDeltaTime;
    }
}
```

### 10. Profiling & Optimization Checklist
- [ ] Collider shape tối giản (dùng primitive trước, mesh collider chỉ cho static object).
- [ ] Gộp các rigidbody nhỏ thành một rigidbody + nhiều collider con để giảm số solver.
- [ ] Tránh `OnCollisionStay` nếu không thật sự cần (gọi mỗi FixedUpdate).
- [ ] Batch `Physics.RaycastNonAlloc` thay vì tạo GC mỗi lần ray.
- [ ] Dùng `Physics.IgnoreCollision` cho các cặp không cần va chạm (ví dụ viên đạn với người bắn).
- [ ] Với mobile, giữ tổng số Rigidbody động < 200 để tránh drop khung hình.

### 11. Sample: Custom Gravity & Surface Alignment
```csharp
public class PlanetGravity : MonoBehaviour {
    public Transform planetCenter;
    public float gravity = 9.81f;
    Rigidbody rb;

    void Awake() {
        rb = GetComponent<Rigidbody>();
        rb.useGravity = false; // Tắt gravity mặc định
    }

    void FixedUpdate() {
        Vector3 direction = (planetCenter.position - transform.position).normalized;
        rb.AddForce(direction * gravity, ForceMode.Acceleration);

        // Căn nhân vật theo bề mặt
        Quaternion targetRotation = Quaternion.FromToRotation(transform.up, direction) * transform.rotation;
        transform.rotation = Quaternion.Slerp(transform.rotation, targetRotation, 10f * Time.fixedDeltaTime);
    }
}
```
- Script trên cho phép nhân vật đi trên hành tinh hình cầu, sử dụng lực trọng trường tùy chỉnh và lượng giác/quaternion để căn bề mặt.

### 12. Khi nào nên tự viết Physics?
- **Mini-game cần độ chính xác đặc biệt** (ví dụ golf, billiards): Tự viết collision và phản xạ để kiểm soát tuyệt đối.
- **Game turn-based:** Có thể dùng vật lý “từng bước” (discrete) thay vì simulation liên tục.
- **Compatibility:** Một số console/mobile build yêu cầu deterministic physics; khi đó bạn phải tự implement hoặc dùng DOTS Physics với fixed point math.

### 13. Unity Physics Best Practices
1. **Tách Update và FixedUpdate rõ ràng:** Logic gameplay (input, animation) ở `Update`, logic vật lý ở `FixedUpdate`. Đừng đọc input trong `FixedUpdate` để tránh missed frame.
2. **Không thay đổi transform trực tiếp khi dùng Rigidbody:** Luôn dùng `MovePosition`, `MoveRotation` hoặc `AddForce` để giữ đồng bộ với solver.
3. **Giảm GC Alloc:** Tránh tạo mới Vector/Quaternion trong vòng lặp. Dùng biến static hoặc `Vector3 temp` tái sử dụng.
4. **Batch Raycast:** Dùng `Physics.RaycastNonAlloc` hoặc `RaycastCommand.ScheduleBatch` để xử lý hàng loạt ray trong job.
5. **Layer-based logic:** Việc bật/tắt collision bằng layer mask tốt hơn code `if (other.CompareTag("Player"))` lặp lại.
6. **Animator vs Physics:** Nếu nhân vật dùng Animator, bật `Update Mode = Animate Physics` để đồng bộ với FixedUpdate nhằm tránh jitter.
7. **Snapshot & rollback khi multiplayer:** Lưu trạng thái Rigidbody (pos/vel) để dễ rollback khi client prediction sai.
8. **Sử dụng `Physics.OverlapSphere` để thay thế trigger liên tục:** Tối ưu cho kiểm tra vùng ảnh hưởng (AOE damage) so với việc tạo nhiều collider trigger.
9. **Đặt `Maximum Allowed Timestep` hợp lý:** Tránh trường hợp FPS drop khiến physics “nhảy” do FixedUpdate bị skip. Giá trị ~0.33 giúp game vẫn chạy ổn khi drop.
10. **Document unit scale và gravity trong README dự án:** Đảm bảo tất cả thành viên team dùng chung tiêu chuẩn, tránh bug do “mỗi người một mét”.

---

## 🔗 Liên kết mở rộng
*   **[Advanced Trigonometry Guide](../../guides/01-mental-models/mathematics/advanced-trigonometry.md):** Nắm vững lý thuyết chuỗi Taylor và Euler.
*   **[Game AI Patterns](../ai/game-ai-patterns.md):** Dùng lượng giác để tính tầm nhìn (Field of View).
