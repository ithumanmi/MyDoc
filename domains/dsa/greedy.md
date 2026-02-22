# 🤑 Greedy Algorithms: The Best Choice Right Now

> [← Back to DSA Roadmap](./README.md)

Thuật toán Tham lam (Greedy) là chiến lược giải quyết vấn đề bằng cách **luôn đưa ra lựa chọn tốt nhất tại thời điểm hiện tại** với hy vọng rằng lựa chọn cục bộ đó sẽ dẫn đến kết quả tối ưu toàn cục.

---

## 1. Bản chất của Greedy
Không giống như Lập trình động (DP) cần tính toán mọi trường hợp con, Greedy chỉ quan tâm đến bước đi tiếp theo.

### 🧩 Hai tính chất để bài toán dùng được Greedy:
1.  **Greedy Choice Property (Tính chất lựa chọn tham lam):** Lựa chọn cục bộ tối ưu dẫn đến lựa chọn toàn cục tối ưu.
2.  **Optimal Substructure (Cấu trúc con tối ưu):** Bài toán gốc có thể được giải bằng cách giải các bài toán con.

---

## 🛠️ Các bài toán kinh điển (Patterns)

### 1. Interval Scheduling (Lập lịch khoảng)
Chọn số lượng công việc tối đa không trùng lặp thời gian.
*   **Chiến lược tham lam:** Luôn chọn công việc **kết thúc sớm nhất**. (Đúng!)
*   *Lưu ý:* Chọn công việc bắt đầu sớm nhất hay ngắn nhất đều sai.

### 2. Fractional Knapsack (Cái túi phân đoạn)
Bạn có thể chia nhỏ vật phẩm (như vàng, bạc).
*   **Chiến lược tham lam:** Luôn chọn vật phẩm có **giá trị/trọng lượng** lớn nhất.

### 3. Huffman Coding (Mã hóa Huffman)
Nén dữ liệu bằng cách gán mã ngắn cho ký tự xuất hiện nhiều nhất.

### 4. Prim / Kruskal (Cây khung nhỏ nhất)
Chọn các cạnh ngắn nhất để kết nối các đỉnh mà không tạo chu trình.

---

## 💡 Cạm bẫy của Greedy
Đừng để tên gọi lừa bạn. Không phải lúc nào tham lam cũng tốt.
*   *Ví dụ:* Bài toán đổi tiền. Với các mệnh giá (25, 10, 1), Greedy (lấy tờ lớn nhất) hoạt động tốt. Nhưng với mệnh giá (25, 20, 10, 1), để đổi 40 xu, Greedy sẽ cho (25, 10, 1, 1, 1, 1, 1) - 7 tờ, trong khi đáp án đúng là (20, 20) - 2 tờ.
*   **Lời khuyên:** Khi Greedy thất bại, hãy nghĩ đến **Lập trình động (DP)**.

---

## 🧠 Mental Model: Sắp xếp trước, Tham lam sau
90% bài toán Greedy đều bắt đầu bằng việc **Sắp xếp (Sorting)** dữ liệu theo một tiêu chí nào đó (thời gian kết thúc, giá trị/trọng lượng, độ ưu tiên).

---

## 🚀 Thực hành (LeetCode Tags)
1.  **Basic:** *Assign Cookies, Lemmonade Change.*
2.  **Intermediate:** *Gas Station, Queue Reconstruction by Height, Partition Labels.*
3.  **Advanced:** *Candy, Course Schedule III.*

---

## 🔗 Tiếp theo
Học cách thử mọi trường hợp một cách thông minh với **[Backtracking](./backtracking.md)**.
