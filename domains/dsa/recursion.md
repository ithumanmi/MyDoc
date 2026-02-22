# 🔄 Recursion: Thinking in Patterns

> [← Back to DSA Roadmap](./README.md)

🌌 **Tâm thế:** *"Lặp là cách ta đi qua thế giới. Đệ quy là cách ta định nghĩa thế giới."*

👉 **Tư duy Đệ quy (Mental Model):** [Từ Code đến Đời sống: Nhìn thấu bản chất của hệ thống](../../guides/01-mental-models/recursive-thinking.md) (⭐ **New**)

👉 **Phân tích Triết học:** [Lặp vs. Đệ quy: Hai cách nhìn, một bản chất](./iteration-vs-recursion.md) (⭐ **New**)

👉 **Phân tích Toán học:** [Tại sao người giỏi Toán thích Đệ quy?](./why-mathematicians-love-recursion.md) (⭐ **New**)

👉 **Kiệt tác Đệ quy:** [Tháp Hà Nội, Hàm Ackermann & Fractals](./recursive-masterpieces.md) (⭐ **New**)

👉 **Phân chia & Cai trị:** [QuickSort: Đỉnh cao của Đệ quy Sắp xếp](./quicksort-divide-conquer.md) (⭐ **New**)

👉 **Sự Hợp nhất Hoàn hảo:** [Merge Sort: Đệ quy của sự Ổn định](./merge-sort-recursion.md) (⭐ **New**)

Đệ quy (Recursion) không phải là một cấu trúc dữ liệu, mà là một **phương pháp giải quyết vấn đề**. Nó giúp chia một bài toán khổng lồ thành nhiều bài toán nhỏ hơn cùng loại.

---

## 1. Công thức cơ bản của Đệ quy
Bất kỳ một hàm đệ quy nào cũng phải có 2 thành phần:
1.  **Base Case (Trường hợp cơ sở):** Điều kiện dừng. Nếu không có cái này, bạn sẽ gặp lỗi **Stack Overflow**.
2.  **Recursive Step (Bước đệ quy):** Gọi lại chính nó với dữ liệu nhỏ hơn hoặc đơn giản hơn.

---

## 🛠️ Kỹ thuật tối ưu kinh điển

### 1. Memoization (Ghi nhớ)
Lưu kết quả của các bài toán con đã giải để không phải tính lại.
*   *Tình huống:* Tính Fibonacci. Đệ quy thường tốn **$O(2^n)$**, có Memoization giảm xuống **$O(n)$**.

### 2. Tail Recursion (Đệ quy đuôi)
Thực hiện phép tính cuối cùng trước khi gọi đệ quy. Một số ngôn ngữ (như Scala hay Haskell) tối ưu cái này thành vòng lặp `while` để tiết kiệm bộ nhớ.

---

## 💡 Tư duy: Chia để trị (Divide and Conquer)
Đây là pattern phổ biến nhất của đệ quy:
1.  **Divide:** Chia bài toán thành 2 hoặc nhiều bài toán con.
2.  **Conquer:** Giải các bài toán con đó (thường bằng đệ quy).
3.  **Combine:** Kết hợp kết quả các bài toán con để có kết quả bài toán gốc.
*   *Ví dụ điển hình:* Merge Sort, Quick Sort, Binary Search.

---

## 🧠 Mental Model: Call Stack (Chồng hàm)
Khi một hàm gọi đệ quy, nó không "biến mất". Nó nằm lại trong bộ nhớ (Stack) và chờ hàm con trả về giá trị.
*   **Chi phí:** Đệ quy tốn bộ nhớ hơn vòng lặp vì mỗi lần gọi đều cần tạo một "Stack Frame".
*   **Lời khuyên:** Nếu bài toán có thể giải bằng vòng lặp đơn giản (Iterative), hãy dùng vòng lặp. Nhưng với Cây (Trees) và Đồ thị (Graphs), đệ quy thường làm code sạch hơn 10 lần.

---

## ⚠️ Cạm bẫy của Đệ quy
1.  **Stack Overflow:** Do đệ quy quá sâu hoặc thiếu điều kiện dừng.
2.  **Tính toán thừa:** Không dùng Memoization cho các bài toán con chồng chéo (Overlapping subproblems).

---

## 🚀 Thực hành (LeetCode Tags)
1.  **Basic:** *Fibonacci, Reverse String.*
2.  **Divide & Conquer:** *Merge Sort, Quick Sort, Binary Search.*
3.  **Advanced:** *Pow(x, n), Climbing Stairs.*
4.  **🌌 Expert (Math Recursion):** **[Ramanujan Recursion & Number Theory](./math-recursion-ramanujan.md)** (⭐ **New**)

---

## 🔗 Tiếp theo
Học cách sắp xếp và tìm kiếm dữ liệu hiệu quả với **[Sorting & Searching](./sorting-searching.md)**.
