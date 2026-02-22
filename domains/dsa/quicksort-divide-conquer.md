# ⚡ QuickSort: The Mastery of Divide and Conquer

> [← Back to Sorting & Searching](./sorting-searching.md) | [← Back to Recursion](./recursion.md)
> 
> *"Lặp là cách ta đi qua thế giới. Đệ quy là cách ta định nghĩa thế giới."*

Nếu **Selection Sort** là cách tiếp cận **Lặp (Iteration)** điển hình (tìm số nhỏ nhất, đưa lên đầu, lặp lại cho đến hết), thì **QuickSort** là cách tiếp cận **Đệ quy (Recursion)** đỉnh cao: Nó không "sắp xếp", nó **"định nghĩa lại trật tự"**.

---

## 1. Định nghĩa "Sự sắp xếp" theo QuickSort

QuickSort định nghĩa một mảng đã được sắp xếp là:
1.  Chọn một phần tử làm **Chốt (Pivot)**.
2.  Đưa các phần tử nhỏ hơn Pivot sang bên trái, các phần tử lớn hơn sang bên phải.
3.  Khi đó, Pivot đã nằm đúng vị trí vĩnh viễn của nó.
4.  Lặp lại định nghĩa này cho hai nửa bên trái và bên phải (Đệ quy).

### 💡 Lời giải Đệ quy (Vẻ đẹp của Logic):
```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr # Base case: Thế giới chỉ có 1 phần tử đã tự sắp xếp
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Định nghĩa: Sorted = Quick(Left) + Middle + Quick(Right)
    return quicksort(left) + middle + quicksort(right)
```
*Lưu ý: Đây là phiên bản Pythonic để minh họa ý tưởng. Trong thực tế, ta dùng kỹ thuật In-place để tối ưu bộ nhớ.*

---

## 2. Tại sao QuickSort lại "Nhanh"? (Lý thuyết Thông tin)

QuickSort trung bình tốn **$O(n \log n)$**. Tại sao?
*   **Lặp ($O(n^2)$):** Bạn so sánh mọi thứ với mọi thứ. Bạn đang làm việc một cách mù quáng.
*   **Đệ quy ($O(n \log n)$):** Mỗi bước phân chia (Partition), bạn loại bỏ một nửa số lượng so sánh không cần thiết. Bạn đang "nén" bài toán lại.

**Quy luật:** Khi bạn chia đôi vấn đề, bạn đang giải quyết nó theo cấp số nhân (Exponential speedup).

---

## 🧠 Mental Model: Phân chia và Cai trị (Divide and Conquer)

QuickSort không chỉ là một thuật toán, nó là một chiến lược sống:
1.  **Phân chia (Divide):** Đừng nhìn cả một dự án khổng lồ. Hãy tìm một "Pivot" (điểm mấu chốt) và chia dự án thành hai phần: việc làm ngay và việc làm sau.
2.  **Cai trị (Conquer):** Giải quyết từng phần nhỏ bằng cùng một phương pháp (Đệ quy).
3.  **Kết hợp (Combine):** Khi các phần nhỏ đã xong, cả dự án tự động hoàn thành mà không cần một bước "tổng hợp" phức tạp.

---

## 💡 Bí mật của Pivot (Điểm Chốt)

Trong QuickSort, sự lựa chọn Pivot quyết định vận mệnh của thuật toán:
*   **Pivot tốt (Trung vị):** Bài toán chia đôi hoàn hảo ($O(n \log n)$).
*   **Pivot tệ (Nhỏ nhất/Lớn nhất):** Bài toán không được chia nhỏ, đệ quy trở thành lặp ($O(n^2)$).

**Bài học thực tế:** Trong bất kỳ hệ thống phức tạp nào, việc tìm ra "điểm mấu chốt" (Pivot) chính xác là yếu tố then chốt giữa thành công rực rỡ và thất bại thảm hại.

---

## 🚀 Thực hành (LeetCode)
*   **K-th Largest Element in an Array:** Thử giải bài này bằng tư duy **QuickSelect** (Một biến thể của QuickSort chỉ đệ quy vào một nửa mảng). Bạn sẽ thấy sức mạnh của việc "vứt bỏ" 50% dữ liệu ở mỗi bước!

---

## 🔗 Tiếp theo
Học cách kết hợp đệ quy với bộ nhớ để đạt hiệu năng tối thượng tại **[Dynamic Programming](./dynamic-programming.md)**.
