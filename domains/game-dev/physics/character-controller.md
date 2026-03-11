---
title: "Character Controller"
description: "Built-in vs custom Rigidbody, slopes, stairs, grounding."
tags:
  - physics
  - unity
  - character-controller
updated: 2026-03-11
---

# 🧍 Character Controller (Unity)

## 1) Built-in CharacterController
- Ưu: ổn định, không chịu lực; sẵn `Move`, `SimpleMove`, slope limit, step offset.
- Nhược: không bị đẩy bởi lực, khó tương tác ragdoll/physics thật; chỉ capsule.
- Sử dụng khi cần movement arcade, camera third-person, ít tương tác lực.

### Tips
- `Move` với deltaPos tính từ input (normalized) * speed * Time.deltaTime.
- Ground check: dùng `CharacterController.isGrounded` + raycast bổ sung để tránh miss.
- Slope limit & step offset: set 45° và 0.3–0.5m; hạ step offset khi chạy nhanh để tránh bounce.
- Slide khi vượt slope: tính vector kéo xuống, áp vào Move.

## 2) Custom Rigidbody Controller
- Dùng Rigidbody + collider (Capsule). Cho phép AddForce, impulse, ragdoll, network prediction.
- Cần kiểm soát: lock rotation (freeze X/Z), dùng `MovePosition`/`MoveRotation` thay vì AddForce nếu cần chính xác.
- Ground detection: SphereCast hoặc CapsuleCast; track normal để xử lý slope.

### Slopes & Stairs
- **Slope handling:** project velocity lên plane theo ground normal; clamp angle > limit → slide.
- **Stairs:** dùng capsule cast nâng ~stepHeight, move forward, sau đó hạ xuống raycast.
- **Coyote time:** cho phép jump trong 0.1s sau khi rời đất để responsive.

## 3) Custom Controller Architecture
- Split input, movement intent, physics apply.
- FixedUpdate: handle physics, raycast; Update: đọc input, camera.
- Layer mask: ground vs hazard vs dynamic; tắt collisions không cần.

## 4) Performance & Debug
- Gizmo ground normal, slope limit, step preview.
- Profiler: check FixedUpdate cost; tránh dùng nhiều raycast trong frame.
- NonAlloc casts; cache colliders.

## 5) Ví dụ C# (Rigidbody Controller)

```csharp
[RequireComponent(typeof(Rigidbody))]
public class RigidbodyCharacterController : MonoBehaviour
{
    [SerializeField] float moveSpeed = 6f;
    [SerializeField] float acceleration = 12f;
    [SerializeField] float jumpForce = 6f;
    [SerializeField] float coyoteTime = 0.1f;
    [SerializeField] Transform groundCheck;
    [SerializeField] float groundRadius = 0.25f;
    [SerializeField] LayerMask groundMask;

    Rigidbody _body;
    Vector3 _desiredVel;
    float _lastGroundedTime;

    void Awake()
    {
        _body = GetComponent<Rigidbody>();
        _body.constraints = RigidbodyConstraints.FreezeRotationX |
                            RigidbodyConstraints.FreezeRotationZ;
    }

    void Update()
    {
        Vector2 input = new Vector2(Input.GetAxisRaw("Horizontal"), Input.GetAxisRaw("Vertical"));
        Vector3 moveDir = (transform.right * input.x + transform.forward * input.y).normalized;
        _desiredVel = moveDir * moveSpeed;

        if (IsGrounded())
            _lastGroundedTime = Time.time;

        if (Input.GetButtonDown("Jump") && Time.time - _lastGroundedTime <= coyoteTime)
        {
            Vector3 vel = _body.velocity;
            vel.y = 0f;
            _body.velocity = vel + Vector3.up * jumpForce;
        }
    }

    void FixedUpdate()
    {
        Vector3 vel = _body.velocity;
        Vector3 target = new Vector3(_desiredVel.x, vel.y, _desiredVel.z);
        Vector3 accel = Vector3.MoveTowards(new Vector3(vel.x, 0f, vel.z),
                                            new Vector3(_desiredVel.x, 0f, _desiredVel.z),
                                            acceleration * Time.fixedDeltaTime);
        Vector3 projected = ProjectOnGround(new Vector3(accel.x, 0f, accel.z));
        _body.velocity = new Vector3(projected.x, vel.y, projected.z);
    }

    bool IsGrounded()
    {
        return Physics.CheckSphere(groundCheck.position, groundRadius, groundMask,
            QueryTriggerInteraction.Ignore);
    }

    Vector3 ProjectOnGround(Vector3 horizontal)
    {
        if (Physics.Raycast(transform.position, Vector3.down, out RaycastHit hit, 0.75f, groundMask))
        {
            return Vector3.ProjectOnPlane(horizontal, hit.normal);
        }
        return horizontal;
    }
}
```

- `ProjectOnGround` giữ vận tốc theo mặt phẳng slope.
- `CheckSphere` + coyote time giúp jump ổn định.
- Input đọc ở `Update`, áp lực trong `FixedUpdate` để sync với physics.

## ✅ Apply it
- [ ] Chọn built-in khi movement arcade, ít tương tác; custom Rigidbody khi cần lực/netcode.
- [ ] Thiết lập slope limit, step offset hợp lý; thêm slide logic.
- [ ] Ground check kết hợp isGrounded + ray/sphere cast.
- [ ] Với custom: lock rotation, project velocity theo ground, coyote time.
- [ ] Profile raycast, dùng NonAlloc; debug gizmo slope/step.