# 🧶 Longest Common Subsequence (LCS): Finding Hidden Connections

> [← Back to Dynamic Programming](./dynamic-programming.md)
> 
> *"Lặp là cách ta đi qua thế giới. Đệ quy là cách ta định nghĩa thế giới. DP là cách ta ghi nhớ thế giới."*

Nếu Knapsack là về **Lựa chọn**, thì LCS là về **Sự tương đồng**. Làm sao để biết hai chuỗi ký tự, hai đoạn mã, hay hai chuỗi DNA giống nhau đến mức nào? Câu trả lời nằm ở LCS.

---

## 1. Định nghĩa bài toán (The Core Problem)

Cho hai chuỗi $S1$ và $S2$, tìm độ dài của chuỗi con dài nhất xuất hiện trong cả hai theo cùng thứ tự (không nhất thiết phải liên tiếp).

### 💡 Tư duy Đệ quy (Defining Similarity):
Giả sử ta xét ký tự cuối cùng của $S1$ (độ dài $i$) và $S2$ (độ dài $j$):
1.  **Nếu $S1[i] == S2[j]$:** Chắc chắn ký tự này thuộc LCS.
    *   `LCS(i, j) = 1 + LCS(i-1, j-1)`
2.  **Nếu $S1[i] \neq S2[j]$:** LCS có thể nằm ở nửa $S1$ bỏ đi 1 ký tự, HOẶC ở nửa $S2$ bỏ đi 1 ký tự.
    *   `LCS(i, j) = max(LCS(i-1, j), LCS(i, j-1))`

---

## 2. Từ Đệ quy sang DP (Tabulation)

Dùng một bảng `dp[i][j]` để lưu "Độ dài LCS của $S1$ (độ dài $i$) và $S2$ (độ dài $j$)". 
Độ phức tạp: **$O(n \times m)$** (với $n, m$ là độ dài hai chuỗi).

### Công thức truy hồi (Transition):
$$dp[i][j] = \begin{cases} 
1 + dp[i-1][j-1] & \text{nếu } S1[i] == S2[j] \\
\max(dp[i-1][j], dp[i][j-1]) & \text{nếu } S1[i] \neq S2[j] 
\end{cases}$$

---

## 🏗️ 3. Các biến thể kinh điển (Common Variations)

### A. Edit Distance (Levenshtein Distance)
Số bước ít nhất (thêm, xóa, sửa) để biến chuỗi $A$ thành $B$.
*   *Ứng dụng:* Kiểm tra lỗi chính tả (Spell Check), gợi ý từ khi gõ (Autocomplete).

### B. Longest Palindromic Subsequence (LPS)
Chuỗi con đối xứng dài nhất trong chính nó.
*   *Tip:* LCS của chuỗi $S$ và chuỗi đảo ngược $S'$ chính là LPS của $S$.

### C. Diff Tool (Git)
Bạn đã bao giờ tự hỏi làm sao `git diff` biết bạn đã thêm hay xóa dòng nào chưa? 
*   **Bản chất:** `git diff` tìm LCS giữa hai phiên bản tệp tin. Những dòng KHÔNG thuộc LCS chính là những dòng đã bị thay đổi.

---

## 🧠 Mental Model: Tìm sự giao thoa (Finding Intersection)

Trong cuộc sống, LCS dạy chúng ta cách tìm **Điểm chung (Common Ground)**. Khi hai người có quan điểm khác nhau, hãy tìm "LCS" trong hệ giá trị của họ. Đó chính là nền tảng để xây dựng sự thấu hiểu và thỏa hiệp.

---

## 🛠️ Tối ưu không gian (Space Optimization)

Tương tự Knapsack, chúng ta chỉ cần hàng hiện tại và hàng trước đó để tính toán. 
=> Có thể giảm bộ nhớ từ $O(n \times m)$ xuống **$O(\min(n, m))$**.

---

## 🚀 Thực hành (LeetCode)
*   **Longest Common Subsequence:** Bài toán cơ bản.
*   **Edit Distance:** Cực kỳ quan trọng trong xử lý ngôn ngữ tự nhiên (NLP).
*   **Distinct Subsequences:** Một biến thể đếm số lượng cách tạo ra chuỗi.

---

## 🔗 Tiếp theo
Học cách tối ưu hóa các dãy số tăng dần tại **[Longest Increasing Subsequence (LIS)](./lis-pattern.md)**.
