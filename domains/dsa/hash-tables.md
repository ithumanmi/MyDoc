# 🔑 Hash Tables: The Speed of $O(1)$

> [← Back to DSA Roadmap](./README.md)

Bảng băm (Hash Tables) là cấu trúc dữ liệu "ma thuật" nhất. Nó cho phép bạn tìm kiếm, chèn và xóa dữ liệu trong thời gian **hằng số $O(1)$**, bất kể dữ liệu lớn đến đâu.

---

## 1. Cơ chế hoạt động
1.  **Hash Function (Hàm băm):** Chuyển đổi một Key (ví dụ: "John Doe") thành một chỉ số (Index) trong mảng.
2.  **Bucket:** Vị trí lưu trữ giá trị dựa trên chỉ số đó.

---

## ⚠️ Vấn đề Xung đột (Collision Handling)
Hai Key khác nhau có thể băm ra cùng một chỉ số. Đây là lúc cuộc chiến hiệu năng bắt đầu.

### 🛠️ Kỹ thuật giải quyết:
1.  **Chaining (Liên kết):** Mỗi ô trong mảng chứa một Linked List. Nếu trùng, cứ nối thêm vào.
2.  **Open Addressing (Địa chỉ mở):** Nếu ô đó đã có người, hãy tìm ô trống tiếp theo (Linear Probing, Quadratic Probing, Double Hashing).

---

## 🛠️ Kỹ thuật tối ưu kinh điển

### 1. Kỹ thuật "Phòng vé" (Frequency Array)
Nếu Key chỉ là số nhỏ hoặc ký tự (A-Z), hãy dùng mảng `int[]` thay vì `HashMap`. Nó nhanh hơn và tốn ít bộ nhớ hơn rất nhiều.

### 2. Hai mảng/Set (Two-Set Pattern)
Dùng 2 Hash Set để tìm phần tử chung hoặc phần tử khác biệt giữa hai mảng trong $O(n)$.

---

## 💡 Ứng dụng thực tế
*   **Database Indexing:** Tìm bản ghi nhanh chóng.
*   **Caching (Redis):** Lưu trữ Key-Value.
*   **Compiler/Interpreter:** Lưu trữ bảng ký hiệu (Symbol Table) của các biến.

---

## 🧠 Mental Model: Trade-off Space for Time
Hash Table là ví dụ điển hình nhất của việc hy sinh bộ nhớ (RAM) để đổi lấy tốc độ (CPU). Bạn cần một mảng đủ lớn để giảm thiểu xung đột, nhưng mảng càng lớn thì càng lãng phí RAM.

---

## 🚀 Thực hành (LeetCode Tags)
1.  **Basic:** *Two Sum, Contains Duplicate, Valid Anagram.*
2.  **Advanced:** *LRU Cache, Longest Consecutive Sequence.*

---

## 🔗 Tiếp theo
Học cách quản lý sự ưu tiên với **[Heaps](./heaps.md)**.
