# 🎭 Social Engineering: Nghệ thuật Hacking Con người

> [← Back to Network Security](./README.md)

"Bạn có thể cài tường lửa giá 1 triệu đô, nhưng không thể vá lỗ hổng ngu ngốc của con người."
Social Engineering (SE) là kỹ thuật thao túng tâm lý để nạn nhân tự nguyện cung cấp thông tin mật.

---

## 1. Tại sao con người là mắt xích yếu nhất?

Con người có các điểm yếu tâm lý cố hữu ("Bug" trong não bộ):
1.  **Sợ hãi:** "Tài khoản của bạn bị khóa! Click vào đây để mở ngay."
2.  **Tham lam:** "Bạn đã trúng thưởng iPhone 15 Pro Max."
3.  **Thích giúp đỡ:** "Em là nhân viên mới, anh cho em mượn thẻ vào cửa chút được không ạ?"
4.  **Lười biếng:** Đặt mật khẩu là `123456` cho dễ nhớ.

---

## 2. Các kỹ thuật tấn công phổ biến

### **A. Phishing (Lừa đảo qua Email)**
*   **Mass Phishing:** Gửi email rác cho hàng nghìn người ("Tài khoản ngân hàng bị khóa").
*   **Spear Phishing:** Tấn công có mục tiêu cụ thể. Hacker tìm hiểu kỹ về nạn nhân (tên sếp, dự án đang làm) để email trông cực kỳ thật.
    *   *Ví dụ:* Email từ `ceo@company-update.com` (Fake) gửi cho kế toán: "Chuyển tiền cho đối tác X gấp."

### **B. Vishing (Voice Phishing)**
*   Gọi điện thoại giả danh Công an, Nhân viên ngân hàng.
*   "Anh có biên lai phạt nguội, vui lòng chuyển tiền..."

### **C. Pretexting (Kịch bản giả mạo)**
*   Hacker bịa ra một kịch bản để lấy lòng tin.
*   *Ví dụ:* Giả làm nhân viên IT: "Chào chị, hệ thống đang bảo trì, chị đọc giúp em mật khẩu để em backup dữ liệu."

### **D. Baiting (Thả thính)**
*   Vứt một cái USB có dán nhãn "Luong_Thuong_2024.xlsx" ở bãi xe công ty.
*   Nhân viên tò mò nhặt được -> Cắm vào máy tính công ty -> Virus kích hoạt -> Hacker xâm nhập mạng nội bộ.

---

## 3. OSINT: Open Source Intelligence

Trước khi tấn công, Hacker phải thu thập thông tin (Reconnaissance).
Họ tìm kiếm thông tin CÔNG KHAI của bạn trên mạng.

*   **Google Dorking:** Kỹ thuật search Google nâng cao.
    *   `site:linkedin.com "manager" "fpt"` -> Tìm danh sách quản lý FPT trên LinkedIn.
    *   `filetype:pdf "confidential"` -> Tìm tài liệu mật bị lộ.
*   **Social Media:** Facebook, Instagram, TikTok.
    *   Bạn post vé máy bay? -> Lộ Barcode, Lộ lịch trình.
    *   Bạn post ảnh bàn làm việc? -> Lộ giấy note mật khẩu dán trên màn hình.
*   **Tools:**
    *   **TheHarvester:** Thu thập email, subdomain từ Google/Bing.
    *   **Maltego:** Vẽ sơ đồ mối quan hệ giữa người, email, công ty.

---

## 4. Lab Thực hành: Credential Harvester (SET)

**Mục tiêu:** Tạo một trang đăng nhập Google giả mạo để lừa lấy mật khẩu.
**Công cụ:** **SET (Social-Engineer Toolkit)** trên Kali Linux.

### **Bước 1: Khởi động SET**
```bash
sudo setoolkit
```

### **Bước 2: Chọn Vector tấn công**
Menu hiện ra, chọn theo thứ tự:
1.  `1) Social-Engineering Attacks`
2.  `2) Website Attack Vectors`
3.  `3) Credential Harvester Attack Method`
4.  `2) Site Cloner` (Clone một trang web thật).

### **Bước 3: Cấu hình**
*   **IP address for the POST back:** Nhập IP máy Kali của bạn (VD: `192.168.1.10`). Đây là nơi mật khẩu sẽ gửi về.
*   **URL to clone:** Nhập trang muốn giả mạo (VD: `https://accounts.google.com/signin`).

### **Bước 4: Gửi link cho nạn nhân**
SET sẽ tạo một Web Server giả.
Gửi link `http://192.168.1.10` cho nạn nhân (trong thực tế, Hacker sẽ dùng kỹ thuật rút gọn link hoặc fake domain để che giấu IP).

### **Bước 5: Chờ đợi**
Khi nạn nhân vào link, thấy giao diện y hệt Google -> Nhập User/Pass -> Bấm Enter.
-> Trên màn hình Kali của bạn sẽ hiện ra:
```
POSSIBLE USERNAME FIELD FOUND: nan_nhan@gmail.com
POSSIBLE PASSWORD FIELD FOUND: mat_khau_bi_lo_roi
```

---

## 5. Phòng thủ (Defense)

1.  **Stop, Look, Think:** Luôn chậm lại một nhịp trước khi click vào link lạ hoặc file đính kèm.
2.  **Verify:** Kiểm tra kỹ địa chỉ Email người gửi (đừng chỉ nhìn tên hiển thị). Gọi điện xác nhận nếu thấy yêu cầu chuyển tiền lạ.
3.  **Không cắm USB lạ:** Tuyệt đối không cắm thiết bị không rõ nguồn gốc vào máy tính.
4.  **Hạn chế chia sẻ:** Đừng post quá nhiều thông tin cá nhân (ngày sinh, tên thú cưng, địa chỉ nhà) lên mạng xã hội -> Hacker dùng để đoán mật khẩu hoặc trả lời câu hỏi bảo mật.
