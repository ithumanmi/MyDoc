# 🌐 Networking Fundamentals: Mạng căn bản

> [← Back to Network Security](./README.md)

Internet không phải là phép thuật. Nó là hàng tỷ thiết bị nói chuyện với nhau bằng các quy tắc (Protocols) cụ thể.

---

## 1. Mô hình OSI (7 Layers)

Hãy tưởng tượng bạn gửi một lá thư. Nó phải đi qua nhiều bước (viết thư -> bỏ phong bì -> dán tem -> bưu điện -> xe tải -> người nhận).
Mạng cũng vậy. Dữ liệu đi qua 7 lớp:

| Layer | Tên | Chức năng chính | Giao thức/Thiết bị |
| :--- | :--- | :--- | :--- |
| **7** | **Application** | Giao diện người dùng (User Interface). | HTTP, FTP, DNS, SMTP |
| **6** | **Presentation** | Mã hóa/Giải mã dữ liệu (Format data). | SSL/TLS, JPEG, ASCII |
| **5** | **Session** | Thiết lập/Duy trì kết nối (Connection). | NetBIOS, RPC |
| **4** | **Transport** | Truyền dữ liệu tin cậy (End-to-end delivery). | **TCP**, **UDP** |
| **3** | **Network** | Định tuyến (Routing - Tìm đường đi). | **IP**, Router |
| **2** | **Data Link** | Truyền dữ liệu trong mạng LAN (MAC Address). | Ethernet, Switch |
| **1** | **Physical** | Tín hiệu vật lý (Bit 0/1). | Cáp quang, Wifi, Hub |

> **Ghi nhớ:** "Please Do Not Throw Sausage Pizza Away" (Physical -> Application).

---

## 2. TCP vs UDP (Layer 4)

Khi gửi dữ liệu, bạn chọn "Tin cậy" hay "Tốc độ"?

*   **TCP (Transmission Control Protocol):**
    *   **Đặc điểm:** Tin cậy. Đảm bảo dữ liệu đến nơi đầy đủ, đúng thứ tự. Có bắt tay 3 bước (3-way handshake).
    *   **Ví dụ:** Web (HTTP), Email, File Transfer. (Mất 1 gói tin -> Web lỗi -> Gửi lại).
*   **UDP (User Datagram Protocol):**
    *   **Đặc điểm:** Nhanh. "Fire and forget". Gửi đi không cần biết có nhận được không.
    *   **Ví dụ:** Streaming video, Game Online, DNS. (Mất 1 frame hình -> Kệ, hiện frame tiếp theo -> Không bị lag).

---

## 3. IP Address & DNS

*   **IP Address (Địa chỉ nhà):** Mỗi thiết bị có 1 IP định danh (VD: `192.168.1.1`).
    *   **IPv4:** 32-bit (Hết địa chỉ).
    *   **IPv6:** 128-bit (Dùng mãi không hết).
*   **DNS (Domain Name System - Danh bạ):**
    *   Con người nhớ tên (`google.com`). Máy tính chỉ hiểu số (`142.250.183.206`).
    *   DNS Server giúp dịch Tên -> Số.

---

## 4. Subnetting & Routing

*   **Subnetting:** Chia một mạng lớn thành các mạng nhỏ để dễ quản lý và bảo mật.
    *   *Ví dụ:* Phòng Kế toán (VLAN 10) không thể truy cập máy in của phòng Giám đốc (VLAN 20).
*   **NAT (Network Address Translation):**
    *   IP Private (trong nhà): `192.168.x.x` (Trùng nhau thoải mái).
    *   IP Public (ngoài đường): Duy nhất trên toàn cầu.
    *   Router dùng NAT để thay mặt cả nhà đi ra Internet bằng 1 IP Public.
