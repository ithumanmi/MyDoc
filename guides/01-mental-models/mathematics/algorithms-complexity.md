# 💻 Algorithms & Complexity (Toán học của Hiệu suất)

## 1. Độ phức tạp (Big O Notation) - Giới hạn trên
Big O mô tả hành vi của thuật toán khi dữ liệu đầu vào ($n$) tiến tới vô cùng. Nó là **giới hạn trên** (Upper Bound) của thời gian thực thi hoặc bộ nhớ cần dùng.

### Các cấp độ phổ biến:
1.  **$O(1)$ - Constant Time (Hằng số):** Thời gian không đổi bất kể $n$.
    *   *Ví dụ:* Truy cập phần tử mảng bằng index `arr[5]`.
    *   *Đời sống:* Thói quen. Đánh răng tốn năng lượng não như nhau dù bạn đánh 1 ngày hay 10 năm.
2.  **$O(\log n)$ - Logarithmic Time (Logarit):** Thời gian tăng cực chậm khi $n$ tăng gấp đôi.
    *   *Ví dụ:* Tìm kiếm nhị phân (Binary Search). Tìm từ trong từ điển.
    *   *Đời sống:* Phân loại hồ sơ khoa học.
3.  **$O(n)$ - Linear Time (Tuyến tính):** Thời gian tăng tỷ lệ thuận với $n$.
    *   *Ví dụ:* Đọc sách từng trang. Quét nhà.
4.  **$O(n \log n)$ - Linearithmic:** Hiệu suất của các thuật toán sắp xếp tốt nhất (Merge Sort, Quick Sort).
5.  **$O(n^2)$ - Quadratic (Bình phương):**
    *   *Ví dụ:* Nested loops (Vòng lặp lồng nhau). Mọi người trong phòng bắt tay nhau từng đôi một.
    *   *Đời sống:* Họp hành không hiệu quả. Thêm 1 người, số kết nối giao tiếp tăng theo bình phương.
6.  **$O(2^n)$ - Exponential (Mũ):**
    *   *Ví dụ:* Bài toán Tháp Hà Nội, Phá mật khẩu Brute-force.
    *   *Ý nghĩa:* Tăng trưởng bùng nổ (Viral) hoặc độ khó không thể giải quyết.

## 2. P vs NP (Bài toán Thiên niên kỷ)
*   **P (Polynomial):** Các bài toán có thể **giải** nhanh chóng (trong thời gian đa thức). (Ví dụ: Phép nhân, Sắp xếp).
*   **NP (Nondeterministic Polynomial):** Các bài toán có thể **kiểm tra** đáp án nhanh chóng, nhưng chưa biết cách giải nhanh. (Ví dụ: Sudoku, Xếp lịch học, Bài toán người du lịch - TSP).
*   **Câu hỏi:** Liệu $P = NP$? (Liệu mọi bài toán kiểm tra dễ đều có thể giải dễ?). Đa số tin là Không.
*   **Ứng dụng:** Mật mã học (Cryptography) dựa trên giả định $P \neq NP$. Nếu ai đó chứng minh $P=NP$, toàn bộ hệ thống bảo mật ngân hàng, blockchain sẽ sụp đổ vì việc phá mã trở nên dễ dàng.

## 3. Divide and Conquer (Chia để trị)
Chiến lược đệ quy:
$$T(n) = aT(n/b) + f(n)$$
1.  Chia bài toán lớn thành $a$ bài toán con kích thước $n/b$.
2.  Giải quyết từng bài toán con.
3.  Gộp kết quả ($f(n)$ là chi phí gộp).
*   **Ứng dụng:** Đừng cố "Xây dựng sự nghiệp". Hãy chia nhỏ thành: Học kỹ năng A -> Làm dự án B -> Xin việc C.

## 4. Greedy Algorithms (Thuật toán Tham lam)
Luôn chọn phương án tốt nhất *tại thời điểm hiện tại* (Local Optimum) với hy vọng dẫn đến kết quả tốt nhất toàn cục (Global Optimum).
*   **Ưu điểm:** Nhanh, dễ quyết định.
*   **Nhược điểm:** Thường không đạt Global Optimum.
*   **Ví dụ:** Bạn chọn công việc lương cao nhất ngay khi ra trường (Greedy), nhưng bỏ qua công việc lương thấp hơn nhưng có mentor giỏi (Global Optimum về dài hạn).
*   **Hill Climbing:** Một dạng tham lam. Bạn leo lên chỗ cao nhất bạn thấy. Nhưng bạn có thể đang đứng trên một ngọn đồi nhỏ chứ không phải đỉnh Everest. Để tìm Everest, đôi khi bạn phải chấp nhận đi xuống thung lũng (Simulated Annealing).

## 5. Explore vs. Exploit (Khám phá vs. Khai thác)
Bài toán Multi-armed Bandit: Bạn có nên tiếp tục chơi cái máy slot machine đang cho tiền (Exploit) hay thử máy khác có thể cho nhiều hơn (Explore)?
*   **Regret Minimization:** Mục tiêu là giảm thiểu sự hối tiếc.
*   **Quy tắc Gittins Index:** Cung cấp giải pháp toán học tối ưu.
*   **Chiến lược Đời sống:**
    *   Giai đoạn đầu (Trẻ): Explore tối đa (Thử sai). Giá trị thông tin > Giá trị lợi nhuận tức thời.
    *   Giai đoạn sau (Già): Exploit tối đa (Tận dụng kinh nghiệm).
    *   **Tỷ lệ vàng:** Dành 10-20% tài nguyên để thử nghiệm ngẫu nhiên, 80% để tối ưu cái đang hiệu quả.

---

## 🛠️ Ứng dụng Thực chiến (Life Applications)

### 1. Batch Processing (Xử lý theo lô) - Giảm O(n)
Mỗi lần chuyển đổi tác vụ (Context Switching), não mất 20 phút để tập trung lại.
*   **Sai:** Check email 5 phút/lần (O(n) lần chuyển đổi).
*   **Đúng:** Check email 2 lần/ngày (Batching - O(1)).
*   **Đời sống:** Giặt đồ 1 lần/tuần thay vì mỗi ngày. Đi chợ 1 lần/tuần. Gom các việc lặt vặt (trả bill, gọi điện) làm một lèo trong 1 tiếng.

### 2. Caching (Bộ nhớ đệm) - Tăng tốc O(1)
Lấy đồ từ ngăn kéo (Disk) lâu hơn lấy đồ trên mặt bàn (RAM).
*   **Mise-en-place:** Đầu bếp chuyên nghiệp luôn bày sẵn nguyên liệu (Cache) trước khi nấu.
*   **Deep Work:** Trước khi ngồi làm việc, hãy chuẩn bị sẵn nước, tài liệu, tắt thông báo. Đừng để việc "đi lấy nước" làm gián đoạn dòng chảy (Cache miss).

### 3. Premature Optimization (Tối ưu hóa sớm)
"Tối ưu hóa sớm là nguồn gốc của mọi tội lỗi" (Donald Knuth).
*   **Code:** Tốn 10 tiếng để tối ưu một hàm chỉ chạy 1 lần/tháng là vô nghĩa.
*   **Khởi nghiệp:** Tốn 1 tháng thiết kế Logo, in danh thiếp khi chưa có khách hàng nào là vô nghĩa. Hãy làm bản nháp (MVP) trước, tối ưu sau.
