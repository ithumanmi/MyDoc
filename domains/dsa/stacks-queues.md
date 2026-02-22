# 📚 Stacks & Queues: Order Matters

> [← Back to DSA Roadmap](./README.md)

Ngăn xếp (Stack) và Hàng đợi (Queue) không phải là các cấu trúc lưu trữ phức tạp như Linked List, mà là các **giao diện (Interfaces)** định nghĩa cách thức truy cập dữ liệu.

---

## 1. Ngăn xếp (Stack) - LIFO (Last-In, First-Out)
Cái gì vào sau cùng, cái đó ra đầu tiên. Giống như một chồng đĩa hoặc nút **"Undo"** trên trình duyệt.

### 🛠️ Kỹ thuật tối ưu kinh điển:
1.  **Monotonic Stack (Ngăn xếp đơn điệu):** Duy trì stack luôn tăng hoặc luôn giảm.
    *   *Tình huống:* Tìm phần tử lớn hơn tiếp theo (Next Greater Element). Biến bài toán từ $O(n^2)$ thành $O(n)$.
2.  **Parentheses Matching:** Kiểm tra tính hợp lệ của các dấu đóng mở ngoặc.

### 🏗️ Ứng dụng thực tế:
*   **Hệ thống Undo/Redo:** Lưu các trạng thái thay đổi.
*   **Call Stack:** Cách CPU quản lý các hàm đệ quy.

---

## 2. Hàng đợi (Queue) - FIFO (First-In, First-Out)
Cái gì vào trước, cái đó ra trước. Giống như xếp hàng mua vé.

### 🛠️ Kỹ thuật tối ưu kinh điển:
1.  **Circular Queue:** Dùng mảng cố định để tiết kiệm không gian và tránh phải dịch chuyển phần tử khi xóa đầu hàng.
2.  **Deque (Double-Ended Queue):** Cho phép chèn và xóa ở cả hai đầu. Cực kỳ mạnh mẽ cho bài toán **Sliding Window Maximum**.
3.  **Priority Queue:** Hàng đợi có độ ưu tiên (Học kỹ ở phần [Trees & Graphs](./trees-graphs.md)).

### 🏗️ Ứng dụng thực tế:
*   **Message Brokers:** RabbitMQ, Kafka (Xử lý tác vụ theo thứ tự).
*   **BFS (Breadth-First Search):** Tìm đường đi ngắn nhất trong đồ thị.

---

## 💡 So sánh: Stack vs Queue

| Đặc điểm | Stack | Queue |
| :--- | :--- | :--- |
| **Thứ tự** | LIFO | FIFO |
| **Thao tác chính** | Push / Pop | Enqueue / Dequeue |
| **Giải thuật chính** | DFS (Depth-First Search) | BFS (Breadth-First Search) |

---

## 🧠 Mental Model: Tư duy Lồng nhau (Nested Thinking)
Dùng Stack khi bạn gặp các bài toán có tính chất lồng nhau hoặc cần quay ngược lại trạng thái trước đó.
*   *Gợi ý:* Nếu bài toán có từ khóa "Valid", "Balance", "Nested", hoặc "Undo", hãy nghĩ đến Stack ngay lập tức.

---

## 🚀 Thực hành (LeetCode Tags)
1.  **Stack:** *Valid Parentheses, Min Stack, Daily Temperatures.*
2.  **Queue:** *Implement Stack using Queues, Sliding Window Maximum.*
3.  **Deque:** *Sliding Window Maximum.*

---

## 🔗 Tiếp theo
Học cách giải quyết các bài toán lớn bằng cách chia nhỏ chúng với **[Recursion](./recursion.md)**.
