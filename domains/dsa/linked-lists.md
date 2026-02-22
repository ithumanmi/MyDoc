# 🔗 Linked Lists: Dynamic Connections

> [← Back to DSA Roadmap](./README.md)

Danh sách liên kết (Linked List) là cấu trúc dữ liệu dùng để vượt qua nhược điểm của Mảng: **Chi phí chèn/xóa ở đầu hoặc giữa rất đắt đỏ**. Với Linked List, bạn chỉ cần thay đổi "địa chỉ trỏ tới" là xong.

---

## 1. Các loại Linked List
1.  **Singly Linked List:** Mỗi node chỉ biết node tiếp theo (`next`).
2.  **Doubly Linked List:** Mỗi node biết cả node trước (`prev`) và sau (`next`). Tốn bộ nhớ hơn nhưng linh hoạt hơn.
3.  **Circular Linked List:** Node cuối trỏ ngược lại node đầu. Thường dùng trong các giải thuật lập lịch vòng tròn (Round Robin).

---

## 🛠️ Kỹ thuật tối ưu kinh điển

### 1. Fast & Slow Pointers (Kỹ thuật Rùa và Thỏ)
Dùng hai con trỏ di chuyển với tốc độ khác nhau.
*   **Tìm trung điểm:** Thỏ đi 2 bước, Rùa đi 1 bước. Khi Thỏ đến cuối, Rùa đang ở giữa.
*   **Phát hiện chu trình (Cycle Detection):** Nếu có vòng lặp, Thỏ cuối cùng sẽ đuổi kịp Rùa.

### 2. Dummy Node (Node giả)
Tạo một node trống đứng trước `head`.
*   **Lợi ích:** Tránh các trường hợp biên (edge cases) khi phải xóa node đầu tiên hoặc khi danh sách rỗng. Code sẽ sạch hơn rất nhiều.

### 3. Đảo ngược danh sách (Reversing)
Một thao tác cơ bản nhưng cực kỳ quan trọng để luyện tập tư duy về sự thay đổi của con trỏ.

---

## 💡 So sánh: Linked List vs Array

| Tiêu chí | Array | Linked List |
| :--- | :--- | :--- |
| **Truy cập (Access)** | $O(1)$ | $O(n)$ |
| **Chèn/Xóa ở đầu** | $O(n)$ | **$O(1)$** |
| **Bộ nhớ (Memory)** | Liên tục (Cache friendly) | Phân tán (Pointer overhead) |
| **Kích thước** | Cố định (Fix-sized) | Linh hoạt (Dynamic) |

---

## 🧠 Mental Model: Tư duy Con trỏ (Pointer Thinking)
Khi làm việc với Linked List, hãy luôn vẽ ra giấy.
*   **Nguyên tắc vàng:** Luôn gán con trỏ `next` của node mới trước khi cắt đứt kết nối cũ, nếu không bạn sẽ làm mất địa chỉ của phần còn lại trong danh sách (Memory Leak hoặc Null Pointer).

---

## 🚀 Thực hành (LeetCode Tags)
1.  **Basic:** *Reverse Linked List, Merge Two Sorted Lists.*
2.  **Fast/Slow:** *Linked List Cycle, Middle of the Linked List.*
3.  **Advanced:** *LRU Cache* (Kết hợp Hash Map và Doubly Linked List) - Một bài toán cực kỳ phổ biến trong thiết kế hệ thống.

---

## 🔗 Tiếp theo
Học cách quản lý thứ tự truy cập dữ liệu với **[Stacks & Queues](./stacks-queues.md)**.
