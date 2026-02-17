# ☁️ How Amazon S3 Works: Deep Dive Architecture

> [← Back to Backend Roadmap](../README.md)

Bạn dùng S3 hàng ngày để lưu ảnh, video, log files. Nhưng bạn có bao giờ tự hỏi: *"Làm sao S3 có thể lưu trữ hàng nghìn tỷ object với độ bền 99.999999999% (11 số 9)?"*
Dưới đây là kiến trúc "chìm" của S3 mà ít người biết.

---

## 1. Bản chất của S3: Object Store 📦
*   S3 không phải là File System (như NTFS, ext4 trên máy tính bạn). Nó là **Object Store**.
*   Nó chuyên trị **Unstructured Data** (Dữ liệu phi cấu trúc): Ảnh, Video, Log files, Backup.
*   Bạn không thể "sửa" một phần của file. Bạn chỉ có thể ghi đè (Overwrite) toàn bộ file.

---

## 2. Microservices Architecture 🧩
S3 không phải là một cục phần mềm nguyên khối (Monolith). Nó được xây dựng từ hàng trăm **Microservices** nhỏ, mỗi service làm một việc cụ thể:
*   **Front-end:** Nhận request, xác thực (AuthN/AuthZ).
*   **Namespace:** Quản lý Buckets và tên file.
*   **Storage Node:** Quản lý đĩa cứng vật lý.

---

## 3. Tách biệt Metadata & Data (Separation) ✂️
Để scale được vô hạn, S3 tách file thành 2 phần riêng biệt:
1.  **Metadata:** Tên file, size, ngày tạo, quyền truy cập.
2.  **Data (Content):** Nội dung thực sự của file (bytes).

👉 **Lợi ích:** Bạn có thể liệt kê (List) hàng triệu file cực nhanh mà không cần chạm vào ổ cứng chứa dữ liệu.

---

## 4. Metadata Management 📇
*   **Lưu ở đâu?** Metadata được lưu trong một **Key-Value Database** hiệu năng cao (tương tự DynamoDB).
*   **Caching:** Metadata được cache rất mạnh để đảm bảo tính sẵn sàng cao (High Availability). Khi bạn request `GET /my-bucket/image.jpg`, S3 tra cứu metadata trong cache trước.

---

## 5. Data Storage: HDD is King 💾
*   Mặc dù SSD nhanh hơn, nhưng **HDD (Mechanical Hard Disk)** rẻ hơn rất nhiều.
*   S3 dùng HDD để lưu trữ dữ liệu gốc nhằm tối ưu chi phí cho khách hàng.
*   Để bù lại tốc độ chậm của HDD, họ dùng các kỹ thuật tối ưu hóa (xem mục 6 & 8).

---

## 6. ShardStore & LSM Tree 🌳
*   Làm sao để tìm dữ liệu nhanh trên ổ HDD quay chậm chạp?
*   S3 sử dụng **ShardStore** - một biến thể của **LSM Tree (Log-Structured Merge-tree)**.
*   **Nguyên lý:** Dữ liệu mới luôn được ghi tuần tự (Sequential Write) vào đĩa (append-only). Điều này giúp HDD đạt tốc độ ghi tối đa, tránh việc đầu đọc phải di chuyển lung tung (Random Seek).

---

## 7. Erasure Coding (Thay vì Replication) 🛡️
*   **Replication truyền thống:** Copy file ra 3 bản (chiếm 300% dung lượng). An toàn nhưng tốn kém.
*   **Erasure Coding (EC):** Chia file thành các mảnh nhỏ (Data Shards) + các mảnh sửa lỗi (Parity Shards).
    *   Ví dụ: Chia file thành 10 mảnh data + 4 mảnh parity.
    *   Chỉ cần 10 mảnh bất kỳ là khôi phục được file.
    *   Chiếm khoảng 140% dung lượng (Tiết kiệm hơn nhiều so với 300%).

---

## 8. Parallelism & Throughput ⚡
*   **Replication:** Dù dùng EC, S3 vẫn phân tán các mảnh dữ liệu ra hàng trăm đĩa cứng khác nhau trên nhiều Data Center (Availability Zones).
*   **Parallel Read:** Khi bạn tải một file lớn, S3 đọc song song từ nhiều đĩa cùng lúc. Đó là lý do S3 có throughput (băng thông) cực lớn.

---

## 🎯 Tóm Lại
S3 là một kiệt tác của System Design:
1.  Dùng phần cứng rẻ tiền (HDD) nhưng đạt hiệu năng cao nhờ phần mềm thông minh (**LSM Tree, Parallelism**).
2.  Đạt độ bền vô đối nhờ toán học (**Erasure Coding**) thay vì chỉ copy thô thiển.
3.  Scale vô hạn nhờ tách biệt **Metadata** và **Data**.
