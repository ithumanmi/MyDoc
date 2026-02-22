# 📈 Longest Increasing Subsequence (LIS): Finding Growth Patterns

> [← Back to Dynamic Programming](./dynamic-programming.md)
> 
> *"Lặp là cách ta đi qua thế giới. Đệ quy là cách ta định nghĩa thế giới. DP là cách ta ghi nhớ thế giới."*

LIS không chỉ là một bài toán mảng; nó là một bài toán về **Sự phát triển (Growth)**. Làm sao để tìm một chuỗi các phần tử tăng dần dài nhất trong một mảng hỗn loạn?

---

## 1. Định nghĩa bài toán (The Core Problem)

Cho một mảng $A$, tìm độ dài của chuỗi con dài nhất mà các phần tử của nó tăng dần (không nhất thiết phải liên tiếp).

### 💡 Tư duy Đệ quy (Defining Growth):
Để tính LIS kết thúc tại vị trí $i$:
*   `LIS(i)` = 1 + max(`LIS(j)`) với mọi $j < i$ và $A[j] < A[i]$.

---

## 2. Từ Đệ quy sang DP (Tabulation)

Dùng một mảng `dp[n]` để lưu "Độ dài LIS kết thúc tại vị trí $i$". 
Độ phức tạp: **$O(n^2)$** (mỗi phần tử duyệt lại tất cả các phần tử trước nó).

### Công thức truy hồi (Transition):
$$dp[i] = 1 + \max(\{dp[j] \mid 0 \le j < i, A[j] < A[i]\} \cup \{0\})$$

---

## 🏗️ 3. Các biến thể kinh điển (Common Variations)

### A. Longest Mountain Subsequence
Tìm chuỗi con tăng dần rồi giảm dần (như một ngọn núi).
*   *Cách giải:* Kết hợp LIS từ trái qua và LIS từ phải qua (Longest Decreasing Subsequence).

### B. Russian Doll Envelopes
Lồng các phong bì (width, height) vào nhau. 
*   *Cách giải:* Sắp xếp theo width (tăng dần), nếu width bằng nhau thì height giảm dần. Sau đó tìm LIS trên height.

### C. Maximum Sum Increasing Subsequence
Tìm tổng lớn nhất thay vì độ dài dài nhất.

---

## 💡 Đột phá Hiệu năng: $O(n \log n)$

Khi mảng quá lớn ($n = 10^5$), thuật toán $O(n^2)$ sẽ bị treo. Lúc này, ta cần dùng một kỹ thuật khác: **Patience Sorting** (Sắp xếp kiên nhẫn).

**Bản chất:** Ta duy trì một mảng `tails` (các phần tử cuối cùng của các LIS có độ dài khác nhau). Khi xét phần tử mới, ta dùng **Binary Search** để cập nhật `tails`. 
=> Kết quả: **$O(n \log n)$** - Một bước nhảy vọt về tốc độ!

---

## 🧠 Mental Model: Đừng so sánh với tất cả (Selective Comparison)

Trong cuộc sống, LIS dạy chúng ta về **Sự kiên nhẫn (Patience)**. Để đạt được một cột mốc mới (độ dài mới), bạn cần tìm một nền tảng (phần tử trước đó) vững chắc nhưng thấp hơn mình. Bạn không cần phải tốt hơn tất cả mọi người; bạn chỉ cần tìm đúng người đi trước để làm bước đệm cho sự phát triển của mình.

---

## 🚀 Thực hành (LeetCode)
*   **Longest Increasing Subsequence:** Bài toán cơ bản (Thử cả 2 cách $O(n^2)$ và $O(n \log n)$).
*   **Russian Doll Envelopes:** Bài toán nâng cao về sắp xếp và LIS.
*   **Longest Arithmetic Subsequence:** Biến thể tìm cấp số cộng.

---

## 🔗 Tiếp theo
Học cách tối ưu hóa các dãy số trong một phạm vi bất kỳ tại **[Range Sum & Interval DP](./range-interval-dp.md)**.
