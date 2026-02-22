# 🎒 The Knapsack Pattern: Optimization under Constraints

> [← Back to Dynamic Programming](./dynamic-programming.md)
> 
> *"Lặp là cách ta đi qua thế giới. Đệ quy là cách ta định nghĩa thế giới. DP là cách ta ghi nhớ thế giới."*

Bài toán Cái túi (Knapsack) là "ông tổ" của các bài toán tối ưu hóa có ràng buộc. Nó dạy chúng ta cách đưa ra lựa chọn tốt nhất khi nguồn lực (thời gian, tiền bạc, không gian) là hữu hạn.

---

## 1. Định nghĩa bài toán (The Core Problem)

Bạn có một cái túi có sức chứa tối đa là $W$. Có $n$ món đồ, mỗi món có giá trị $v_i$ và trọng lượng $w_i$.
**Mục tiêu:** Chọn các món đồ sao cho tổng giá trị lớn nhất mà tổng trọng lượng không vượt quá $W$.

### 💡 Tư duy Đệ quy (Defining the Choice):
Tại mỗi món đồ thứ $i$, bạn chỉ có 2 lựa chọn:
1.  **Bỏ qua món đồ $i$:** Giá trị tốt nhất = Giá trị tốt nhất khi xét $i-1$ món đồ với cùng sức chứa $W$.
2.  **Lấy món đồ $i$ (nếu $w_i \le W$):** Giá trị tốt nhất = $v_i$ + Giá trị tốt nhất khi xét $i-1$ món đồ với sức chứa còn lại $(W - w_i)$.

---

## 2. Từ Đệ quy sang DP (Memoization)

Nếu dùng đệ quy thuần túy, bạn sẽ tính lại cùng một cặp $(i, W)$ rất nhiều lần (Overlapping Subproblems) -> $O(2^n)$.
Bằng cách dùng một bảng `dp[i][j]` để lưu "Giá trị lớn nhất khi xét $i$ món đồ đầu tiên với sức chứa $j$", ta giảm xuống còn **$O(n \times W)$**.

### Công thức truy hồi (Transition):
$$dp[i][j] = \max(dp[i-1][j], v_i + dp[i-1][j - w_i] \text{ nếu } w_i \le j)$$

---

## 🏗️ 3. Các biến thể kinh điển (Common Variations)

### A. 0/1 Knapsack (Mỗi món đồ chỉ có 1)
Đây là dạng cơ bản nhất. Bạn không thể chia nhỏ món đồ.
*   *Ứng dụng:* Chọn dự án đầu tư, chọn hành lý đi máy bay.

### B. Unbounded Knapsack (Số lượng đồ vô hạn)
Bạn có thể lấy một món đồ nhiều lần tùy thích.
*   *Ứng dụng:* Bài toán đổi tiền (Coin Change) - Làm sao để đổi $S$ đồng bằng ít tờ tiền nhất.

### C. Bounded Knapsack (Mỗi món đồ có số lượng giới hạn $k_i$)
*   *Ứng dụng:* Quản lý kho hàng thực tế.

---

## 🧠 Mental Model: Đừng nhìn toàn cục, hãy nhìn vào lựa chọn cuối cùng

Bí quyết của Knapsack (và hầu hết bài toán DP) là: **"Nếu tôi biết kết quả tối ưu của mọi bài toán nhỏ hơn, tôi có thể dễ dàng quyết định cho bước hiện tại."**

Trong cuộc sống, Knapsack dạy chúng ta về **Chi phí cơ hội (Opportunity Cost)**. Khi bạn chọn làm việc A, bạn đang hy sinh không gian trong "cái túi thời gian" của mình cho việc B. DP giúp bạn định lượng sự hy sinh đó để đảm bảo tổng giá trị đời mình là lớn nhất.

---

## 🛠️ Tối ưu không gian (Space Optimization)

Bạn có nhận thấy để tính hàng `i`, chúng ta chỉ cần dữ liệu từ hàng `i-1`? 
=> Ta có thể dùng mảng 1D `dp[W]` và duyệt ngược để tiết kiệm bộ nhớ từ $O(n \times W)$ xuống **$O(W)$**.

---

## 🚀 Thực hành (LeetCode)
*   **Partition Equal Subset Sum:** Biến thể của 0/1 Knapsack.
*   **Coin Change:** Biến thể của Unbounded Knapsack.
*   **Target Sum:** Một bài toán Knapsack được "ngụy trang" khéo léo.

---

## 🔗 Tiếp theo
Học cách so sánh sự tương đồng giữa hai thế giới tại **[Longest Common Subsequence (LCS)](./lcs-pattern.md)**.
