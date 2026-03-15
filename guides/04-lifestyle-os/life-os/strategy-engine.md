# 4️⃣ Strategy Engine (Động cơ Chiến lược)

> **"Chiến thuật là làm thế nào để thắng trận đánh. Chiến lược là biết trận đánh nào đáng để tham gia."**

## Core Mental Models

### 1. Game Theory (Lý thuyết trò chơi)
*   **Tư duy:** Kết quả của tôi phụ thuộc vào hành động của người khác.
*   **Hành động:** Đặt mình vào vị trí đối thủ để dự đoán nước đi. Tìm kiếm Cân bằng Nash.

### 2. Zero-sum vs Positive-sum
*   **Tư duy:**
    *   Zero-sum: Cạnh tranh miếng bánh cố định (Status game, Chính trị văn phòng). -> Mệt mỏi, kẻ thù nhiều.
    *   Positive-sum: Hợp tác làm bánh to hơn (Kinh doanh, Sáng tạo, Kiến thức). -> Giàu có, bạn bè nhiều.
*   **Hành động:** Chỉ chơi Positive-sum games với những người Positive-sum.

### 3. Prisoner's Dilemma & Tit-for-Tat
*   **Tư duy:** Hợp tác là tối ưu dài hạn, nhưng dễ bị lợi dụng ngắn hạn.
*   **Hành động:** Bắt đầu bằng thiện chí (Hợp tác). Nếu bị phản bội, đáp trả ngay (Răn đe). Nếu đối phương hối lỗi, tha thứ và hợp tác lại.

### 4. Preferential Attachment (Lợi thế kẻ dẫn đầu)
*   **Tư duy:** Người giàu càng giàu thêm. Winner takes all.
*   **Hành động:** Hãy cố gắng trở thành Top 1 trong một ngách nhỏ (Niche) thay vì làm người trung bình trong thị trường lớn. Vị thế số 1 sẽ hút tài nguyên về phía bạn.

---

## 🛠️ Quy trình Chiến lược (Checklist)

1.  **Game Selection:** Tôi đang chơi game gì? Tôi có thể thắng không? Nếu không, tôi có thể đổi game (tạo ngách mới) không?
2.  **Win-Win Check:** Trong mối quan hệ này, cả hai bên có cùng thắng không? Nếu một bên thua, mối quan hệ sẽ không bền.
3.  **Positioning:** Tôi có đang đứng ở vị trí "Hub" (trung tâm kết nối) không?

---

### 🔗 Related Engines
- **Alignment Engine:** Chiến lược chỉ bền nếu game phù hợp vector sống dài hạn → dùng PCA + Regret test trong [Alignment Engine](./alignment-engine.md#🧭-framework-vector-pca) để lọc game độc hại.
- **Leverage Theory:** Khi đã chọn game đúng, kích hoạt đòn bẩy (Code, Media, Capital, People) để giành ưu thế → [Leverage Theory](./leverage-theory.md#⚙️-4-dòng-đòn-bẩy).
