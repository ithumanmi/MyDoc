# 🧵 Arrays & Strings: The Building Blocks

> [← Back to DSA Roadmap](./README.md)

Mảng và Chuỗi là những cấu trúc dữ liệu cơ bản nhất nhưng lại chứa đựng những kỹ thuật tối ưu hóa kinh điển. Bí quyết ở đây không phải là dùng hàm có sẵn, mà là hiểu các **Design Patterns** để tránh vòng lặp lồng nhau.

---

## 1. Mảng (Arrays) - Quyền năng của bộ nhớ liên tục
Mảng mạnh nhất ở việc **truy cập ngẫu nhiên (Random Access)** nhờ lưu trữ liên tiếp trong RAM.

### 🛠️ Kỹ thuật tối ưu kinh điển:
1.  **Two Pointers (Hai con trỏ):** Dùng để thu hẹp không gian tìm kiếm.
    *   *Tình huống:* Tìm cặp số có tổng bằng $S$ trong mảng đã sắp xếp. Thay vì $O(n^2)$, Two Pointers giảm xuống **$O(n)$**.
2.  **Sliding Window (Cửa sổ trượt):** Dùng để xử lý các mảng con liên tiếp.
    *   *Tình huống:* Tìm mảng con dài nhất có tổng nhỏ hơn $K$. Kỹ thuật này giúp ta không phải tính lại tổng từ đầu ở mỗi bước.
3.  **Prefix Sum (Tổng tiền tố):** Tiền xử lý dữ liệu để trả lời các câu hỏi về khoảng (range queries) trong $O(1)$.
    *   *Tình huống:* Tính tổng các số từ vị trí $i$ đến $j$.

---

## 2. Chuỗi (Strings) - Những mảng ký tự đặc biệt
Chuỗi thực chất là mảng ký tự, nhưng cần lưu ý tính **Immutable** (không thể thay đổi) trong một số ngôn ngữ như Java hay Python.

### 🛠️ Kỹ thuật tối ưu:
1.  **String Builder:** Tránh tạo ra hàng ngàn object tạm thời khi nối chuỗi trong vòng lặp.
2.  **Hash Map / Frequency Array:** Đếm số lần xuất hiện của ký tự.
    *   *Tip:* Nếu chuỗi chỉ chứa ký tự lowercase, hãy dùng mảng `int[26]` thay vì Hash Map để tối ưu tốc độ và bộ nhớ.
3.  **Anagrams & Palindromes:** Hai bài toán kinh điển để luyện tập tư duy đối xứng và tần suất.

---

## 💡 Deep Dive: Sliding Window Pattern
Đây là kỹ thuật giúp bạn chuyển từ $O(n^2)$ xuống $O(n)$ cực kỳ hiệu quả.

**Mẫu code tư duy:**
```python
left = 0
for right in range(len(arr)):
    # 1. Thêm arr[right] vào cửa sổ hiện tại
    # 2. Trong khi điều kiện cửa sổ không thỏa mãn:
    #    - Loại bỏ arr[left] và tăng left
    # 3. Cập nhật kết quả (max length, min length, etc.)
```

---

## 🧠 Mental Model: In-place vs Extra Space
*   **In-place:** Sửa trực tiếp trên mảng đầu vào ($O(1)$ extra space). Đây là yêu cầu thường gặp để kiểm tra khả năng quản lý con trỏ.
*   **Extra Space:** Tạo mảng mới hoặc Hash Map ($O(n)$ space). Dễ code hơn nhưng tốn tài nguyên hơn.

---

## 🚀 Thực hành (LeetCode Tags)
1.  **Two Pointers:** *Two Sum II, Reverse String, Remove Duplicates.*
2.  **Sliding Window:** *Longest Substring Without Repeating Characters, Minimum Size Subarray Sum.*
3.  **Prefix Sum:** *Range Sum Query, Subarray Sum Equals K.*

---

## 🔗 Tiếp theo
Học cách quản lý các phần tử không nằm cạnh nhau trong bộ nhớ tại **[Linked Lists](./linked-lists.md)**.
