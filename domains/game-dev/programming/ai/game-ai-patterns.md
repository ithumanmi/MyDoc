# 🧠 Game AI: Thổi hồn cho NPC (Level 9)

> [← Back to Game Development Roadmap](../README.md)

AI trong Game không cần "thông minh" như ChatGPT. Nó cần "hành xử thú vị" để người chơi tiêu diệt.

---

## 1. Finite State Machine (FSM - Máy trạng thái hữu hạn)

Mô hình AI đơn giản nhất, phổ biến nhất.

### **Cơ chế:**
*   NPC chỉ ở một trạng thái tại một thời điểm: `Idle` (Đứng yên), `Patrol` (Tuần tra), `Chase` (Đuổi theo), `Attack` (Tấn công).
*   **Chuyển đổi (Transition):**
    *   Nếu đang `Patrol` mà nhìn thấy Player -> Chuyển sang `Chase`.
    *   Nếu đang `Chase` mà Player chạy xa quá -> Chuyển về `Patrol`.

### **Nhược điểm:**
*   Khi AI quá phức tạp (50 trạng thái), FSM trở thành "mớ bòng bong" (Spaghetti code) khó bảo trì.

---

## 2. Behavior Trees (Cây hành vi)

Mô hình AI hiện đại, linh hoạt (Dùng trong Halo, Uncharted).

### **Cấu trúc Cây:**
*   **Root:** Gốc cây.
*   **Composite Node (Nút điều khiển):**
    *   *Sequence (Tuần tự):* Làm A -> Xong thì làm B -> Xong thì làm C. (Ví dụ: Tìm chỗ nấp -> Chạy đến -> Bắn).
    *   *Selector (Lựa chọn):* Thử làm A -> Nếu thất bại thì làm B. (Ví dụ: Bắn súng -> Hết đạn thì rút dao).
*   **Leaf Node (Lá):** Hành động cụ thể (Di chuyển, Bắn, Thay đạn).

---

## 3. GOAP (Goal-Oriented Action Planning)

AI tự lập kế hoạch (Dùng trong F.E.A.R).

*   **Mục tiêu (Goal):** "Giết người chơi".
*   **Hành động (Action):** Có thể bắn, có thể ném lựu đạn, có thể đi.
*   **Lập kế hoạch:** AI tự tìm chuỗi hành động tối ưu để đạt mục tiêu.
    *   Ví dụ: Súng hết đạn -> Cần thay đạn -> Nhưng không có đạn -> Cần đi tìm đạn -> Tìm thấy đạn -> Thay đạn -> Bắn.

---

## 5. Behavior Tree Deep Dive (Hướng dẫn chuyên sâu)

FSM rất tốt, nhưng với những con Boss phức tạp, bạn cần Behavior Tree.
Xem hướng dẫn chi tiết tại: **[Behavior Tree Guide](./behavior-tree/core-concepts.md)**

*   **[Custom Implementation](./behavior-tree/custom-implementation.md):** Tự viết hệ thống BT bằng C#.
*   **[Visual Editor](./behavior-tree/visual-editor.md):** Tạo công cụ kéo thả Node bằng Unity GraphView.
*   **[Boss AI Example](./behavior-tree/boss-ai-example.md):** Thiết kế AI cho Boss "The Dark Knight".
