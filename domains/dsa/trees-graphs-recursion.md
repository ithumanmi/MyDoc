# 🌳 Recursive Definition: Trees & Graphs as Self-Similar Worlds

> [← Back to Trees & Graphs](./trees-graphs.md)
> 
> *"Lặp là cách ta đi qua thế giới. Đệ quy là cách ta định nghĩa thế giới."*

Khi áp dụng tư duy này vào Cây (Trees) và Đồ thị (Graphs), chúng ta không còn nhìn thấy các "node" và "cạnh" rời rạc, mà thấy những cấu trúc tự thân mạnh mẽ.

---

## 1. Định nghĩa Cây bằng Đệ quy (Defining a Tree)

Nếu dùng **Lặp (Iteration)**, bạn sẽ thấy Cây là một danh sách các node kết nối với nhau.
Nhưng nếu dùng **Đệ quy (Recursion)**, một Cây được định nghĩa là:
1.  Một **Node gốc (Root)**.
2.  Một tập hợp các **Cây con (Subtrees)**.

### 💡 Tại sao cách nhìn này lại mạnh mẽ?
Vì mọi hàm bạn viết cho Cây đều trở nên cực kỳ đơn giản. Bạn không cần lo lắng về 1000 node; bạn chỉ cần lo cho **1 node hiện tại** và tin rằng đệ quy sẽ giải quyết các cây con.

**Ví dụ: Tính chiều cao của Cây**
```python
def height(node):
    if not node: return 0 # Base case: Thế giới rỗng
    # Định nghĩa: Chiều cao = 1 + Max(chiều cao các con)
    return 1 + max(height(node.left), height(node.right))
```
Bạn không "đi qua" từng node để đếm; bạn **định nghĩa** chiều cao là gì.

---

## 2. Đồ thị (Graphs) - Đệ quy của những trạng thái

Trong Đồ thị, đệ quy (thông qua **DFS**) không chỉ là một thuật toán duyệt, mà là cách ta định nghĩa **"Sự khám phá"**.

*   **Định nghĩa Khám phá:** Khám phá một vùng đất (Graph) là khám phá node hiện tại, sau đó lặp lại hành động khám phá cho tất cả các vùng lân cận chưa biết.

### 🧠 Mental Model: Ma trận Trạng thái (State Space)
Mọi bài toán phức tạp (Sudoku, Mê cung, Cờ vua) đều là Đồ thị của các trạng thái. Đệ quy giúp ta định nghĩa đường đi:
> *"Một đường đi hợp lệ là một bước đi hợp lệ hiện tại, nối tiếp bởi một đường đi hợp lệ từ trạng thái mới."*

---

## 3. Sức mạnh tuyệt đối: Sự Tự tương đồng (Self-Similarity)

Lý do đệ quy thống trị Cây/Đồ thị là vì các cấu trúc này có tính **Tự tương đồng**:
1.  **File System:** Một thư mục (Folder) chứa các file và... các thư mục khác.
2.  **DOM (Web):** Một `<div>` chứa văn bản và... các thẻ HTML khác.
3.  **Decision Tree:** Một quyết định dẫn đến kết quả và... những quyết định mới.

---

## 🎯 Kết luận tối thượng cho Developer

Khi làm việc với Cây và Đồ thị, nếu bạn thấy mình đang viết quá nhiều vòng lặp `for` lồng nhau và biến tạm, hãy dừng lại.

Hãy tự hỏi: **"Bản chất của cấu trúc này là gì? Tôi có thể định nghĩa nó bằng chính nó không?"**

> **"Đừng cố gắng 'đi qua' cây. Hãy định nghĩa cây, và thuật toán sẽ tự hoàn thành."**

---

## 🚀 Thử thách tư duy
Hãy thử viết lại thuật toán **Invert Binary Tree** (Đảo ngược cây nhị phân) chỉ bằng 3 dòng code dựa trên định nghĩa: *"Một cây bị đảo ngược là một cây có gốc giữ nguyên, nhưng hai cây con đã được đảo ngược và hoán đổi vị trí cho nhau."*
