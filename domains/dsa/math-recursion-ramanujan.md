# 🌌 Ramanujan Recursion: The Geometry of Numbers

> [← Back to Recursion](./recursion.md) | [← Back to DSA Roadmap](./README.md)

Khi nói đến Srinivasa Ramanujan, chúng ta không chỉ nói về toán học, mà là về **khả năng nhìn thấy cấu trúc trong sự hỗn loạn**. Đệ quy Ramanujan (đặc biệt là hàm phân hoạch) là một ví dụ kinh điển về việc tối ưu hóa đệ quy thông qua lý thuyết số.

---

## 1. Hàm phân hoạch $p(n)$ & Định lý Số ngũ giác (Pentagonal Number Theorem)

Bài toán: Có bao nhiêu cách phân tích số $n$ thành tổng các số nguyên dương?
*   *Ngây thơ (Naive):* Dùng đệ quy vét cạn sẽ tốn thời gian **Exponential $O(2^n)$**.
*   *Ramanujan - Euler:* Sử dụng các **Số ngũ giác mở rộng** (Generalized Pentagonal Numbers) để tạo ra công thức truy hồi.

### Công thức:
$$p(n) = \sum_{k \neq 0} (-1)^{k-1} p\left(n - \frac{k(3k-1)}{2}\right)$$

Các số hạng $\frac{k(3k-1)}{2}$ tăng rất nhanh ($1, 2, 5, 7, 12, 15...$), điều này có nghĩa là để tính $p(n)$, chúng ta chỉ cần gọi đệ quy khoảng **$O(\sqrt{n})$** lần.

### 💡 Giải thuật tối ưu (Dynamic Programming):
Thay vì đệ quy thuần túy, ta dùng DP để lưu lại các giá trị $p(i)$ đã tính:
```python
def partition_function(n):
    p = [0] * (n + 1)
    p[0] = 1
    for i in range(1, n + 1):
        k = 1
        while True:
            # Pentagonal number formulas: k(3k-1)/2 and k(3k+1)/2
            for pent in [k*(3*k - 1)//2, k*(3*k + 1)//2]:
                if pent <= i:
                    sign = 1 if k % 2 == 1 else -1
                    p[i] += sign * p[i - pent]
                else:
                    break
            else:
                k += 1
                continue
            break
    return p[n]
```
**Hiệu năng:** $O(n \sqrt{n})$ - Một bước nhảy vọt so với $O(2^n)$.

---

## 2. Ramanujan Tau Function $\tau(n)$

Hàm $\tau(n)$ được định nghĩa thông qua chuỗi lũy thừa (Modular Forms). Nó có tính chất **Nhân tính (Multiplicative)** cực kỳ quan trọng:
*   $\tau(mn) = \tau(m)\tau(n)$ nếu $gcd(m, n) = 1$.
*   $\tau(p^{k+1}) = \tau(p)\tau(p^k) - p^{11}\tau(p^{k-1})$ với $p$ là số nguyên tố.

Đây là một dạng **Đệ quy dựa trên tính chất số học**, giúp tính toán các giá trị cực lớn mà không cần duyệt qua toàn bộ không gian số.

---

## 🧠 Mental Model: Cấu trúc ẩn (Hidden Structures)

Ramanujan không nhìn các con số như những thực thể rời rạc. Ông nhìn chúng qua lăng kính của sự đối xứng và hình học.

1.  **Tính hệ thống:** Một giá trị không chỉ phụ thuộc vào giá trị "ngay trước nó" (như $n-1$), mà phụ thuộc vào những giá trị ở các "vị trí hình học đặc biệt" (như các số ngũ giác).
2.  **Sự nén thông tin:** Các công thức của ông là những bộ nén dữ liệu khổng lồ. Thay vì lưu trữ mọi trạng thái, ông tìm ra quy luật để tái tạo trạng thái.

---

## 🏗️ Ứng dụng hiện đại
*   **Mật mã học (Cryptography):** Các dạng modular và đường cong Elliptic (liên quan sâu đến các chuỗi Ramanujan) là nền tảng của bảo mật hiện đại.
*   **Vật lý lý thuyết:** Lý thuyết dây (String Theory) sử dụng các hằng số và hàm của Ramanujan để giải thích các chiều không gian.

---

## 🔗 Tài liệu chuyên sâu
*   *The Man Who Knew Infinity* (Robert Kanigel).
*   *Hardy-Ramanujan Theorem* về số lượng các ước nguyên tố.
