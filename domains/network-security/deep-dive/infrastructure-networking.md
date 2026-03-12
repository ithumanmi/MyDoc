# 🏗️ Infrastructure & Modern Networking

> [← Back to Network Security](../README.md)

Internet hiện đại không chỉ là dây cáp và router. Nó là CDN, Edge Computing và triết lý Zero Trust.

---

## 1. Routing & NAT (Định tuyến)

### **A. Public vs Private IP**
*   **Public IP:** Duy nhất toàn cầu. Do ISP cấp. Đắt tiền.
*   **Private IP:** Dùng trong mạng LAN (`192.168.x.x`, `10.x.x.x`). Miễn phí.

### **B. NAT (Network Address Translation)**
*   Router đóng vai trò người phiên dịch.
*   Khi bạn truy cập Web: Router thay IP Private của bạn bằng IP Public của nó.
*   Khi Web trả lời: Router nhận gói tin, tra bảng NAT, gửi lại cho IP Private của bạn.

---

## 2. CDN (Content Delivery Network)

Làm sao Netflix stream phim 4K cho bạn mượt mà dù Server gốc ở Mỹ?

*   **Nguyên lý:** Cache nội dung tĩnh (Ảnh, Video, CSS) tại các Server rìa (Edge Server) đặt khắp thế giới (gần nhà bạn).
*   **Anycast DNS:** Một IP Public được gán cho nhiều Server ở nhiều vị trí khác nhau. Người dùng ở đâu sẽ được định tuyến đến Server gần nhất.

---

## 3. VPN vs Zero Trust

### **A. VPN (Mô hình Lâu đài & Hào nước)**
*   **Tư duy cũ:** Bên ngoài là kẻ thù, bên trong là bạn bè.
*   **Cách làm:** Dùng VPN để chui qua tường lửa vào mạng nội bộ. Một khi đã vào được, bạn có thể truy cập mọi thứ.
*   **Rủi ro:** Hacker cướp được 1 tài khoản VPN -> Hack cả công ty.

### **B. Zero Trust (Không tin ai cả)**
*   **Tư duy mới:** "Never Trust, Always Verify". Kể cả đang ngồi trong văn phòng cũng không tin.
*   **Cách làm:**
    *   Xác thực từng Request (Identity-based).
    *   Kiểm tra sức khỏe thiết bị (Device Health).
    *   Cấp quyền tối thiểu (Least Privilege).
*   **Công cụ:** Google BeyondCorp, Cloudflare Access.

---

## 4. Modern Firewall

*   **Stateful Inspection:** Nhớ trạng thái kết nối (A đã gửi SYN cho B chưa?).
*   **Next-Gen Firewall (NGFW):**
    *   **Deep Packet Inspection (DPI):** Mổ xẻ nội dung gói tin (Layer 7) xem có chứa mã độc không.
    *   **Application Awareness:** Chặn Facebook Game nhưng cho phép Facebook Chat.

### 🔗 Related Labs & Guides
- **[Linux Hardening with UFW](../labs/linux-hardening-ufw.md):** Thực hành cấu hình firewall host-based và mapping tới concept NAT/ACL.
- **[Virtual Lab Setup](../labs/virtual-lab-setup.md):** Dựng lab multi-network để test NAT, VPN, firewall rules.
- **[IBM QRadar Use Case Engineering](../labs/qradar-detection-lab.md):** Kết nối log firewall/NAT đến SIEM để phát hiện DDoS/scan.
