# ⚖️ Tools Comparison: Tự viết hay Mua sẵn?

> [← Back to Behavior Tree Fundamentals](./core-concepts.md)

Bạn đã biết cách tự viết BT. Nhưng liệu có đáng thời gian không?

---

## 1. Custom Implementation (Tự viết)

### **Ưu điểm:**
*   **Miễn phí:** Không tốn $50-$100 mua asset.
*   **Kiểm soát 100%:** Bạn hiểu rõ từng dòng code. Dễ dàng debug và tối ưu theo ý thích (ví dụ: tích hợp sâu với hệ thống Skill của game).
*   **Nhẹ:** Không có tính năng thừa.

### **Nhược điểm:**
*   **Tốn thời gian:** Viết Editor Window rất cực (GraphView API khá khó học).
*   **Thiếu tính năng:** Không có sẵn Live Debugging xịn, không có Minimap, Undo/Redo nếu bạn không tự làm.

---

## 2. Opsive Behavior Designer ($80)

Asset chuẩn mực của ngành (Industry Standard).

### **Ưu điểm:**
*   **Tính năng đồ sộ:** Hỗ trợ Conditional Aborts (ngắt hành động giữa chừng), Shared Variables, Task Guard.
*   **Integrations:** Tích hợp sẵn với hàng trăm asset khác (A* Pathfinding, PlayMaker).
*   **Ổn định:** Đã được kiểm chứng qua nhiều năm.

### **Nhược điểm:**
*   **Learning Curve:** Quá nhiều tính năng -> Mới đầu rất ngợp.
*   **Giá:** Khá đắt với sinh viên/indie.

---

## 3. NodeCanvas ($75)

Đối thủ của Opsive.

### **Ưu điểm:**
*   **Đa năng:** Hỗ trợ cả FSM (State Machine) và Dialogue Tree trong cùng một gói.
*   **Giao diện:** Thân thiện, dễ nhìn hơn Opsive (ý kiến cá nhân).

---

## 4. Unity Muse Behavior (Mới)

Giải pháp chính chủ từ Unity (đang ở dạng Package Preview).

### **Ưu điểm:**
*   **Native:** Tích hợp sâu vào Unity Editor.
*   **Data-Oriented:** Tối ưu hiệu năng tốt.
*   **Tương lai:** Sẽ được Unity support dài hạn.

### **Nhược điểm:**
*   **Chưa hoàn thiện:** Còn thiếu tính năng và tài liệu so với Opsive.

---

## 💡 Kết luận

*   **Dùng Custom:** Nếu bạn làm game nhỏ, muốn học sâu về AI, hoặc cần hệ thống siêu tối ưu.
*   **Dùng Opsive/NodeCanvas:** Nếu bạn làm game thương mại quy mô lớn (AA/AAA), có ngân sách, và không muốn tốn 2 tháng để viết tool AI.
