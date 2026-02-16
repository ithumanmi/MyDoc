# 🛠️ Editor Scripting: Tự tạo công cụ cho mình

> [← Back to Game Development Roadmap](../README.md)

Unity không chỉ là Game Engine. Nó là một nền tảng để bạn xây dựng công cụ (Tool) làm game.
Làm Tools tốt giúp Designer (và chính bạn) làm việc nhanh gấp 10 lần.

---

## 1. Custom Inspectors (Tùy biến Inspector)

Giao diện mặc định của Script rất chán. Hãy làm nó đẹp và tiện hơn.

### **Attributes:**
*   `[Header("Stats")]`: Tạo tiêu đề.
*   `[Range(0, 100)]`: Tạo thanh trượt (Slider).
*   `[Tooltip("Máu của nhân vật")]`: Hiện hướng dẫn khi di chuột vào.
*   `[HideInInspector]`: Ẩn biến public không cho sửa.

### **Editor Script:**
*   Tạo file trong thư mục `Editor`.
*   Kế thừa `Editor`.
*   Override hàm `OnInspectorGUI()`.
*   Tự vẽ nút bấm: `if (GUILayout.Button("Attack")) { ... }`.

---

## 2. Editor Windows (Cửa sổ công cụ)

Tạo hẳn một cửa sổ mới như Scene View hay Game View.

### **Ứng dụng:**
*   **Level Editor:** Vẽ map bằng cách click chuột (Tilemap nâng cao).
*   **Item Database:** Quản lý danh sách 1000 item, chỉ số, hình ảnh trong một bảng tính.
*   **Quest Maker:** Giao diện nối các node hội thoại.

---

## 3. Gizmos (Vẽ hỗ trợ)

Vẽ các đường line, hình cầu, hình hộp trong Scene View để dễ debug.

*   `OnDrawGizmos()`: Luôn vẽ.
*   `OnDrawGizmosSelected()`: Chỉ vẽ khi chọn object.
*   Ví dụ: Vẽ vòng tròn tầm nhìn của quái vật, vẽ đường đi dự kiến của đạn.

---

## 4. Automation (Tự động hóa)

*   **AssetPostprocessor:** Tự động chạy code khi bạn import file vào Unity.
    *   Ví dụ: Tự động ném file âm thanh vào thư mục Audio, tự động chỉnh setting texture cho đúng chuẩn.
*   **Build Pipeline:** Viết script để tự động Build ra APK, iOS và PC chỉ với 1 nút bấm (hoặc chạy trên Server CI/CD).
