# 🏔️ Heaps: The Hierarchy of Priority

> [← Back to DSA Roadmap](./README.md)

Đống (Heap) không phải là "đống rác", mà là một cấu trúc dữ liệu cực kỳ có tổ chức. Nó giúp bạn luôn biết ai là người **quan trọng nhất** (hoặc nhỏ nhất) trong một nhóm dữ liệu biến động liên tục.

---

## 1. Heap là gì?
Heap là một cây nhị phân gần như hoàn chỉnh (Complete Binary Tree).

### 🌲 Hai loại Heap chính:
1.  **Max-Heap:** Node gốc (Root) luôn lớn hơn hoặc bằng các con của nó.
2.  **Min-Heap:** Node gốc (Root) luôn nhỏ hơn hoặc bằng các con của nó.

### 🏗️ Tính chất quan trọng:
*   Truy cập phần tử lớn nhất/nhỏ nhất: **$O(1)$**.
*   Chèn và Xóa: **$O(\log n)$**.

---

## 🛠️ Kỹ thuật tối ưu kinh điển

### 1. Priority Queue (Hàng đợi ưu tiên)
Heap là cách cài đặt phổ biến nhất cho Priority Queue.
*   *Tình huống:* Hệ thống cấp cứu trong bệnh viện. Bệnh nhân nặng luôn được khám trước, bất kể họ đến khi nào.

### 2. Heap Sort ($O(n \log n)$)
Sắp xếp dữ liệu bằng cách đưa tất cả vào Heap rồi lần lượt lấy ra. Đây là thuật toán sắp xếp tại chỗ (In-place) cực kỳ ổn định.

### 3. K-th Smallest / Largest Element
Dùng một Heap có kích thước cố định là $K$.
*   Dùng **Max-Heap** để tìm $K$ phần tử nhỏ nhất.
*   Dùng **Min-Heap** để tìm $K$ phần tử lớn nhất.
*   Đây là cách tìm $K$ phần tử tối ưu nhất trong $O(n \log k)$.

---

## 💡 Ứng dụng thực tế
*   **Hệ thống lập lịch CPU:** Chọn tiến trình có độ ưu tiên cao nhất.
*   **Thuật toán Dijkstra:** Tìm đường đi ngắn nhất (chọn node có khoảng cách nhỏ nhất tiếp theo).
*   **Dữ liệu trực tiếp (Streams):** Tìm trung vị (Median) của một dòng dữ liệu đang chảy.

---

## 🧠 Mental Model: Đừng sắp xếp tất cả
Nếu bạn chỉ cần 5 người đứng đầu, đừng sắp xếp cả 1000 người. Hãy dùng một Heap để giữ lại 5 người đó. Tiết kiệm CPU từ $O(n \log n)$ xuống $O(n \log 5)$.

---

## 🚀 Thực hành (LeetCode Tags)
1.  **Basic:** *Kth Largest Element in a Stream, Last Stone Weight.*
2.  **Advanced:** *Merge k Sorted Lists, Find Median from Data Stream.*

---

## 🔗 Tiếp theo
Học cách đưa ra quyết định tối ưu tại mỗi bước với **[Greedy Algorithms](./greedy.md)**.
