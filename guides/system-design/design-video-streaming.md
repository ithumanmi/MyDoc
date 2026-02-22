# 🎥 Deep Dive: Design Video Streaming Platform (YouTube/Netflix)

> **"Mục tiêu: Thiết kế một hệ thống cho phép người dùng tải lên video, chuyển đổi định dạng (encoding) và xem trực tuyến (streaming) với độ trễ thấp và chất lượng thích ứng."**

---

## 1. Clarify Requirements (Làm rõ yêu cầu)

### Functional Requirements
*   **Uploading:** Người dùng có thể upload video.
*   **Streaming:** Người dùng có thể xem video trên web/mobile.
*   **Searching:** Tìm kiếm video theo tiêu đề.
*   **Quality Switching:** Tự động điều chỉnh chất lượng dựa trên tốc độ mạng.

### Non-Functional Requirements
*   **Highly Reliable:** Không mất video đã upload.
*   **High Scalability:** Phục vụ hàng tỷ lượt xem mỗi ngày.
*   **Low Latency:** Thời gian "buffering" thấp nhất có thể.

---

## 2. Back-of-the-envelope Estimation (Ước lượng)
*   **Users:** 1 tỷ DAU.
*   **Views:** Trung bình 5 video/user/ngày -> 5 tỷ lượt xem/ngày.
*   **Storage:** Giả sử mỗi phút video chiếm 50MB. Nếu mỗi ngày có 100k giờ video mới -> 100k * 60 * 50MB = 300TB/ngày.
*   **Bandwidth:** Streaming chiếm phần lớn băng thông quốc tế. Đây là bài toán cực nặng về **Egress traffic**.

---

## 3. High-level Design

### Components
*   **Web Server:** Xử lý metadata, auth, search.
*   **Blob Storage:** Lưu video gốc và video đã qua xử lý (dùng S3/GCS).
*   **Transcoding Pipeline:** Chuyển đổi video sang các định dạng (MP4, DASH) và độ phân giải (360p, 720p, 1080p, 4K) khác nhau.
*   **CDN (Content Delivery Network):** Đưa video đến gần người dùng nhất để giảm độ trễ.

---

## 4. Deep Dive: Transcoding & Adaptive Streaming

Đây là "trái tim" của hệ thống video.

### Video Transcoding Pipeline
Khi một video 4K được upload, ta không thể gửi file 4K đó cho người dùng dùng mạng 3G.
1.  **Chipping:** Chia video thành các đoạn nhỏ (chunks) - ví dụ 2-5 giây mỗi chunk.
2.  **Parallel Processing:** Dùng các worker để encode song song các chunk sang nhiều độ phân giải khác nhau.
3.  **DAG (Directed Acyclic Graph):** Quy trình xử lý phức tạp (watermarking, thumbnail extraction, encoding) được quản lý bởi một DAG để đảm bảo thứ tự và khả năng retry.

### Adaptive Bitrate Streaming (ABR)
Hệ thống sử dụng các giao thức như **HLS (Apple)** hoặc **DASH (MPEG)**.
*   Máy nghe (Client) sẽ dựa trên tốc độ internet hiện tại để chủ động yêu cầu chunk video tiếp theo ở độ phân giải phù hợp.
*   Nếu mạng yếu -> Client bốc chunk 360p. Nếu mạng mạnh -> Client bốc chunk 1080p.

---

## 5. Deep Dive: Content Delivery Network (CDN)

Streaming video mà không có CDN là không thể thực hiện được ở quy mô lớn.
*   **Edge Servers:** Video được lưu tại các máy chủ đặt tại ISP (Viettel, VNPT, FPT) để người dùng tải dữ liệu ngay trong nước thay vì đi qua cáp quang biển.
*   **Caching Strategy:** 
    *   Video phổ biến (Trending): Lưu ở tất cả các Edge nodes.
    *   Video cũ/ít người xem: Lưu ở Origin Storage, chỉ đẩy lên CDN khi có yêu cầu.

---

## 6. Interview Pro-tips (Trade-offs)

1.  **Upload vs View:** Upload có thể chậm (Asynchronous), nhưng View phải nhanh (Real-time). Hãy tập trung vào việc tối ưu đường ra (Egress).
2.  **Cost Optimization:** CDN rất đắt. Netflix tự xây dựng hệ thống CDN riêng gọi là **Open Connect** để tiết kiệm chi phí trả cho bên thứ 3 như Akamai hay Cloudflare.
3.  **Blob Storage:** Video gốc (Original) nên được lưu ở "Cold Storage" (rẻ tiền) sau khi đã được encode xong để dự phòng.

---

## 📚 Bài tiếp theo
*   [Design Distributed Cache (Redis Concept)](./design-distributed-cache.md)
