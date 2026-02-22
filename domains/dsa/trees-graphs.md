# 🌳 Trees & Graphs: The World of Connections

> [← Back to DSA Roadmap](./README.md)

🌌 **Tâm thế:** *"Lặp là cách ta đi qua thế giới. Đệ quy là cách ta định nghĩa thế giới."*

👉 **Phân tích Sâu:** [Cây & Đồ thị qua lăng kính Đệ quy](./trees-graphs-recursion.md) (⭐ **New**)

Cây (Trees) và Đồ thị (Graphs) là những cấu trúc dữ liệu mô phỏng thế giới thực: Từ sơ đồ tổ chức công ty, cấu trúc tệp tin đến mạng xã hội và bản đồ giao thông.

---

## 1. Cây (Trees) - Cấu trúc phân cấp
Cây là đồ thị không có chu trình (No cycles).

### 🌲 Các loại cây phổ biến:
1.  **Binary Search Tree (BST):** Trái < Gốc < Phải. Tìm kiếm, chèn và xóa trong **$O(\log n)$**.
2.  **AVL / Red-Black Tree:** Các cây BST tự cân bằng, đảm bảo hiệu năng trong mọi trường hợp.
3.  **Heap (Priority Queue):** Cây luôn giữ phần tử lớn nhất/nhỏ nhất ở gốc ($O(1)$ access, $O(\log n)$ insert/delete).
4.  **Trie (Prefix Tree):** Dùng cho tìm kiếm từ ngữ (Autocomplete). Tìm một từ có độ dài $L$ trong **$O(L)$**.

### 🛠️ Kỹ thuật tối ưu kinh điển:
1.  **Duyệt cây (Traversals):** In-order (cho BST ra kết quả đã sắp xếp), Pre-order, Post-order.
2.  **Lowest Common Ancestor (LCA):** Tìm tổ tiên chung gần nhất của 2 node.

---

## 2. Đồ thị (Graphs) - Mạng lưới kết nối
Bao gồm các Đỉnh (Vertices) và Cạnh (Edges). Có hướng hoặc vô hướng, có trọng số hoặc không.

### 🛠️ Hai giải thuật tìm kiếm cốt lõi:
1.  **BFS (Breadth-First Search):** Duyệt theo chiều rộng (Queue). **Tìm đường đi ngắn nhất** trong đồ thị không trọng số.
2.  **DFS (Depth-First Search):** Duyệt theo chiều sâu (Stack/Recursion). Dùng để phát hiện chu trình, sắp xếp Topo.

### 🛠️ Các giải thuật tối ưu kinh điển:
1.  **Dijkstra:** Tìm đường đi ngắn nhất trong đồ thị có trọng số dương.
2.  **Bellman-Ford:** Hoạt động cả với trọng số âm.
3.  **Union-Find (DSU):** Quản lý các tập hợp không giao nhau. Dùng để tìm cây khung nhỏ nhất (Kruskal).
4.  **Topological Sort:** Sắp xếp thứ tự công việc (Build pipeline, Course schedule).

---

## 💡 So sánh: BFS vs DFS

| Tiêu chí | BFS (Hàng ngang) | DFS (Hàng dọc) |
| :--- | :--- | :--- |
| **Cấu trúc** | Queue | Stack / Recursion |
| **Mục tiêu** | Tìm đường ngắn nhất | Khám phá mọi ngóc ngách |
| **Bộ nhớ** | Tốn nhiều (Lưu mọi node cùng cấp) | Ít hơn (Lưu đường đi hiện tại) |

---

## 🧠 Mental Model: Mọi thứ đều là Đồ thị
Khi gặp một bài toán có trạng thái (States) và các bước di chuyển (Transitions), hãy nghĩ đến Đồ thị.
*   *Ví dụ:* Giải một mê cung hoặc trò chơi Sudoku thực chất là duyệt đồ thị các trạng thái hợp lệ.

---

## 🚀 Thực hành (LeetCode Tags)
1.  **Trees:** *Maximum Depth of Binary Tree, Invert Binary Tree, Validate Binary Search Tree.*
2.  **BFS/DFS:** *Number of Islands, Flood Fill, Clone Graph.*
3.  **Advanced:** *Course Schedule (Topo Sort), Network Delay Time (Dijkstra).*

---

## 🔗 Tiếp theo
Học cách tối ưu hóa cực đại với **[Dynamic Programming](./dynamic-programming.md)**.
