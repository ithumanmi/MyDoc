# 📂 Deep Dive: Design File Storage System (Google Drive/Dropbox)

> **"Mục tiêu: Thiết kế một hệ thống lưu trữ tệp tin đám mây cho phép người dùng tải lên, tải về, chia sẻ và đồng bộ hóa tệp tin trên nhiều thiết bị."**

---

## 1. Clarify Requirements (Làm rõ yêu cầu)

### Functional Requirements
*   **File Upload/Download:** Tải tệp lên và tải tệp về.
*   **Syncing:** Tệp tin tự động cập nhật trên mọi thiết bị (Laptop, Mobile).
*   **Versioning:** Xem lịch sử và khôi phục các phiên bản cũ của tệp.
*   **Sharing:** Chia sẻ tệp/thư mục cho người dùng khác với quyền đọc/ghi.

### Non-Functional Requirements
*   **Reliability:** Không được mất tệp tin (Độ bền dữ liệu cực cao).
*   **Consistency:** Khi cập nhật ở thiết bị A, thiết bị B phải thấy thay đổi sớm nhất có thể.
*   **Scalability:** Hỗ trợ hàng tỷ tệp tin và hàng triệu người dùng.

---

## 2. High-level Design

### Components
*   **Block Server:** Xử lý việc chia nhỏ tệp thành các khối (chunks) để upload/download hiệu quả.
*   **Metadata DB:** Lưu thông tin về tệp (tên, kích thước, đường dẫn) và các phiên bản.
*   **Object Storage:** Nơi lưu trữ thực sự các khối dữ liệu (dùng S3/GCS).
*   **Notification Service:** Thông báo cho các thiết bị khác khi có thay đổi tệp để bắt đầu quá trình đồng bộ.

---

## 3. Deep Dive: Efficiency & Reliability (Trọng tâm)

### Chunking (Chia nhỏ tệp)
Thay vì upload toàn bộ 1 file 1GB, hệ thống chia nhỏ thành các khối (ví dụ 4MB).
*   *Lợi ích:* 
    *   **Retry:** Nếu upload thất bại, chỉ cần upload lại chunk đó.
    *   **Differential Sync:** Nếu chỉ sửa 1 câu trong file, hệ thống chỉ cần upload chunk chứa thay đổi đó.

### Deduplication (Loại bỏ trùng lặp)
Nếu 1.000 người cùng upload một file giáo trình nặng 100MB, hệ thống có lưu 100GB không?
*   **Giải pháp:** Hash từng chunk. Nếu chunk đó đã tồn tại trong Object Storage, Metadata chỉ việc trỏ link đến chunk cũ thay vì lưu mới.
*   *Kết quả:* Tiết kiệm chi phí lưu trữ khổng lồ.

### Metadata DB Sharding
Với hàng tỷ tệp tin, DB metadata sẽ trở nên rất lớn.
*   **Sharding theo `user_id`:** Tất cả tệp của 1 user sẽ nằm cùng 1 node, giúp các thao tác duyệt thư mục và tìm kiếm của user đó nhanh hơn.

---

## 4. Deep Dive: Syncing Mechanism

Làm sao để thiết bị B biết thiết bị A vừa sửa file?
1.  **Thiết bị A:** Upload chunk mới -> Update Metadata -> Gửi tín hiệu đến Notification Service.
2.  **Notification Service:** Dùng **Long Polling** hoặc **WebSocket** để đẩy tín hiệu "New Update" đến các thiết bị đang online của người dùng đó.
3.  **Thiết bị B:** Nhận tín hiệu -> So sánh version trong Metadata -> Chỉ tải về các chunk bị thay đổi.

---

## 5. Conflict Handling (Xử lý xung đột)
Khi 2 người cùng sửa 1 file lúc offline và cùng online cùng lúc:
*   **Strategy:** Hệ thống tạo ra 2 version khác nhau (Conflicted copy) và yêu cầu người dùng tự giải quyết (Merge manual) giống như Git.

---

## 6. Interview Pro-tips (Trade-offs)

1.  **Strong vs Eventual Consistency:** Metadata cần **Strong Consistency** (không thể thấy file tồn tại nhưng click vào lại báo lỗi). Dữ liệu chunk có thể chấp nhận **Eventual Consistency** trong quá trình đồng bộ.
2.  **Storage Costs:** Đề cập đến chiến lược **Cold Storage** (lưu các version cũ hoặc file lâu không dùng vào loại đĩa rẻ tiền hơn).

---

## 📚 Bài tiếp theo
*   [Design Rate Limiter](./design-rate-limiter.md)
