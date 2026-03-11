# 📖 20 Khái Niệm System Design "Must-Know" 🚀

---
title: "System Design Glossary"
description: "20 thuật ngữ nền tảng giúp developer tự tin bước vào phỏng vấn system design."
tags:
  - backend
  - system-design
  - glossary
updated: 2026-03-11
---

> [← Back to Backend Roadmap](../README.md)

Đây là tấm vé thông hành cho Developer muốn lên Senior.
20 khái niệm này giúp bạn không bị "ngợp" khi thiết kế hệ thống lớn và tự tin khi phỏng vấn Big Tech.

---

## 🎯 1. Performance & Tốc Độ

### 1.1. ⚖️ Load Balancing
*   **Là gì:** Phân phối traffic đều giữa các server để tránh quá tải một máy đơn lẻ.
*   **Ví dụ:** Như ông tổng đài chia cuộc gọi cho các nhân viên trực điện thoại.
*   **Tại sao cần:** Tăng độ tin cậy (Reliability) và khả năng mở rộng (Scalability).

### 1.2. ⚡ Caching
*   **Là gì:** Lưu dữ liệu hay dùng vào bộ nhớ nhanh (RAM) thay vì truy xuất từ ổ cứng (Disk) hay tính toán lại.
*   **Ví dụ:** Như tờ giấy nhớ dán trên bàn làm việc thay vì mỗi lần cần phải mở tủ hồ sơ tìm kiếm.
*   **Tại sao cần:** Giảm độ trễ (Latency), tăng tốc độ phản hồi.

### 1.3. 📇 DB Indexing
*   **Là gì:** Cấu trúc dữ liệu giúp tìm kiếm bản ghi trong Database cực nhanh.
*   **Ví dụ:** Như mục lục ở cuối cuốn sách giúp bạn tìm trang cần đọc ngay lập tức thay vì lật từng trang.
*   **Tại sao cần:** Tăng tốc độ truy vấn (Query Performance).

### 1.4. 🌍 CDN (Content Delivery Network)
*   **Là gì:** Hệ thống máy chủ phân tán toàn cầu, lưu trữ bản sao nội dung tĩnh (ảnh, video) gần người dùng nhất.
*   **Ví dụ:** Như kho hàng Tiki/Shopee đặt ngay tại Hà Nội để giao cho khách Hà Nội nhanh hơn là giao từ kho Sài Gòn.
*   **Tại sao cần:** Giảm tải cho server gốc, tăng tốc độ tải trang cho user ở xa.

---

## 🗄️ 2. Database & Data

### 2.1. 🧩 Database Sharding
*   **Là gì:** Chia một database khổng lồ thành nhiều mảnh nhỏ (shard) lưu trên các máy khác nhau.
*   **Ví dụ:** Như 1 tủ hồ sơ quá đầy được chia thành nhiều tủ nhỏ A-M, N-Z.
*   **Tại sao cần:** Chịu được lượng dữ liệu và traffic viết (Write) khổng lồ mà 1 máy không tải nổi.

### 2.2. 📋 Replication
*   **Là gì:** Sao chép dữ liệu từ máy chính (Master) sang các máy phụ (Slave).
*   **Ví dụ:** Như photo tài liệu quan trọng cất ở nhiều nơi, nếu bản chính mất thì vẫn còn bản sao.
*   **Tại sao cần:** Đảm bảo an toàn dữ liệu (Backup) và tăng khả năng đọc (Read Scalability).

### 2.3. 🔪 Partitioning
*   **Là gì:** Chia bảng lớn thành nhiều phần nhỏ hơn để dễ quản lý.
*   **Ví dụ:** Như chia 1 cuốn tiểu thuyết dày 1000 trang thành 3 tập.
*   **Tại sao cần:** Truy vấn nhanh hơn khi chỉ cần quét trên 1 phân vùng nhỏ.

### 2.4. 🎭 CAP Theorem
*   **Là gì:** Định lý phát biểu rằng một hệ thống phân tán chỉ có thể đảm bảo tối đa 2 trong 3 thuộc tính: Consistency (Tính nhất quán), Availability (Tính sẵn sàng), Partition Tolerance (Khả năng chịu lỗi phân vùng).
*   **Ví dụ:** Tam giác bất khả thi - Bạn chỉ được chọn 2: Ngon, Bổ, Rẻ.

### 2.5. ⏳ Eventual Consistency
*   **Là gì:** Mô hình nhất quán yếu, chấp nhận dữ liệu không đồng bộ tức thì nhưng sẽ đồng bộ sau một khoảng thời gian.
*   **Ví dụ:** Khi bạn like ảnh trên Facebook, bạn bè có thể chưa thấy ngay lập tức, nhưng vài giây sau sẽ thấy.

### 2.6. 🔄 Consistent Hashing
*   **Là gì:** Kỹ thuật phân phối dữ liệu sao cho khi thêm/bớt server, số lượng dữ liệu phải di chuyển là ít nhất.
*   **Ví dụ:** Chia bánh cho 10 người, nếu có người thứ 11 đến thì chỉ cần lấy một ít phần của vài người, chứ không cần gom lại chia lại từ đầu.

---

## 📨 3. Communication & Messaging

### 3.1. 📬 Message Queues (MQ)
*   **Là gì:** Hàng đợi tin nhắn giúp các thành phần hệ thống giao tiếp bất đồng bộ (Asynchronous).
*   **Ví dụ:** Như đi mua trà sữa: Khách gọi món xong, lấy số thứ tự, ra ghế ngồi đợi. Nhân viên làm xong sẽ gọi số.
*   **Tại sao cần:** Decoupling (giảm phụ thuộc), xử lý traffic đột biến (Traffic Spike).

### 3.2. 🔌 WebSockets
*   **Là gì:** Giao thức kết nối 2 chiều liên tục giữa Client và Server.
*   **Ví dụ:** Như cuộc gọi điện thoại: Cả 2 bên đều có thể nói bất cứ lúc nào (khác với bộ đàm chỉ 1 người nói).
*   **Tại sao cần:** Ứng dụng Real-time (Chat, Game, Chứng khoán).

### 3.3. 🚪 API Gateway
*   **Là gì:** Cổng vào duy nhất cho tất cả các request từ Client, sau đó chuyển tiếp đến các service bên trong.
*   **Ví dụ:** Như lễ tân khách sạn: Tiếp nhận mọi yêu cầu của khách và chuyển cho bộ phận buồng phòng, nhà bếp, bảo vệ.
*   **Tại sao cần:** Bảo mật tập trung, Rate limiting, Routing.

### 3.4. 🛑 Rate Limiting
*   **Là gì:** Giới hạn số lượng request từ một user trong một khoảng thời gian.
*   **Ví dụ:** ATM quy định mỗi ngày chỉ được rút tối đa 20 triệu.
*   **Tại sao cần:** Chống DDoS, ngăn chặn spam, bảo vệ tài nguyên hệ thống.

---

## 🏗️ 4. Architecture & Scalability

### 4.1. 🧩 Microservices
*   **Là gì:** Kiến trúc chia ứng dụng thành nhiều service nhỏ, độc lập, mỗi service làm một việc cụ thể.
*   **Ví dụ:** Nhà hàng có nhiều bếp chuyên biệt: Bếp món Việt, Bếp món Âu, Quầy Bar.
*   **Tại sao cần:** Dễ phát triển, deploy độc lập, scale linh hoạt từng phần.

### 4.2. 🔍 Service Discovery
*   **Là gì:** Cơ chế giúp các service tự động tìm thấy nhau (IP/Port) trong môi trường thay đổi liên tục.
*   **Ví dụ:** Danh bạ điện thoại tự động cập nhật số mới của bạn bè.

### 4.3. 📈 Scalability (Horizontal vs Vertical)
*   **Vertical Scaling (Scale Up):** Nâng cấp phần cứng máy hiện tại (Thêm RAM, CPU).
    *   *Ví dụ:* Mua xe tải to hơn để chở nhiều hàng.
*   **Horizontal Scaling (Scale Out):** Thêm nhiều máy mới vào hệ thống.
    *   *Ví dụ:* Thuê thêm nhiều xe tải nhỏ chạy song song.

### 4.4. 🛡️ Fault Tolerance
*   **Là gì:** Khả năng hệ thống vẫn hoạt động (có thể giảm hiệu năng) khi có một hoặc nhiều thành phần bị lỗi.
*   **Ví dụ:** Máy bay có 4 động cơ, nếu hỏng 1 cái thì 3 cái còn lại vẫn giúp máy bay bay được.

### 4.5. 📊 Monitoring
*   **Là gì:** Theo dõi sức khỏe hệ thống qua các chỉ số (Metrics), Logs, và cảnh báo (Alerts).
*   **Ví dụ:** Bác sĩ đo nhiệt độ, huyết áp, nhịp tim cho bệnh nhân để biết tình trạng sức khỏe.

### 4.6. 🔐 AuthN vs AuthZ
*   **AuthN (Authentication):** Xác thực bạn là ai? (Đăng nhập).
    *   *Ví dụ:* Kiểm tra CMND/Passport.
*   **AuthZ (Authorization):** Xác định bạn được phép làm gì? (Phân quyền).
    *   *Ví dụ:* Kiểm tra vé máy bay để biết bạn được ngồi ghế hạng Thương gia hay Phổ thông.

---

## 🎯 Tóm Lại

Nắm vững 20 khái niệm này, bạn sẽ:
*   ✅ Tự tin "chém gió" khi phỏng vấn System Design.
*   ✅ Hiểu bản chất các hệ thống lớn (Facebook, Uber, Netflix).
*   ✅ Có tư duy của một Senior Architect.

## ✅ Apply it
- [ ] Chọn 5 thuật ngữ ít quen thuộc, viết lại định nghĩa + ví dụ thực tế của sản phẩm bạn đang làm.
- [ ] Tạo flashcard (Anki/Notion) cho toàn bộ 20 concepts và luyện trong 3 ngày liên tục.
- [ ] Mô tả 1 hệ thống bạn từng xây, highlight rõ những thuật ngữ nào đã áp dụng (caching, sharding, rate limit...).
- [ ] Dùng danh sách này làm checklist trước mỗi vòng phỏng vấn system design để không bỏ sót ý.
