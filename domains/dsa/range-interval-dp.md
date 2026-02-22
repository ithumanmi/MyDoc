# 📏 Range & Interval DP: Optimizing over Sub-intervals

> [← Back to Dynamic Programming](./dynamic-programming.md)
> 
> *"Lặp là cách ta đi qua thế giới. Đệ quy là cách ta định nghĩa thế giới. DP là cách ta ghi nhớ thế giới."*

Trong khi các bài toán DP khác thường xét theo thứ tự từ $0$ đến $n$, thì **Range/Interval DP** lại xét theo **Khoảng (Interval)**: $[i, j]$. Làm sao để tìm kết quả tối ưu cho cả đoạn bằng cách kết hợp các đoạn con?

---

## 1. Định nghĩa bài toán (The Core Problem)

Bạn cần giải một bài toán trên đoạn $[i, j]$. 
**Ý tưởng:** Chia đoạn $[i, j]$ thành hai phần tại điểm $k$ ($i \le k < j$) và kết hợp kết quả của $[i, k]$ và $[k+1, j]$.

### 💡 Tư duy Đệ quy (Defining the Range):
`Solve(i, j)` = $\min/\max$ ( `Solve(i, k)` + `Solve(k+1, j)` + `Chi phí kết hợp` ) cho mọi $k \in [i, j-1]$.

---

## 2. Từ Đệ quy sang DP (Tabulation)

Dùng một bảng `dp[n][n]` để lưu "Kết quả tối ưu cho đoạn từ $i$ đến $j$". 
Độ phức tạp: **$O(n^3)$** (duyệt độ dài đoạn, duyệt điểm đầu $i$, duyệt điểm chia $k$).

### Cách lấp đầy bảng (Order of Computation):
Ta không thể duyệt $i, j$ thông thường. Ta phải duyệt theo **Độ dài đoạn (Length)** từ nhỏ đến lớn:
1.  Đoạn độ dài 1: `dp[i][i]`.
2.  Đoạn độ dài 2: `dp[i][i+1]`.
3.  ... cho đến đoạn độ dài $n$.

---

## 🏗️ 3. Các bài toán kinh điển (Patterns)

### A. Matrix Chain Multiplication (Nhân ma trận liên tiếp)
Tìm thứ tự nhân các ma trận sao cho số phép nhân là ít nhất.
*   *Bản chất:* Tìm cách đặt dấu ngoặc $[(A \times B) \times C]$ hay $[A \times (B \times C)]$.

### B. Burst Balloons (Bắn bóng bay)
Bắn bóng bay thứ $i$ sẽ nhận được điểm dựa trên hai bóng láng giềng.
*   *Mẹo:* Thay vì nghĩ bóng nào bắn trước, hãy nghĩ bóng nào bắn **cuối cùng** trong đoạn $[i, j]$.

### C. Optimal Binary Search Tree
Xây dựng cây nhị phân tìm kiếm sao cho chi phí tìm kiếm trung bình là thấp nhất.

---

## 🧠 Mental Model: Đừng chia rẽ, hãy kết hợp (Building from Inside Out)

Range DP dạy chúng ta cách xây dựng một hệ thống từ **Bên trong ra ngoài (Inside-out)**. Thay vì nhìn từ đầu đến cuối một cách tuyến tính, ta nhìn vào sự tương tác giữa các thành phần con trong một phạm vi hẹp và dần dần mở rộng phạm vi đó.

Trong cuộc sống, đây là cách ta xây dựng **Sự đồng thuận (Consensus)**. Bắt đầu từ những nhóm nhỏ ($[i, k]$ và $[k+1, j]$), tìm tiếng nói chung để hợp nhất chúng thành một tập thể lớn hơn.

---

## 🚀 Thực hành (LeetCode)
*   **Matrix Chain Multiplication:** Bài toán kinh điển nhất.
*   **Burst Balloons:** Một bài toán nâng cao về tư duy đệ quy ngược.
*   **Minimum Score Triangulation of Polygon:** Ứng dụng trong hình học.

---

## 🔗 Chúc mừng!
Bạn đã nắm vững toàn bộ các **DP Patterns** kinh điển. Hãy áp dụng chúng vào thực tế tại **[Knowledge Audit](../../case-studies/knowledge-audits/dsa-knowledge-audit.md)**.
