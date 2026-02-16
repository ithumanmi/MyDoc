# 🕵️ Anonymity & OpSec: Nghệ thuật Tàng hình

> [← Back to Network Security](./README.md)

"Privacy is not a crime."
Trong thế giới bị giám sát 24/7, giữ an toàn danh tính (OpSec) là kỹ năng sống còn, không chỉ cho Hacker mà còn cho nhà báo, nhà hoạt động xã hội.

---

## 1. OpSec (Operational Security)

OpSec là quy trình bảo vệ các mẩu thông tin nhỏ (mà khi ghép lại có thể lộ danh tính thật).

### **Quy tắc vàng của OpSec:**
1.  **Compartmentalization (Chia ngăn):** Tách biệt các danh tính.
    *   Danh tính thật (Real Life): Facebook, Bank, Shopee.
    *   Danh tính ảo (Cyber): Hacker forum, Dark Web.
    *   *Tuyệt đối không:* Dùng chung Username, Password, Email, Số điện thoại giữa 2 thế giới này.
2.  **Trust No One:** Không tin tưởng VPN Provider, ISP, hay thậm chí là Tor. Luôn có lớp bảo vệ thứ 2.
3.  **Loose Lips Sink Ships:** Khoe khoang chiến tích là cách nhanh nhất để bị bắt.

---

## 2. Tor & The Dark Web

### **A. Tor (The Onion Router)**
*   **Cơ chế:** Dữ liệu được mã hóa nhiều lớp và đi qua 3 trạm trung chuyển ngẫu nhiên (Guard -> Middle -> Exit).
    *   Trạm đầu chỉ biết bạn là ai, không biết bạn đi đâu.
    *   Trạm cuối chỉ biết bạn đi đâu, không biết bạn là ai.
*   **Sử dụng:** Tải **Tor Browser** (Dựa trên Firefox).

### **B. Onion Services (Dark Web)**
*   Các website có đuôi `.onion`. Chỉ truy cập được qua Tor.
*   Ẩn danh cả người truy cập lẫn chủ sở hữu website.
*   *Lưu ý:* Dark Web chứa nhiều nội dung bất hợp pháp. Hãy cẩn thận.

---

## 3. Privacy Tools (Bộ công cụ)

### **A. Hệ điều hành: Tails OS**
*   **The Amnesic Incognito Live System.**
*   Chạy trực tiếp từ USB.
*   Mọi kết nối bắt buộc qua Tor.
*   **Quên sạch mọi thứ:** Rút USB ra -> RAM bị xóa -> Không để lại dấu vết gì trên máy tính.

### **B. VPN (Mạng riêng ảo)**
*   Giấu IP thật của bạn khỏi ISP (Nhà mạng) và Website đích.
*   *Chọn VPN:* Không lưu Log (No-log policy), nằm ngoài liên minh tình báo "14 Eyes". (Gợi ý: Mullvad, ProtonVPN).

### **C. Giao tiếp an toàn**
*   **Email:** ProtonMail (Mã hóa PGP đầu cuối).
*   **Chat:** Signal (Mã hóa, không lưu metadata). Tránh dùng Messenger/Zalo cho việc nhạy cảm.

---

## 4. Metadata: Kẻ thù thầm lặng

Bạn gửi một bức ảnh cho ai đó. Bạn nghĩ mình chỉ gửi ảnh?
Không, bạn gửi cả:
*   **EXIF Data:** Loại máy ảnh, Ngày giờ chụp.
*   **GPS Coordinates:** Tọa độ chính xác nơi chụp (Nhà bạn!).

> **Giải pháp:** Dùng tool (như `exiftool`) để xóa Metadata trước khi upload ảnh.
