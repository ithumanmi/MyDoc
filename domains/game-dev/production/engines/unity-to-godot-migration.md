# Unity to Godot 4.x Migration Guide (Cho Indie Dev)

> [← Back to Game Engines Focus](./README.md) | [Home](../../../README.md)

Godot 4.x đang dần trở thành "Blender của Game Engine". Đối với Indie Hackers và Solo Developers năm 2026, Godot cung cấp môi trường nhẹ, mã nguồn mở 100% (không lo vụ phí cài đặt Runtime Fee như Unity năm 2023), và workflow cực kỳ mượt mà cho 2D/3D. 

Bài viết này dành cho những ai đã rành Unity C# và muốn chuyển não (Mental Shift) sang Godot.

---

## 🏗️ 1. Cú Áp Tròng Lớn Nhất: Nodes vs Components

Ở Unity, cấu trúc thế giới dựa trên **Entity-Component System (ECS)** cơ bản. 
*   **Unity:** Mỗi cái cây là 1 `GameObject`. Bạn gắn `MeshFilter`, `BoxCollider`, và `TreeScript` vào nó.
*   **Godot:** Không có GameObject. Mọi thứ là **Nodes**. Một cái cây là 1 `Node3D`. Nó chắp thêm con (Child Node) là `MeshInstance3D`, con nữa là `CollisionShape3D`. Script gắn trực tiếp vào Node.

> 💡 **Khẩu quyết ráp não chuyển đổi:** Trong Godot, Component chính là một Child Node!

### Tree Structure (Ví dụ con Player 2D)

**Kiến trúc Unity:**
*   `Player (GameObject)`
    *   `Transform` (Mặc định)
    *   `SpriteRenderer`
    *   `BoxCollider2D`
    *   `PlayerMovement.cs`

**Kiến trúc Godot:**
*   `CharacterBody2D (Root Node) - [Gắn Script PlayerMovement.gd]`
    *   `Sprite2D (Child Node)`
    *   `CollisionShape2D (Child Node)`
    *   `Camera2D (Child Node)`

---

## 🎬 2. Prefabs (Unity) là Scenes (Godot)

Trong Unity, bạn lưu Player thành 1 file `.prefab`. Sau đó kéo nó vào Scene "Level_1".
Trong Godot, **Mọi thứ đều là Scene**.
*   Con Player là 1 Scene riêng biệt (`Player.tscn`).
*   Khẩu súng là 1 Scene (`Gun.tscn`).
*   Màn chơi cũng là 1 Scene (`Level1.tscn`).

Trò chơi Godot thực chất là một "Scene khổng lồ" lồng ghép chứa hàng trăm "Scene nhỏ" gọi là **Instancing**. Tính kế thừa (Inheritance) của Scene ở Godot bá đạo hơn Prefab Variant của Unity rất nhiều. Bạn có thể tạo 1 Scene `MonsterBase.tscn` và sinh ra `FireMonster.tscn` kế thừa nó.

---

## ⌨️ 3. Ngôn ngữ: C# vs GDScript

Godot 4 hỗ trợ C# siêu mạnh (chuẩn .NET 8). Gần như bạn copy Script từ Unity sang chỉ đổi API. Tuy nhiên, GDScript (giống Python) mới là linh hồn của Godot vì nó compile nhanh như chớp.

### Bảng Từ Điển API (Rosetta Stone)

| Khái niệm trong Unity (C#) | Khái niệm trong Godot (GDScript) | Khái niệm trong Godot (C#) |
| :--- | :--- | :--- |
| `void Start()` | `func _ready():` | `public override void _Ready()` |
| `void Update()` | `func _process(delta):` | `public override void _Process(double delta)` |
| `void FixedUpdate()`| `func _physics_process(delta):`| `public override void _PhysicsProcess(double delta)` |
| `GameObject.Find()` | `$ChildNodeName` hoặc `get_node("ChildNode")`| `GetNode<Node3D>("ChildNodeName")` |
| `GetComponent<Rigidbody>()`| Gọi thằng con: `$RigidBody3D` | Tham chiếu trực tiếp Node Con |
| `Instantiate(prefab)` | `preload("res://Enemy.tscn").instantiate()` | `GD.Load<PackedScene>("res://Enemy.tscn").Instantiate()`|
| `Destroy(gameObject)` | `queue_free()` | `QueueFree()` |
| `[SerializeField]` | `@export` | `[Export]` |
| `Debug.Log("Hello");` | `print("Hello")` | `GD.Print("Hello");` |

---

## 📡 4. Tạm Biệt `Events/Delegates`, Xin Chào `Signals`

Hệ thống giao tiếp giữa các Object trong Godot ăn đứt Unity Event Action. Mọi Node trong Godot đều có thể phát tín hiệu (Emit Signals) và kết nối (Connect) dễ dàng qua Giao diện hoặc Code.

**Ví dụ: Khi viên đạn trúng đích, gọi Player tăng điểm:**

Unity (C# Delegate):
```csharp
public event Action OnEnemyKilled;
// Bên Player: Enemy.OnEnemyKilled += AddScore;
```

Godot (GDScript Signals):
```gdscript
signal enemy_killed(points) # Khai báo Signal

func die():
    enemy_killed.emit(100) # Bắn tín hiệu
```
Ở bên giao diện Editor Godot, bạn chỉ cần click tab "Node", kéo signal `enemy_killed` thả vào Player script là xong!

---

## ⚖️ 5. Khi nào chốt hạ chọn Godot thay vì Unity? (2026 Edition)

**NẾU BẠN NÊN GIỮ LẠI UNITY:**
*   Bạn nhắm làm game Console (PS5/Xbox). Unity/Unreal pipeline porting console trơn tru hơn nhiều.
*   Bạn phát triển game Mobile F2P cắm đầy các loại SDK Quảng cáo (Admob/IronSource), SDK Analytics của bên thứ 3. (Hệ sinh thái Plugin Unity vẫn là vô đối).
*   Bạn làm VR/AR (Native Meta Quest SDK viết cốt cho Unity).

**NẾU BẠN NÊN ĐỔI QUA GODOT:**
*   Bạn làm Game 2D Pixel Art: Godot có Engine 2D native (đơn vị tọa độ là pixel), không phải là engine 3D lừa thị giác ép dẹt như Unity (đơn vị là meter). Làm Pixel-perfect siêu đỉnh.
*   Bạn là Solo/Indie Dev làm game bán qua Steam. Godot build siêu lẹ, app nặng chưa tới 100MB (chẳng bù Unity bèo nhất 1-2GB setup).
*   Bạn xài Linux, hoặc thích sự gọn nhẹ (Cả cái Godot Engine nặng 80MB không cần cài ráp). Open Source xài trọn đời không lo kiện tụng License.
