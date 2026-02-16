# 🤖 Automation Tools: Quy trình tự động hóa MMO

> [← Back to Network Security](../README.md)

Automation giúp bạn scale từ 1 tài khoản lên 10.000 tài khoản. Nhưng automation không thông minh sẽ bị ban hàng loạt.

---

## 1. Browser Automation Tools

### **A. Code-based (Dành cho Dev)**
*   **Selenium / Puppeteer:** Kinh điển. Nhưng dễ bị phát hiện do biến `navigator.webdriver = true`.
*   **Playwright:** Mới, nhanh hơn, hỗ trợ giả lập Mobile tốt hơn.
*   **Stealth Plugin:** (Ví dụ: `puppeteer-extra-plugin-stealth`). Bắt buộc phải dùng để che giấu dấu vết Automation.

### **B. No-Code / Low-Code (Dành cho MMO)**
*   **ZennoPoster:** "Ông trùm" MMO. Kéo thả logic, multithread mạnh, nhưng chạy trên Windows và tốn tài nguyên.
*   **BAS (Browser Automation Studio):** Miễn phí, mạnh mẽ, có thể compile ra file `.exe` để bán tool.
*   **Automa:** Extension Chrome để tự động hóa các task đơn giản (Click, Scroll).

---

## 2. Mobile Automation (Phone Farm)

Nuôi nick TikTok, Facebook trên điện thoại thật bao giờ cũng "trâu" hơn giả lập.

### **Mô hình Phone Farm:**
1.  **Hardware:** 20-50 điện thoại Android cũ (Samsung S8, Note 8) tháo pin, cấp nguồn trực tiếp (để không cháy nổ).
2.  **Hub USB:** Kết nối tất cả vào 1 máy tính.
3.  **Software Control:**
    *   **ADB (Android Debug Bridge):** Gõ lệnh điều khiển (`adb shell input tap x y`).
    *   **Scrcpy:** View màn hình nhiều máy cùng lúc.
    *   **Total Control / ATP Software:** Tool thương mại để quản lý farm.

### **Quy trình nuôi:**
*   Mỗi máy 1 Proxy 4G riêng.
*   Script tự động lướt Newfeed, like dạo, xem video ngẫu nhiên (Random behavior) để tăng Trust.

---

## 3. SMS & OTP Verification

Rào cản lớn nhất của Reg acc là số điện thoại.

### **Giải pháp:**
1.  **Thuê SIM (Sim thuê):** Các dịch vụ nhận OTP giá rẻ (1000đ - 3000đ/code).
    *   *Nhược điểm:* Số dùng lại nhiều lần (re-used), dễ bị checkpoint sau này.
2.  **Nuôi SIM thật:** Mua hàng trăm SIM rác, cắm vào **GSM Modem** (Khay SIM).
    *   Tự viết tool đọc tin nhắn từ Modem.
    *   Chủ động, an toàn, nhưng tốn tiền gia hạn SIM.

---

## 4. Anti-Bot Detection (Vượt qua tường lửa AI)

Các trang web lớn (Cloudflare, Akamai) dùng AI để phát hiện Bot.

### **Dấu hiệu Bot:**
*   **Mouse Movement:** Di chuyển chuột thẳng tắp (Linear) -> Bot. (Người dùng di chuột cong cong, run run).
*   **Timing:** Bấm nút "Submit" quá nhanh (ngay khi trang vừa load).
*   **Network:** Load trang nhưng không tải ảnh/CSS (để tiết kiệm băng thông) -> Bot.

### **Kỹ thuật Human Emulation:**
*   Thêm `Random Sleep` giữa các hành động.
*   Sử dụng thư viện tạo chuyển động chuột cong (Bezier Curve).
*   Gõ phím từng ký tự một (với tốc độ không đều), thay vì Paste `Ctrl+V`.
