# 🕵️ Browser Fingerprinting & Anti-Detect

> [← Back to Network Security](../README.md)

Trong thế giới MMO (Make Money Online), kẻ thù lớn nhất không phải là Hacker, mà là **AI của Google/Facebook/Amazon**. Nó biết bạn là ai, kể cả khi bạn đổi IP.

---

## 1. Browser Fingerprinting là gì?

Web server thu thập hàng trăm thông số nhỏ từ trình duyệt của bạn. Khi gộp lại, chúng tạo thành một "Dấu vân tay" (Fingerprint) duy nhất.
**Độ chính xác:** 99.5%.

### **Các thông số bị thu thập:**
1.  **Canvas Fingerprint:** Vẽ một hình ẩn. Mỗi Card màn hình (GPU) + Driver sẽ vẽ ra pixel hơi khác nhau một chút -> Lộ diện thiết bị.
2.  **AudioContext:** Cách card âm thanh xử lý tín hiệu.
3.  **WebGL:** Thông số chi tiết về GPU (Vendor, Renderer).
4.  **Fonts:** Danh sách font chữ đã cài trên máy (Máy Design nhiều font lạ -> Dễ bị phát hiện).
5.  **Screen Resolution:** Độ phân giải màn hình + Kích thước cửa sổ trình duyệt.
6.  **WebRTC:** Có thể làm lộ IP thật dù đang dùng VPN.

---

## 2. Anti-Detect Browser (Trình duyệt ẩn danh)

Trình duyệt thường (Chrome/Firefox) không cho phép đổi các thông số phần cứng này. Bạn cần trình duyệt chuyên dụng.

### **Cơ chế hoạt động:**
*   Tạo ra các **Profile** ảo độc lập.
*   Mỗi Profile giả lập một thiết bị khác nhau (Fake User-Agent, Fake Canvas, Fake WebGL...).
*   Cách ly Cookie/Cache hoàn toàn.

### **Các công cụ phổ biến (MMO Tools):**
1.  **Gologin / Multilogin / AdsPower:** (Trả phí). Mạnh, database vân tay chuẩn, ít bị phát hiện. Dùng để nuôi tài khoản Facebook Ads, Ebay, Amazon.
2.  **GenLogin:** (Việt Nam). Có tích hợp Automation (kéo thả).
3.  **HydraHeaders:** (Free/Open Source). Cơ bản, dùng để test.

---

## 3. Chiến lược "Nuôi" (Farming Strategy)

### **A. Consistency (Sự nhất quán)**
*   Đừng bao giờ đổi Fingerprint giữa chừng.
*   Profile A phải luôn dùng đúng bộ thông số A và Proxy A.
*   Nếu hôm nay bạn dùng iPhone 14 ở Mỹ, mai bạn dùng Samsung S23 ở Việt Nam -> **Checkpoint ngay lập tức.**

### **B. Cookies Aging (Làm già tài khoản)**
*   Tài khoản mới tạo (Fresh) rất yếu.
*   Phải cho đi "tương tác dạo" (lướt web, xem youtube, scroll facebook) trong 1-2 tuần để tạo lịch sử (Cookies History) trước khi làm việc chính (Reg acc, Chạy quảng cáo).

### **C. Tránh "WebRTC Leak"**
*   Luôn tắt WebRTC hoặc dùng extension chặn WebRTC để không bị lộ IP thật khi dùng VPN/Proxy.
