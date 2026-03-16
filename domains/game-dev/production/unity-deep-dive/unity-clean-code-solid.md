---
title: "Clean Code & SOLID cho Unity Dev"
description: "Áp dụng nguyên tắc lập trình sạch vào vòng đời MonoBehaviour, ScriptableObject, hệ thống gameplay."
last_updated: 2026-03-04
---

# 🧼 Clean Code & SOLID cho Unity Developer

> Unity cho phép bạn ship prototype nhanh, nhưng cũng dễ biến dự án thành “Scene spaghetti”. Bài này giúp bạn áp dụng Clean Code + SOLID vào thực tế Unity: từ MonoBehaviour lifecycle, ScriptableObject đến hệ thống Event/DI.

---

## 0. Mindset dành cho Unity

| Tư duy | Áp dụng trong Unity |
| --- | --- |
| **Scene ≠ God Object** | Tránh nhồi mọi thứ vào `GameManager`/`UIManager`. Tạo module rõ ràng (Input, Combat, UI...). |
| **Data-Driven** | Prefab + ScriptableObject chứa config. Code xử lý logic, không hardcode số. |
| **Testable Behaviour** | MonoBehaviour khó test → trừu tượng hóa logic vào class thuần C#. |
| **Profiling early** | Clean code giúp dễ tối ưu: tách update loop, tránh `FindObjectOfType` runtime. |

---

## 1. SOLID trong Unity

### Single Responsibility (SRP)

- Mỗi MonoBehaviour lo đúng 1 nhiệm vụ. Ví dụ `PlayerInputHandler` chỉ đọc input, `PlayerMovement` xử lý di chuyển.
- Tách logic game khỏi phần render/UI để reuse trên platform khác.

```csharp
public class PlayerInputHandler : MonoBehaviour {
    public Vector2 MoveDirection { get; private set; }

    void Update() {
        MoveDirection = new Vector2(Input.GetAxisRaw("Horizontal"), Input.GetAxisRaw("Vertical"));
    }
}

public class PlayerMovement : MonoBehaviour {
    [SerializeField] float speed = 5f;
    PlayerInputHandler _input;

    void Awake() => _input = GetComponent<PlayerInputHandler>();

    void FixedUpdate() {
        transform.Translate(_input.MoveDirection * speed * Time.fixedDeltaTime);
    }
}
```

### Open/Closed (OCP)

- Dùng Strategy/State để mở rộng feature mà không sửa code cũ. Ví dụ hệ thống vũ khí: thêm `LaserWeapon` mà không sửa `WeaponManager`.
- Sử dụng interface + ScriptableObject để inject behaviour:

```csharp
public abstract class WeaponBehavior : ScriptableObject {
    public abstract void Fire(Transform origin);
}

[CreateAssetMenu(menuName="Weapon/Raycast")]
public class RaycastWeapon : WeaponBehavior {
    public override void Fire(Transform origin) {
        // Raycast logic
    }
}

public class WeaponController : MonoBehaviour {
    [SerializeField] WeaponBehavior currentWeapon;
    public void OnFire() => currentWeapon.Fire(transform);
}
```

### Liskov Substitution (LSP)

- Thực thể kế thừa phải dùng được ở mọi nơi base class dùng. Ví dụ `EnemyAIBase` có `Move()`/`Attack()` → subclass không được throw `NotImplementedException`.
- Dấu hiệu vi phạm: subclass phải check type của chính nó trong method (`if (this is Boss)` ...).

### Interface Segregation (ISP)

- Tạo interface nhỏ, đặc thù: `IDamageable`, `IHealable`, `IInteractable`. Mỗi component chỉ implement cái cần thiết.
- Unity hỗ trợ `RequireComponent` → đảm bảo dependency rõ ràng.

### Dependency Inversion (DIP)

- Module gameplay (Use Case) phụ thuộc abstraction, không phụ thuộc component cụ thể.
- Dùng DI container như **Zenject**, **Extenject** hoặc tự viết **Service Locator** nhẹ.

```csharp
public interface IAudioService { void PlaySfx(string key); }

public class AudioService : IAudioService {
    public void PlaySfx(string key) { /* ... */ }
}

public class AttackAction {
    readonly IAudioService _audio;
    public AttackAction(IAudioService audio) => _audio = audio;
    public void Execute() => _audio.PlaySfx("slash");
}
```

> 🔌 Inject qua constructor/Zenject để Unit Test dễ dàng (mock IAudioService).

---

## 2. Clean Code checklist cho Unity

- [ ] Prefab nhỏ, component rõ trách nhiệm.
- [ ] Không dùng `FindObjectOfType` trong Update (cache hoặc DI).
- [ ] Tránh magic number trong script → đưa vào ScriptableObject/const.
- [ ] Scene chỉ chứa setup, logic nằm ở script thuần.
- [ ] Sử dụng `SerializedField` thay vì public field, tránh lộ state.
- [ ] Viết `Context Menu`/`[Button]` để debug thay vì phím tắt ngẫu nhiên.
- [ ] Ghi chú `TODO(name, date)` rõ ràng trong script.

---

## 3. ScriptableObject & Event Channel

- Tạo **event channel** để decouple UI ↔ gameplay.

```csharp
[CreateAssetMenu(menuName="Events/Void Event")]
public class VoidEvent : ScriptableObject {
    private readonly List<VoidEventListener> listeners = new();
    public void Raise() {
        for (int i = listeners.Count - 1; i >= 0; i--) listeners[i].OnEventRaised();
    }
    public void Register(VoidEventListener listener) => listeners.Add(listener);
    public void Unregister(VoidEventListener listener) => listeners.Remove(listener);
}
```

- UI nghe event qua component `VoidEventListener`, gameplay chỉ cần gọi `event.Raise()`.
- Giúp tuân thủ DIP: lớp phát event không biết ai lắng nghe.

---

## 4. Testing & Tooling

| Mảng | Công cụ/Thực hành | Ghi chú |
| --- | --- | --- |
| Unit Test | NUnit + Test Runner | Test lớp thuần (không MonoBehaviour) |
| Integration | [Unity Test Framework](https://docs.unity3d.com/Packages/com.unity.test-framework@1.1/manual/) | Dựng scene nhỏ, verify flow |
| Automation | CI với `-runTests` | GitHub Actions chạy build & test |
| Static Analysis | Rider/Resharper, SonarLint | Phát hiện smell C# |
| Profiling | Unity Profiler, Deep Profile | Đảm bảo refactor không làm chậm |

> 📦 Lưu ý: Viết test cho service logic giúp refactor tự tin hơn, đặc biệt khi áp dụng SOLID.

---

## 5. Pipeline refactor thực tế

1. Chọn hệ thống cụ thể (Inventory, Input, AI) → viết test bảo vệ logic chính.
2. Tách data/config ra ScriptableObject.
3. Tách MonoBehaviour khỏi logic (service class).
4. Áp dụng SOLID theo thứ tự SRP → DIP.
5. Tích hợp DI/ Event channel nếu cần.
6. Thử nghiệm trong scene nhỏ trước khi merge.

---

## 6. Unity-specific anti-patterns & fix

| Anti-pattern | Triệu chứng | Giải pháp |
| --- | --- | --- |
| God MonoBehaviour | Class 1000 dòng điều phối mọi thứ | Chia thành component theo domain |
| Static Manager | Không test được, thứ tự init lỗi | DI container + ScriptableObject config |
| Update Hell | Script nào cũng Update, tốn CPU | Event/Coroutines, `InvokeRepeating`, hệ thống Tick trung tâm |
| Magic Prefab | Prefab chứa logic ẩn, khó reuse | Document prefab, dùng ScriptableObject cho config |
| Tight Coupling UI-Gameplay | UI gọi trực tiếp logic | Event channel hoặc Presenter layer |

---

## 7. Resources & bài tập

- **Talk “Game Architecture with Scriptable Objects” – Ryan Hipple (Unite Austin).**
- **Zenject/Extenject**: Dependency Injection cho Unity.
- **Unity Game Architecture Guide (Infallible Code, Jason Weimann).**
- **Clean Architecture for Unity (Pragmatic Studio).**

### Bài tập

1. Refactor hệ thống Input hiện tại theo SRP + DIP (Input System mới + Service layer).
2. Chuyển hệ thống UI event sang ScriptableObject event channel.
3. Viết test cho Inventory service (không phụ thuộc MonoBehaviour).
4. Document 1 ADR giải thích vì sao dùng Zenject/ScriptableObject trong dự án.

> 🎯 Kết quả mong đợi: Demo scene chạy ổn, dev mới join hiểu architecture trong <1 ngày.

---

**Next Steps:**

- Commit guideline này vào repo nội bộ hoặc Confluence.
- Thiết lập PR checklist riêng cho Unity (SRP, event channel, test) để giữ chuẩn.

**Remember:** Code sạch + SOLID không làm bạn chậm lại; nó giúp bạn ship prototype nhanh và scale lên game full release mà không rewrite.