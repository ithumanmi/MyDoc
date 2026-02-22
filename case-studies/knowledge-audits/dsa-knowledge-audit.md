# 🧮 Data Structures & Algorithms Knowledge Audit: Thử thách "Algorithm Master"

> **Mục đích:** Đo lường năng lực tư duy logic, khả năng chọn lựa cấu trúc dữ liệu phù hợp và tối ưu hóa hiệu năng thuật toán.
> **Phiếu trả lời:** [Tải mẫu tại đây](../templates/dsa-answer-template.md)
> 
> **Kịch bản:** Bạn là **Optimization Engineer** cho "DataFlow" - một công cụ xử lý dữ liệu lớn thời gian thực. Hệ thống đang gặp nút thắt cổ chai về hiệu năng khi phải xử lý hàng tỷ bản ghi mỗi ngày. Bạn cần tái cấu trúc code để giảm chi phí vận hành server.

---

## 🛠️ Thử thách 1: Complexity & Basic Structures (Độ phức tạp)
*Đo lường năng lực phân tích hiệu năng và xử lý mảng/chuỗi.*

**Tình huống:** Bạn có một mảng các số nguyên đại diện cho giá cổ phiếu. Bạn cần tìm lợi nhuận lớn nhất có thể đạt được bằng cách mua 1 lần và bán 1 lần. Code hiện tại đang dùng 2 vòng lặp lồng nhau ($O(n^2)$).

**Câu hỏi:**
1.  Hãy mô tả thuật toán để giải bài toán này với độ phức tạp **$O(n)$** về thời gian và **$O(1)$** về không gian.
2.  Khi nào bạn sẽ chọn **Linked List** thay vì **Array**? Giải thích sự khác biệt về chi phí bộ nhớ và thời gian truy cập ngẫu nhiên.

**Thước đo:**
*   **🟢 Beginner:** Biết dùng vòng lặp, hiểu sơ về Big O.
*   **🔴 Expert:** Luôn nghĩ đến tối ưu Space/Time, thành thạo các pattern như **Two Pointers** hay **Sliding Window**.

---

## 🌳 Thử thách 2: Non-linear Data Structures (Cây & Đồ thị)
*Đo lường năng lực xử lý quan hệ phức tạp và phân cấp.*

**Tình huống:** DataFlow cần tính năng "Gợi ý kết nối" giữa các người dùng trong một mạng xã hội (tương tự 2nd-degree connections).

**Câu hỏi:**
1.  Bạn sẽ chọn cấu trúc dữ liệu nào để biểu diễn mạng lưới này? Tại sao?
2.  Để tìm đường đi ngắn nhất giữa hai người dùng, bạn chọn **Breadth-First Search (BFS)** hay **Depth-First Search (DFS)**? Tại sao?

**Thước đo:**
*   **🟢 Beginner:** Biết duyệt cây nhị phân đơn giản.
*   **🔴 Expert:** Thành thạo các thuật toán đồ thị nâng cao (**Dijkstra**, **A***, **DSU**) và hiểu cách áp dụng chúng vào bài toán thực tế.

---

## 📈 Thử thách 3: Sorting & Searching (Sắp xếp & Tìm kiếm)
*Đo lường năng lực quản lý dữ liệu lớn.*

**Tình huống:** Bạn cần tìm kiếm sự tồn tại của một phần tử trong một danh sách đã được sắp xếp có 1 tỷ phần tử.

**Câu hỏi:**
1.  Giải thuật **Binary Search** hoạt động dựa trên nguyên lý nào? Số lần so sánh tối đa là bao nhiêu trong trường hợp này?
2.  Sự khác biệt lớn nhất giữa **Quick Sort** và **Merge Sort** là gì? Trong trường hợp tài nguyên RAM cực kỳ hạn chế, bạn sẽ ưu tiên cái nào?

**Thước đo:**
*   **🟢 Beginner:** Biết dùng hàm `sort()` có sẵn của ngôn ngữ.
*   **🔴 Expert:** Hiểu bản chất các thuật toán sắp xếp, biết cách tùy chỉnh để xử lý dữ liệu ngoại cỡ (External Sorting).

---

## 🧠 Thử thách 4: Advanced Patterns (DP & Greedy)
*Đo lường tư duy tối ưu hóa cấp cao.*

**Tình huống:** Bạn cần thiết lập một hệ thống đổi tiền thối cho khách hàng sao cho số lượng tờ tiền là ít nhất (biết rằng có các mệnh giá 1, 2, 5).

**Câu hỏi:**
1.  Tại sao giải thuật **Greedy** hoạt động tốt trong trường hợp này nhưng lại thất bại nếu mệnh giá tiền là 1, 3, 4 (và bạn cần thối 6 đồng)?
2.  Hãy mô tả hướng giải quyết bài toán mệnh giá 1, 3, 4 bằng **Dynamic Programming**. Công thức truy hồi là gì?

**Thước đo:**
*   **🟢 Beginner:** Thử sai (Brute-force) hoặc chỉ dùng được Greedy đơn giản.
*   **🔴 Expert:** Nhận diện được bài toán DP, thiết kế được bảng phương án (Tabulation) và tối ưu hóa không gian lưu trữ.

---

## 📊 Bảng tự chấm điểm (Scoring Rubric)

| Lĩnh vực | Thang điểm (1-10) | Gợi ý tự vấn |
| :--- | :---: | :--- |
| **Basic Mastery** | ____ / 10 | Bạn có thể Center a Div (à nhầm, giải bài LeetCode Easy) trong 5 phút không? |
| **Non-linear Logic** | ____ / 10 | Bạn có sợ khi nhìn thấy Đồ thị (Graph) và Đệ quy không? |
| **Search/Sort Deep Dive** | ____ / 10 | Bạn có hiểu tại sao $O(n \log n)$ lại là "tốc độ ánh sáng" của Sorting không? |
| **Advanced Patterns** | ____ / 10 | Bạn có thể bóc tách một bài toán DP phức tạp thành các bài toán con không? |
| **Space/Time Balance** | ____ / 10 | Bạn có biết hy sinh RAM để đổi lấy Tốc độ (hoặc ngược lại) không? |

### 🏆 Xếp hạng năng lực DSA:
*   **0 - 15 điểm:** **Logical Beginner**. Hãy bắt đầu với lộ trình tại `domains/dsa/`.
*   **16 - 30 điểm:** **Problem Solver**. Có khả năng code tốt, hiểu cấu trúc dữ liệu, đủ sức pass phỏng vấn Junior/Mid.
*   **31 - 45 điểm:** **Algorithm Specialist**. Bạn là người tối ưu hóa thầm lặng đằng sau các hệ thống lớn.
*   **46 - 50 điểm:** **Optimization Architect**. Bạn có tư duy toán học và logic cực kỳ sắc bén, đủ sức làm việc tại các lab nghiên cứu hoặc FAANG.

---

## 🔑 Answer Key: Góc nhìn Chuyên gia (Expert Guidelines)

### Thử thách 1: Complexity
*   **Lợi nhuận cổ phiếu:** Dùng 1 biến `min_price` để lưu giá thấp nhất đã qua và 1 biến `max_profit` để cập nhật lợi nhuận tức thì. Chỉ cần duyệt mảng 1 lần.
*   **Linked List:** Chọn khi cần chèn/xóa ở đầu/giữa thường xuyên ($O(1)$ nếu đã có node) và không biết trước kích thước dữ liệu.

### Thử thách 2: Trees & Graphs
*   **Biểu diễn:** Dùng **Adjacency List** (Danh sách kề) để tiết kiệm bộ nhớ cho đồ thị thưa.
*   **Đường đi ngắn nhất:** Dùng **BFS** cho đồ thị không trọng số (mỗi kết nối coi là 1 bước).

### Thử thách 3: Sorting & Searching
*   **Binary Search:** Dựa trên Chia để trị (Divide and Conquer). Với 1 tỷ phần tử ($\approx 2^{30}$), chỉ tốn tối đa 30 lần so sánh.
*   **RAM hạn chế:** Dùng **Quick Sort** ($O(1)$ extra space cho in-place) mặc dù Merge Sort ổn định hơn nhưng tốn $O(n)$ không gian.

### Thử thách 4: Advanced Patterns
*   **Greedy thất bại:** Với mệnh giá 1, 3, 4 và cần thối 6: Greedy lấy 4+1+1 (3 tờ), nhưng DP sẽ tìm ra 3+3 (2 tờ).
*   **DP Formula:** $DP[i] = 1 + \min(DP[i - c])$ với $c$ là từng mệnh giá tiền.

---

## 🚀 Tài liệu bổ trợ để "Level Up"
*   **Lộ trình toàn diện:** [DSA Roadmap](../../domains/dsa/README.md)
*   **Luyện tập:** [LeetCode Top 100 Liked Questions](https://leetcode.com/problemset/top-100-liked-questions/)
*   **Visualizer:** [VisuAlgo.net](https://visualgo.net/) (Xem thuật toán chạy trực quan)
