# ↩️ Backtracking: The Art of Trying Every Possibility

> [← Back to DSA Roadmap](./README.md)

Quay lui (Backtracking) là một chiến lược giải quyết vấn đề bằng cách **thử mọi khả năng** cho đến khi tìm được lời giải. Nếu một bước đi không dẫn tới kết quả, ta **quay lại** bước trước đó và thử một lựa chọn khác.

---

## 1. Bản chất của Backtracking
Đây là một biến thể của DFS (Duyệt theo chiều sâu) trên cây không gian trạng thái (State Space Tree).

### 🏗️ Ba thành phần của một hàm Backtracking:
1.  **Choice (Lựa chọn):** Bước tiếp theo bạn định đi.
2.  **Constraint (Ràng buộc):** Bước đi này có hợp lệ không? (Ví dụ: đặt quân Hậu vào ô không bị ăn).
3.  **Goal (Đích):** Bạn đã hoàn thành nhiệm vụ chưa? (Ví dụ: đã đặt đủ $N$ quân Hậu).

---

## 🛠️ Các bài toán kinh điển (Patterns)

### 1. Permutations & Subsets (Hoán vị & Tập con)
Tạo ra mọi cách sắp xếp các phần tử hoặc mọi tập hợp con.
*   *Tình huống:* Tìm mọi tổ hợp mật khẩu có 6 chữ số.

### 2. N-Queens (Quân Hậu)
Đặt $N$ quân Hậu lên bàn cờ $N \times N$ sao cho không có hai quân nào ăn nhau.
*   *Chiến lược:* Thử đặt một quân ở hàng $i$. Nếu được, đệ quy sang hàng $i+1$. Nếu không được, bỏ quân đó ra (backtrack) và thử cột khác.

### 3. Sudoku Solver
Giải bảng Sudoku 9x9 bằng cách điền số từ 1 đến 9 vào ô trống. Nếu sai, xóa đi và thử số khác.

### 4. Word Search
Tìm một từ trong ma trận ký tự bằng cách di chuyển 4 hướng. Đừng quên đánh dấu ô đã đi qua để không quay lại.

---

## 💡 Tối ưu: Cắt tỉa (Pruning)
Càng sớm loại bỏ các nhánh không dẫn tới kết quả, thuật toán càng nhanh.
*   *Ví dụ:* Nếu tổng các số đã chọn lớn hơn mục tiêu, đừng thử thêm bất kỳ số nào nữa. Hãy quay lại ngay lập tức!

---

## 💡 So sánh: Backtracking vs Brute Force

| Đặc điểm | Brute Force (Vét cạn) | Backtracking (Quay lui) |
| :--- | :--- | :--- |
| **Chiến thuật** | Thử mọi thứ một cách mù quáng | Thử từng bước và kiểm tra ràng buộc |
| **Hiệu năng** | Rất chậm | Nhanh hơn nhờ cắt tỉa nhánh sai |
| **Cấu trúc** | Vòng lặp lồng nhau | Đệ quy |

---

## 🧠 Mental Model: Đừng đi vào ngõ cụt
Hãy coi Backtracking như việc đi trong một mê cung. Mỗi ngã rẽ là một **Lựa chọn**. Nếu gặp ngõ cụt, bạn quay lại ngã rẽ gần nhất và thử lối khác.

---

## 🚀 Thực hành (LeetCode Tags)
1.  **Basic:** *Permutations, Subsets, Combination Sum.*
2.  **Intermediate:** *Word Search, Palindrome Partitioning.*
3.  **Advanced:** *N-Queens, Sudoku Solver.*

---

## 🔗 Hoàn thành!
Chúc mừng bạn đã đi qua tất cả các nền tảng chính của **Cấu trúc dữ liệu & Giải thuật**. 
👉 Hãy quay lại **[Roadmap chính](./README.md)** để ôn tập và kiểm tra năng lực của mình.
