# 🔍 Sorting & Searching: The Algorithms that Run the Web

> [← Back to DSA Roadmap](./README.md)

Sắp xếp và Tìm kiếm là hai bài toán phổ biến nhất trong mọi hệ thống. Hiệu năng của cơ sở dữ liệu (Indexes) và các công cụ tìm kiếm (Google, Bing) đều dựa trên các nguyên tắc cơ bản này.

---

## 1. Tìm kiếm (Searching)
1.  **Linear Search ($O(n)$):** Duyệt qua mọi phần tử. Chỉ dùng cho dữ liệu chưa sắp xếp và kích thước nhỏ.
2.  **Binary Search ($O(\log n)$):** Phân chia không gian tìm kiếm làm đôi mỗi bước. Chỉ hoạt động trên dữ liệu **đã sắp xếp**.

### 🛠️ Kỹ thuật tối ưu kinh điển:
1.  **Binary Search trên đáp án (Binary Search on Answer):** Thay vì tìm một giá trị trong mảng, ta tìm giá trị tối ưu (lớn nhất/nhỏ nhất) trong một dải kết quả có thể có.
    *   *Tình huống:* Chia $K$ quyển sách cho $M$ người sao cho số trang tối đa một người phải đọc là nhỏ nhất.

---

## 2. Sắp xếp (Sorting)
1.  **Sắp xếp cơ bản ($O(n^2)$):** Bubble Sort, Insertion Sort, Selection Sort. Chỉ dùng để học hoặc cho mảng cực nhỏ (< 20 phần tử).
2.  **Sắp xếp tối ưu ($O(n \log n)$):** [QuickSort](./quicksort-divide-conquer.md), [Merge Sort](./merge-sort-recursion.md), Heap Sort. Đây là những gì các hàm `sort()` hiện đại sử dụng.

### 💡 So sánh:
*   **[QuickSort](./quicksort-divide-conquer.md):** Thường nhanh nhất trong thực tế. Đỉnh cao của triết lý **Phân chia & Cai trị** bằng đệ quy. Nhược điểm: Có thể rơi vào $O(n^2)$ nếu chọn "pivot" tệ.
*   **[Merge Sort](./merge-sort-recursion.md):** Luôn là $O(n \log n)$, cực kỳ ổn định (Stable). Đỉnh cao của sự **Hợp nhất (Combine)**. Nhược điểm: Tốn thêm $O(n)$ bộ nhớ.

---

## 🛠️ Kỹ thuật tối ưu kinh điển

### 1. Counting Sort / Bucket Sort ($O(n + k)$)
Phá vỡ giới hạn $O(n \log n)$ bằng cách không dùng phép so sánh. Chỉ hoạt động khi bạn biết trước dải giá trị của dữ liệu (ví dụ: điểm thi từ 0 đến 10).

### 2. K-th Largest Element (Quick Select)
Tìm phần tử lớn thứ $K$ trong $O(n)$ thời gian thay vì $O(n \log n)$ bằng cách dùng tư duy của Quick Sort.

---

## 🧠 Mental Model: Hiệu năng thực tế vs Lý thuyết
Dù $O(n \log n)$ là giới hạn lý thuyết cho sắp xếp dựa trên so sánh, nhưng các thư viện hiện đại (như Python's Timsort) thường kết hợp nhiều thuật toán để tận dụng các mảng đã được sắp xếp một phần.

---

## 🚀 Thực hành (LeetCode Tags)
1.  **Binary Search:** *Binary Search, Search in Rotated Sorted Array, First Bad Version.*
2.  **Sorting:** *Merge Intervals, Sort Colors, Kth Largest Element in an Array.*
3.  **Binary Search on Answer:** *Koko Eating Bananas, Capacity To Ship Packages Within D Days.*

---

## 🔗 Tiếp theo
Học cách quản lý dữ liệu phân cấp và mạng lưới với **[Trees & Graphs](./trees-graphs.md)**.
