# 🌐 Proxy & Network Infrastructure for MMO

> [← Back to Network Security](../README.md)

"IP xấu là chết." Trong MMO, chất lượng Proxy quyết định 50% sự sống còn của tài khoản.

---

## 1. Phân loại Proxy cho MMO

### **A. Datacenter Proxy (IP Server)**
*   **Nguồn:** AWS, Google Cloud, DigitalOcean.
*   **Đặc điểm:** Tốc độ siêu nhanh, ping thấp, rẻ.
*   **Nhược điểm:** Dải IP (Subnet) bị đánh dấu là "Hosting".
*   **Sử dụng:** Crawl data (Shopee, Amazon), Spam comment web rác.
*   **KHÔNG DÙNG:** Reg acc Facebook, Google, TikTok (Chết ngay lập tức).

### **B. Residential Proxy (IP Dân cư) ⭐⭐⭐**
*   **Nguồn:** Máy tính/Wifi của người dùng thật (được thuê lại hoặc... botnet).
*   **Đặc điểm:** ISP là VNPT, FPT, Viettel... Độ tin cậy (Trust Score) cực cao.
*   **Nhược điểm:** Chậm, không ổn định, đắt (tính tiền theo GB).
*   **Sử dụng:** Reg account, Checkout hàng hiệu (Sneaker), Nuôi nick quý.

### **C. Mobile Proxy (4G/5G)**
*   **Nguồn:** Từ SIM điện thoại.
*   **Đặc điểm:** Một trạm BTS có hàng nghìn người dùng chung 1 IP Public. Do đó, Facebook/Google **KHÔNG DÁM CHẶN** IP 4G (vì sợ chặn nhầm người dùng thật).
*   **Ưu điểm:** Reset IP cực nhanh (Bật/Tắt chế độ máy bay). IP luôn sạch.
*   **Sử dụng:** Farm tài khoản số lượng lớn (Mass Account Creation).

---

## 2. Xây dựng Proxy Farm (Tự làm)

Thay vì đi mua (đắt), dân MMO chuyên nghiệp tự xây Farm 4G.

### **Mô hình USB Dongle Farm:**
*   **Phần cứng:** *(xem [4G Farm Hardware Guide](./network/4g-farm-hardware-guide.md))*
    *   1 PC/Server hoặc Raspberry Pi.
    *   1 USB Hub (có nguồn phụ 12V).
    *   10-20 USB 4G (Dcom 3G) + SIM Data trọn gói.
*   **Phần mềm:**
    *   **Proxy Server:** Squid hoặc 3Proxy.
    *   **Tool đổi IP:** Viết script Python gửi lệnh AT Command đến USB để reset kết nối (*tham chiếu [AT Commands Reference](./network/at-commands-reference.md)*).
*   **Kết quả:** Bạn có 20 luồng Proxy xoay (Rotating) private, không chung đụng với ai.

---

## 3. Proxy Rotation Strategy (Chiến thuật Xoay)

### **Sticky IP (IP Tĩnh theo phiên):** *(chi tiết rotation xem [IP Rotation Algorithms](./network/ip-rotation-algorithms.md))*
*   Giữ nguyên 1 IP trong 10-30 phút để hoàn thành 1 quy trình (Reg nick -> Verify mail -> Upload avatar).
*   Nếu IP đổi giữa chừng -> Web nghi ngờ -> Checkpoint.

### **Rotating IP (Xoay liên tục):**
*   Đổi IP sau mỗi Request.
*   Dùng để: Crawl giá sản phẩm, Check thứ hạng từ khóa SEO.

---

## 4. Check IP Sạch (IP Score)

Trước khi dùng Proxy vào việc quan trọng, hãy kiểm tra "sức khỏe" của nó.
*   **IPhey / Whoer:** Kiểm tra xem có bị lộ DNS, WebRTC không.
*   **Scamalytics / IPQualityScore:** Kiểm tra điểm gian lận (Fraud Score).
    *   Score < 30: An toàn.
    *   Score > 70: Vứt ngay (IP đã bị Blacklist).

## 5. Quản lý Geo & Provider
- Đồng bộ IP, timezone, GPS theo [Geolocation Spoofing Guide](./network/geolocation-spoofing.md).
- So sánh dịch vụ mua proxy dân cư tại [Residential Provider Comparison](./network/residential-proxy-providers-comparison.md).
- 🔗 **Cross-domain:** Xem thêm [Infrastructure & Modern Networking](../network-security/deep-dive/infrastructure-networking.md) để hiểu routing, NAT, Zero Trust và áp dụng guardrail khi build proxy farm.
