# 📊 Complexity Analysis: Big O & Beyond

> [← Back to DSA Roadmap](./README.md)

Hiểu về độ phức tạp không chỉ để trả lời phỏng vấn, mà là để biết **giới hạn vật lý** của giải pháp bạn đang viết.

---

## 1. Ba thước đo chính
1.  **Big O ($O$):** Giới hạn trên (Upper bound) - Trường hợp xấu nhất. Đây là cái chúng ta quan tâm nhất.
2.  **Big Omega ($\Omega$):** Giới hạn dưới (Lower bound) - Trường hợp tốt nhất.
3.  **Big Theta ($\Theta$):** Giới hạn chặt (Tight bound) - Khi $O$ và $\Omega$ trùng nhau.

---

## 2. Các cấp độ "Tốc độ" (Visualizing Growth)

| Complexity | Name | Thang đo thực tế |
| :--- | :--- | :--- |
| **$O(1)$** | Constant | Truy cập ID khách hàng bằng Hash Map. |
| **$O(\log n)$** | Logarithmic | Tìm kiếm một từ trong từ điển (Binary Search). |
| **$O(n)$** | Linear | Duyệt qua danh sách email để tìm spam. |
| **$O(n \log n)$** | Linearithmic | Tốc độ của các thuật toán sắp xếp tối ưu (Merge Sort). |
| **$O(n^2)$** | Quadratic | So sánh mọi cặp sản phẩm trong giỏ hàng (Nested loops). |
| **$O(2^n)$** | Exponential | Thử mọi tổ hợp mật khẩu (Brute-force). |
| **$O(n!)$** | Factorial | Bài toán người du lịch (TSP) - Tìm đường đi qua mọi thành phố. |

---

## 3. Tư duy Tối ưu (The Optimization Mindset)

### A. Trade-off: Time vs Space
Đôi khi ta hy sinh RAM (Space) để lấy Tốc độ (Time).
*   **Ví dụ:** Dùng một `HashSet` để lưu các phần tử đã thấy ($O(n)$ space) giúp kiểm tra trùng lặp trong $O(1)$ thay vì phải dùng 2 vòng lặp ($O(n^2)$ time).

### B. Amortized Analysis (Độ phức tạp khấu hao)
Một thao tác có thể rất đắt đỏ một lần, nhưng nếu nó hiếm khi xảy ra và các thao tác khác rất rẻ, trung bình nó vẫn rẻ.
*   **Ví dụ:** `ArrayList` resize. Khi mảng đầy, nó phải copy sang mảng mới gấp đôi kích thước ($O(n)$). Nhưng việc này chỉ xảy ra sau $n$ lần chèn $O(1)$. Khấu hao lại vẫn là $O(1)$.

---

## 4. Checklist phân tích Big O nhanh
1.  **Vòng lặp đơn:** $O(n)$.
2.  **Vòng lặp lồng nhau:** $O(n \times m)$ hoặc $O(n^2)$.
3.  **Chia đôi dữ liệu mỗi bước:** $O(\log n)$.
4.  **Đệ quy:** $O(\text{chi nhánh}^\text{độ sâu})$.
    *   *Fibonacci đệ quy thuần:* $O(2^n)$ - Cực kỳ tệ!
5.  **Dùng Hash Map/Set:** Thường là $O(1)$.

---

## 🧠 Mental Model: Giới hạn 1 giây
Trong hầu hết các cuộc thi lập trình và hệ thống thực tế, bạn có khoảng **$10^8$ phép tính mỗi giây**.
*   $n = 100 \rightarrow O(n^4)$ có thể chạy được.
*   $n = 10^5 \rightarrow Chỉ $O(n \log n)$ hoặc $O(n)$ mới sống sót.
*   $n = 10^9 \rightarrow Chỉ $O(\log n)$ hoặc $O(1)$ mới khả thi.

---

## 🚀 Bước tiếp theo
Hãy áp dụng tư duy này vào **[Arrays & Strings](./arrays-strings.md)** để thấy cách các pattern tối ưu hóa Big O.
