# 🌊 Cuộc Chiến Các Vị Thần Message Broker: Apache Kafka vs RabbitMQ

> [← Back to Distributed Architecture](./README.md)

Khi hệ thống từ Monolith chuyển sang Microservices, bài toán "Làm sao để 2 Services nói chuyện với nhau" là sống còn. HTTP/REST thì quá chậm, gRPC thì đồng bộ (chờ nhau). Message Brokers (Hệ thống xếp hàng tin nhắn) ra đời để giải quyết bài toán giao tiếp **Bất Đồng Bộ (Asynchronous)**.

Nhưng trong thế giới Broker, có 2 trường phái hoàn toàn đối lập, đại diện bởi 2 ông lớn: **RabbitMQ** và **Apache Kafka**.

---

## 🐇 1. RabbitMQ (Trường Phái "Bưu Điện Thông Minh")

**Định nghĩa:** RabbitMQ là một Message Broker truyền thống dựa trên chuẩn AMQP. Nó hành xử giống hệt một bưu điện thông minh.

### ⚙️ Cách hoạt động (Smart Broker, Dumb Consumer)
1.  **Thông Minh Tại Lõi (Smart Broker):** RabbitMQ nhận gói tin từ Producer, và dùng **Exchange** (Mạng lưới định tuyến) để xem xét xem nên vứt gói tin này vào **Queue** (Hộp thư) nào dựa trên "Routing Keys" (Mã bưu điện).
2.  **Khách Hàng Ngốc Nghếch (Dumb Consumer):** Service nhận đồ (Consumer) chỉ việc ngồi chờ. RabbitMQ sẽ chủ động **Tọng tin nhắn (Push)** vào mồm Consumer. Ăn xong (Xử lý xong), Consumer báo "ACK" (Đã nhận). Nhận xong, RabbitMQ lập tức **Xóa vĩnh viễn tin nhắn đó khỏi ổ cứng**.

### 🌟 Khi Nào Dùng RabbitMQ?
- Nhu cầu Routing định tuyến siêu phức tạp (Chuyển Email cho Queue A, Chuyển Lỗi cho Queue B).
- Các Background Jobs rải rác: Xử lý Resize ảnh, Bắn gửi Email OTP, Nạp Credit tự động. (Những việc làm xong là bỏ, không cần lưu lại dấu vết sự kiện).

---

## 🛸 2. Apache Kafka (Trường Phái "Sổ Xố Cuộc Đời Nhớ Dai")

**Định nghĩa:** Kafka KHÔNG PHẢI LÀ QUEUE. Nó là một **Distributed Commit Log** (Sổ ghi chép phân tán bất biến). Hình dung nó như hệ thống sổ tay của kế toán viên, viết xuống là không bao giờ sửa hoặc tẩy xóa.

### ⚙️ Cách hoạt động (Dumb Broker, Smart Consumer)
1.  **Lõi Cứng Đầu "Ngu Ngốc" (Dumb Broker):** Kafka chỉ làm đúng 1 việc: Ghi tin nhắn (Event) vào Cuối Đuôi ổ cứng (Append-Only Log) theo Topic. Ghi nhanh khủng khiếp. Không màng định tuyến phức tạp.
2.  **Khách Hàng Tự Trị (Smart Consumer):** Kafka KHÔNG bắn tin nhắn đi. Consumer phải chủ động hỏi "Anh ơi có tin gì mới không?" **(Pull Model)**. 
3.  **Bất Tử Hóa Dữ Liệu:** Độc đáo nhất, Kafka **KHÔNG XÓA MESSAGE** khi Consumer đọc xong. Nó giữ lại (theo ngày hoặc dung lượng). Consumer tự phải nhớ trang sách mình đã đọc tới đâu bằng con số gọi là **Offset**. Đọc chết thì thôi, máy sau lên tự nhìn Offset đọc tiếp.

### 🌟 Bóc Tách Sức Mạnh (Thuật Ngữ Vàng)
*   **Partition:** 1 Quyển Sổ (Topic) được xé thành nhiều tập (Partitions) ném lên nhiều máy chủ khác nhau. Nhờ xé lẻ này, 100 Consumers có thể đọc cùng lúc 1 Topic mà không đá chân nhau -> *Scale siêu hạng không điểm thắt cổ chai*.
*   **Consumer Groups:** Kafka cho phép nhiều nhóm Consumer tải chung 1 Topic. Anh A đọc gửi Email, Chị B đọc cập nhật Search Engine DB, Bác C đọc đưa vào Data Warehouse. Tất cả đọc chung 1 File Sổ Xố mà không tốn công copy!

### 🌟 Khi Nào Dùng Apache Kafka?
- **Event Sourcing / Event Streaming:** Mọi thao tác trên trang (Click, Add Cart, Checkout) là 1 Dây Sự Kiện đổ vào Kafka. (Ví dụ: Chuyển dữ liệu Microservice Data Sync khổng lồ liên tục Real-time).
- Cần **Replay Events**: Server chết 3 ngày, mất sạch Database? Bật Node mới lên, vặn Offset Kafka về số 0, đọc lại tuốt luốt dữ kiện 3 ngày dựng lại Database nguyên trạng! (Zero Data Loss).

---

## 🥊 3. Bảng Tóm Tắt Định Quyết Lựa Chọn

| Tiêu Chí | RabbitMQ (Bưu Điện) | Apache Kafka (Sổ Nhật Ký Bất Tử) |
| :--- | :--- | :--- |
| **Bản chất kiến trúc** | Queue thông minh (Push) | Log phân tán lưu trữ (Pull) |
| **Xóa Tin Nhắn** | Gửi xong xóa luôn 🔥 | Lưu chết trên Đĩa (Retention) 🧊 |
| **Thứ Tự (Ordering)** | Không đảm bảo tuyệt đối ở quy mô bự | Đảm bảo tuyệt đối trong Lõi Partition 1 Mạch |
| **Độ Phức Tạp Định Tuyến** | Có sẵn hệ thống Top Keys Rẽ Nhánh Thông Minh | "Khách tự chia tự hiểu" |
| **Hiệu suất / Tốc Độ Tải** | ~50k/giây (Nghẽn RAM/CPU nếu Queue Đầy) | Cả Triệu tin nhắn/s (Vì lưu tuần tự xuống Ổ Đĩa IO) |
| **Lời Khuyên Use Code:** | Hệ thống vừa, Worker Gửi Email Ngắn, Nhanh Dọn Hàng Rác. | Big Data Streaming, Cần Data Vĩnh Viễn Để Phân Tích Sync Dữ Liệu Khắc Máy Khác. |

> **🔥 Kết Luận Chốt Hạ Của Backend Staff:** Nếu làm Hệ Ngắn Khớp Job Run - Nhấc thỏ (RabbitMQ). Nếu dựng Xương Sống System Đồng Bộ Siêu Cấu Trúc Toàn App Toàn Vẹn Microservices Tách Data - Build Lõi Bằng Sổ Trạm Log (Kafka).
