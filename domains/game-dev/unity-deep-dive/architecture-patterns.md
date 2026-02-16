# 🏗️ Advanced Unity Architecture: Xây dựng nền móng vững chắc

> [← Back to Game Development Roadmap](../README.md)

Khi dự án Game lớn lên, code sẽ trở thành "Spaghetti" nếu không có kiến trúc tốt.
Đừng để `GameManager` dài 5000 dòng. Hãy chia nhỏ và cai trị.

---

## 1. ScriptableObjects as Architecture (SO)

ScriptableObjects không chỉ để chứa Data (Stats, Inventory). Nó có thể là **Event Channel**.

### **Game Architecture with ScriptableObjects (Ryan Hipple):**
*   **Biến toàn cục (Global Variables):** Thay vì Singleton, hãy tạo một SO `FloatVariable`. Mọi script đều có thể tham chiếu đến nó.
*   **Event System:** Tạo một SO `GameEvent`.
    *   Script A gọi `GameEvent.Raise()`.
    *   Script B lắng nghe `GameEvent.RegisterListener()`.
    *   -> A và B không cần biết nhau (Decoupling).

### **Lợi ích:**
*   Dễ dàng debug (xem giá trị ngay trong Inspector).
*   Giảm sự phụ thuộc (Dependencies).
*   Dễ dàng thay thế/test (Swap SO khác vào là xong).

---

## 2. Dependency Injection (DI)

Làm sao để Class A dùng Class B mà không cần `FindObjectOfType` hay `GetComponent`?

### **Zenject / VContainer:**
*   **Container:** Nơi đăng ký tất cả các dependency (Service, Manager).
*   **Inject:** Khi một class cần dùng cái gì, chỉ cần khai báo `[Inject]`, Container sẽ tự động đưa vào.

### **Ví dụ:**
```csharp
public class PlayerController : MonoBehaviour {
    [Inject] IInputService _inputService; // Tự động được tiêm vào

    void Update() {
        if (_inputService.IsJumpPressed) Jump();
    }
}
```
*   **Lợi ích:** Dễ dàng Unit Test (Mock input service), code sạch sẽ.

---

## 3. Design Patterns (Mẫu thiết kế)

### **A. Singleton (Đúng cách)**
*   Chỉ dùng cho các Manager thực sự duy nhất (AudioManager, GameManager).
*   Đừng lạm dụng. Singleton làm code bị couple chặt chẽ (Tight Coupling).

### **B. Observer (Quan sát viên)**
*   Dùng C# Events (`Action`, `Func`) hoặc UniRx.
*   Khi máu nhân vật thay đổi -> UI tự cập nhật. UI không cần check máu trong `Update()`.

### **C. Command Pattern**
*   Đóng gói một hành động thành một Object.
*   **Ứng dụng:** Hệ thống Undo/Redo trong game chiến thuật (Turn-based).
*   Lưu lịch sử các Command -> Khi cần Undo, gọi `Command.Undo()`.

### **D. State Pattern**
*   Thay thế các câu lệnh `if/else` hoặc `switch/case` khổng lồ trong FSM.
*   Mỗi trạng thái (Idle, Walk, Jump) là một Class riêng biệt.
