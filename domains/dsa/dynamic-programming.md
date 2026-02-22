# 💎 Dynamic Programming: The Art of Storing Wisdom

> [← Back to DSA Roadmap](./README.md)

Lập trình động (DP) không phải là một thuật toán, mà là một **chiến thuật tối ưu hóa**. Nó đơn giản là giải quyết các bài toán con chồng chéo (Overlapping Subproblems) bằng cách **lưu lại kết quả** để không bao giờ phải tính lại (Memoization/Tabulation).

---

## 1. Hai đặc điểm của một bài toán DP
1.  **Optimal Substructure (Cấu trúc con tối ưu):** Kết quả bài toán lớn được xây dựng từ kết quả bài toán con.
2.  **Overlapping Subproblems (Bài toán con chồng chéo):** Bạn gặp lại cùng một bài toán con nhiều lần.

---

## 🛠️ Hai cách tiếp cận: Bottom-Up vs Top-Down

### A. Top-Down (Memoization) - Đi từ trên xuống
*   Dùng **Đệ quy** + Một bảng nhớ (`HashMap` hoặc `Array`).
*   Dễ viết, trực quan.
*   *Nhược điểm:* Có thể gặp lỗi **Stack Overflow** nếu đệ quy quá sâu.

### B. Bottom-Up (Tabulation) - Đi từ dưới lên
*   Dùng **Vòng lặp** để lấp đầy một bảng kết quả (thường là mảng 1D hoặc 2D).
*   Luôn an toàn hơn về bộ nhớ, thường nhanh hơn một chút.
*   *Lợi thế:* Dễ dàng tối ưu hóa không gian (Space Optimization) từ $O(n^2)$ xuống $O(n)$ bằng cách chỉ giữ lại hàng/cột trước đó.

---

## 🏗️ 1. Các bước giải một bài toán DP (The 5-Step Process)

1.  **Định nghĩa Trạng thái (State):** `dp[i]` đại diện cho cái gì? (Ví dụ: Số cách leo đến bậc thứ $i$).
2.  **Tìm công thức truy hồi (Transition):** `dp[i] = dp[i-1] + dp[i-2]`.
3.  **Xác định Trường hợp cơ sở (Base Case):** `dp[0] = 1, dp[1] = 1`.
4.  **Xác định thứ tự tính toán (Order):** Tính từ $i=2$ đến $n$.
5.  **Trả về kết quả:** `dp[n]`.

---

## 🏗️ 2. Các bài toán kinh điển (Patterns)

### 1. Knapsack (Cái túi)
Chọn một tập hợp các vật phẩm sao cho tổng giá trị lớn nhất mà không vượt quá giới hạn khối lượng.
*   👉 **Chi tiết Pattern:** **[The Knapsack Pattern: Optimization under Constraints](./knapsack-pattern.md)** (⭐ **New**)
*   *Biến thể:* Subset Sum, Coin Change, Partition Equal Subset Sum.

### 2. Longest Common Subsequence (LCS)
Tìm chuỗi con chung dài nhất giữa hai chuỗi.
*   👉 **Chi tiết Pattern:** **[Longest Common Subsequence (LCS): Finding Hidden Connections](./lcs-pattern.md)** (⭐ **New**)
*   *Biến thể:* Edit Distance (Levenshtein Distance) - Dùng trong kiểm tra lỗi chính tả.

### 3. Longest Increasing Subsequence (LIS)
Tìm chuỗi con tăng dài nhất trong một mảng.
*   👉 **Chi tiết Pattern:** **[Longest Increasing Subsequence (LIS): Finding Growth Patterns](./lis-pattern.md)** (⭐ **New**)
*   *Biến thể:* Russian Doll Envelopes, Maximum Sum Increasing Subsequence.

### 4. Kadane's Algorithm
Tìm mảng con có tổng lớn nhất. Đây là DP ở dạng đơn giản nhất ($O(n)$).

### 5. Range & Interval DP
Tối ưu hóa các dãy số trong một phạm vi $[i, j]$ bất kỳ.
*   👉 **Chi tiết Pattern:** **[Range & Interval DP: Optimizing over Sub-intervals](./range-interval-dp.md)** (⭐ **New**)
*   *Biến thể:* Matrix Chain Multiplication, Burst Balloons.

---

## 🛠️ Kỹ thuật tối ưu kinh điển: State Compression
Nếu bạn chỉ cần kết quả của hàng trước đó để tính hàng hiện tại, đừng dùng mảng 2D. Hãy dùng 2 mảng 1D (hoặc thậm chí 1 mảng 1D nếu khéo léo) để giảm bộ nhớ từ **$O(n^2)$** xuống **$O(n)$**.

---

## 🧠 Mental Model: Ma trận Trạng thái (State Matrix)
Hãy coi DP như việc lấp đầy một ma trận. Mỗi ô $(i, j)$ trả lời một câu hỏi: "Kết quả tốt nhất cho bài toán kích thước $i$ và $j$ là gì?".
*   **Chiến thuật:** Luôn bắt đầu từ các trường hợp nhỏ nhất (Base cases) và tìm ra công thức chuyển trạng thái (State Transition Equation).

---

## 🚀 Thực hành (LeetCode Tags)
1.  **Basic:** *Climbing Stairs, House Robber, Coin Change.*
2.  **Strings:** *Longest Palindromic Substring, Word Break.*
3.  **2D DP:** *Unique Paths, Longest Common Subsequence, Edit Distance.*

---

## 🔗 Chúc mừng!
Bạn đã hoàn thành chặng đường cơ bản của **Cấu trúc dữ liệu & Giải thuật**. Hãy quay lại **[Roadmap chính](./README.md)** để ôn tập hoặc thử sức với **[Knowledge Audit](../../case-studies/knowledge-audits/dsa-knowledge-audit.md)**.
