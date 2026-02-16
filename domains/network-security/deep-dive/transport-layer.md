# 🚚 Transport Layer Internals: Lớp Giao vận

> [← Back to Network Security](../README.md)

Lớp 4 (Transport) chịu trách nhiệm đưa dữ liệu từ ứng dụng này sang ứng dụng kia một cách trọn vẹn (hoặc nhanh nhất).

---

## 1. TCP (Transmission Control Protocol) - "Quý ông Tin cậy"

TCP đảm bảo: Không mất gói tin, đúng thứ tự, không bị lỗi.

### **A. 3-Way Handshake (Bắt tay 3 bước)**
Trước khi gửi dữ liệu, 2 bên phải chào nhau:
1.  **SYN:** "Alo, tôi muốn kết nối." (Client -> Server)
2.  **SYN-ACK:** "Ok, tôi nghe rồi. Bạn có nghe tôi không?" (Server -> Client)
3.  **ACK:** "Nghe rõ. Bắt đầu nhé!" (Client -> Server)

### **B. Flow Control (Điều khiển Luồng)**
*   **Vấn đề:** Server gửi quá nhanh, Client không kịp xử lý (tràn bộ đệm RAM) -> Mất dữ liệu.
*   **Giải pháp (Sliding Window):** Client bảo Server: "Tôi chỉ còn chỗ cho 5 gói tin thôi". Server sẽ chỉ gửi 5 gói rồi dừng lại chờ xác nhận.

### **C. Congestion Control (Điều khiển Tắc nghẽn)**
*   **Vấn đề:** Mạng Internet bị tắc (nhiều người dùng quá).
*   **Giải pháp (Slow Start):**
    *   Ban đầu gửi chậm (1 gói).
    *   Nếu thấy ổn -> Gửi gấp đôi (2 gói -> 4 gói -> 8 gói).
    *   Nếu thấy mất gói (Mạng tắc) -> Giảm tốc độ ngay lập tức.

---

## 2. UDP (User Datagram Protocol) - "Kẻ Liều lĩnh"

UDP gửi dữ liệu đi mà không cần biết đích đến có nhận được hay không.

### **Đặc điểm:**
*   Không có Handshake (Connectionless).
*   Không có Flow/Congestion Control.
*   Mất gói tin? Kệ nó.

### **Tại sao dùng UDP?**
*   **Tốc độ:** Không tốn thời gian bắt tay.
*   **Real-time:** Trong game bắn súng hoặc gọi video, việc nhận lại gói tin cũ (bị lag 2s) là vô nghĩa. Thà bỏ qua luôn để hiển thị cái mới nhất.

---

## 3. Ports & Sockets

Làm sao máy tính biết gói tin này là của Chrome hay của Game? -> Dựa vào **Port**.

*   **Port:** Số hiệu cửa (0-65535).
    *   0-1023: Well-known ports (80 HTTP, 443 HTTPS, 22 SSH).
    *   1024-49151: Registered ports (3306 MySQL, 5432 Postgres).
    *   49152-65535: Dynamic/Private ports (Dùng tạm thời cho Client).
*   **Socket:** Cặp địa chỉ `IP:Port` (VD: `192.168.1.5:8080`).

---

## 4. QUIC (The Future is UDP)

Giao thức nền tảng của HTTP/3.
*   Thực chất là: **TCP + TLS + HTTP/2** được xây dựng lại trên nền **UDP**.
*   Chuyển phần xử lý tắc nghẽn từ Kernel (OS) lên User Space (Ứng dụng) -> Linh hoạt hơn, cập nhật nhanh hơn.
