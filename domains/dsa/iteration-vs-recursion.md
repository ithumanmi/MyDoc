# 🔄 Iteration vs. Recursion: Two Perspectives, One Essence

> [← Back to Recursion](./recursion.md) | [← Back to DSA Roadmap](./README.md)

Trong khoa học máy tính, chúng ta thường tranh luận về hiệu năng giữa Lặp (Iteration) và Đệ quy (Recursion). Nhưng ở tầng sâu hơn, đây là hai cách tiếp cận khác nhau hoàn toàn về **nhận thức**.

---

## 1. Lặp (Iteration): Tư duy Tuyến tính & Thực thi
Lặp là quá trình đi từng bước một, theo trình tự thời gian và không gian bộ nhớ.

*   **Đặc điểm:** Tuyến tính (Linear), Cơ học, Thực dụng.
*   **Hành động:** `for i from 1 to n`.
*   **Ẩn dụ:** Cách con người đi bộ. Bạn không thể nhảy tới đích ngay lập tức, bạn phải nhấc chân trái, rồi chân phải, lặp lại cho đến khi tới nơi.
*   **Bản chất:** Đây là **cách ta thực thi** một quy trình trong thế giới vật lý.

---

## 2. Đệ quy (Recursion): Tư duy Cấu trúc & Định nghĩa
Đệ quy không quan tâm đến "từng bước". Nó quan tâm đến "bản chất của cấu trúc".

*   **Đặc điểm:** Toàn cục (Global), Tự tham chiếu (Self-referential), Hệ thống.
*   **Hành động:** `n! = n * (n-1)!`.
*   **Ẩn dụ:** Quy luật của vũ trụ hoặc cấu trúc của một bông hoa tuyết (Fractal). Một hạt mầm chứa đựng bản thiết kế của cả cái cây.
*   **Bản chất:** Đây là **cách ta định nghĩa** bản chất của một sự vật.

---

## 3. Cầu nối Kỹ thuật: Sự tương đương Church-Turing
Dù cảm giác khác nhau, nhưng về mặt toán học, chúng tương đương:
*   Mọi bài toán đệ quy đều có thể chuyển thành lặp (bằng cách dùng Stack).
*   Mọi vòng lặp đều có thể biểu diễn bằng đệ quy.

Điều này chứng minh rằng **Thực thi** và **Định nghĩa** chỉ là hai mặt của cùng một đồng xu tính toán.

---

## 🧠 Mental Model: Nhận thức luận về Đệ quy

Nhà ngôn ngữ học **Noam Chomsky** cho rằng khả năng đệ quy là đặc trưng cốt lõi của trí tuệ con người. Ngôn ngữ của chúng ta có cấu trúc đệ quy: *"Tôi biết rằng bạn nghĩ rằng anh ta đang nói dối"*.

Khi bạn tư duy bằng đệ quy, bạn đang đứng ở tầng cao của sự trừu tượng:
1.  **Nhìn thấy sự tương đồng:** Bài toán lớn thực chất là phiên bản thu nhỏ của chính nó.
2.  **Định nghĩa điểm dừng (Base Case):** Biết khi nào bản chất sự vật thay đổi (điểm chạm đất).

---

## 🎯 Kết luận tối thượng

> **"Lặp là cách ta đi qua thế giới. Đệ quy là cách ta định nghĩa thế giới."**

*   Dùng **Lặp** khi bạn cần sự tối ưu, thực dụng và kiểm soát từng bước (Performance-driven).
*   Dùng **Đệ quy** khi bạn cần hiểu thấu đáo cấu trúc, viết mã sạch và định nghĩa các hệ thống phức tạp (Understanding-driven).

---

## 🔗 Liên kết mở rộng
*   **[Lý thuyết Hệ thống (Systems Thinking)](../../guides/01-mental-models/systems-thinking.md):** Sự tự phản chiếu trong các hệ thống phức tạp.
*   **[Fractals & Nature]:** Cách tự nhiên dùng "đệ quy" để xây dựng thế giới vật chất.
