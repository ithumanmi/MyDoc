# 🧩 Merge Sort: The Power of Perfect Combination

> [← Back to Sorting & Searching](./sorting-searching.md) | [← Back to Recursion](./recursion.md)
> 
> *"Lặp là cách ta đi qua thế giới. Đệ quy là cách ta định nghĩa thế giới."*

Nếu QuickSort tập trung vào việc **Phân chia (Divide)** dựa trên một điểm chốt, thì **Merge Sort** lại dồn toàn bộ trí tuệ vào bước **Hợp nhất (Combine)**. 

---

## 1. Định nghĩa "Sự sắp xếp" theo Merge Sort

Merge Sort định nghĩa một mảng đã được sắp xếp là:
1.  Chia mảng làm **hai nửa bằng nhau** (bất kể giá trị bên trong).
2.  Sắp xếp đệ quy hai nửa đó.
3.  **Hợp nhất (Merge)** hai nửa đã sắp xếp thành một mảng thống nhất.

### 💡 Lời giải Đệ quy (Vẻ đẹp của sự Kỷ luật):
```python
def mergesort(arr):
    if len(arr) <= 1:
        return arr # Base case: Thế giới đơn lẻ
    
    mid = len(arr) // 2
    left = mergesort(arr[:mid])  # Đệ quy nửa trái
    right = mergesort(arr[mid:]) # Đệ quy nửa phải
    
    # Định nghĩa: Sorted = Merge(Sorted_Left, Sorted_Right)
    return merge(left, right)

def merge(left, right):
    # Kỹ thuật hợp nhất hai mảng đã sắp xếp trong O(n)
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

---

## 2. Tại sao Merge Sort lại "Ổn định"?

1.  **Hiệu năng bất biến ($O(n \log n)$):** Không giống QuickSort có thể rơi vào $O(n^2)$, Merge Sort luôn chia đôi mảng một cách "công bằng". Nó là thuật toán đáng tin cậy nhất trong các hệ thống quan trọng.
2.  **Tính ổn định (Stability):** Nó giữ nguyên thứ tự tương đối của các phần tử bằng nhau. 
    *   *Ví dụ:* Nếu bạn sắp xếp danh sách sinh viên theo Tên, rồi sau đó sắp xếp theo Lớp, Merge Sort đảm bảo trong cùng một lớp, tên sinh viên vẫn được sắp xếp theo bảng chữ cái.

---

## 🧠 Mental Model: Hợp nhất từ những mảnh vụn

Merge Sort dạy chúng ta rằng: **"Mọi thứ phức tạp đều có thể được giải quyết nếu ta chia nhỏ nó đến mức tối giản, rồi học cách kết hợp chúng lại một cách khoa học."**

*   **QuickSort:** "Làm việc khó ngay từ đầu (Partition), phần sau sẽ dễ."
*   **Merge Sort:** "Làm việc dễ trước (Divide), dành toàn lực để giải quyết việc khó cuối cùng (Merge)."

---

## 🏗️ Ứng dụng thực tế: External Sorting

Merge Sort là thuật toán duy nhất có thể sắp xếp dữ liệu **lớn hơn cả bộ nhớ RAM** (ví dụ sắp xếp 100GB dữ liệu trên máy tính có 8GB RAM).
*   **Cách làm:** Chia nhỏ 100GB thành các mảnh 1GB, sắp xếp từng mảnh bằng RAM, sau đó dùng đệ quy Merge để hợp nhất các mảnh đó trực tiếp trên ổ cứng. Đây là nền tảng của các hệ quản trị cơ sở dữ liệu (SQL, NoSQL).

---

## 🚀 Thực hành (LeetCode)
*   **Merge Sorted Array:** Bài tập cơ bản về bước `merge`.
*   **Sort List:** Sắp xếp Linked List bằng Merge Sort. (Đây là lựa chọn tối ưu nhất cho Linked List vì nó không cần truy cập ngẫu nhiên như QuickSort).

---

## 🔗 Tiếp theo
Học cách nâng tầm đệ quy bằng việc "không bao giờ tính lại" tại **[Dynamic Programming](./dynamic-programming.md)**.
