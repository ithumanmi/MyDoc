# 🛡️ Blue Team Lab: Linux Firewall (UFW)

> [← Back to Network Security](../README.md)

"Default Deny" là nguyên tắc vàng. Chặn tất cả, chỉ mở cái cần thiết.
Hôm nay chúng ta sẽ biến Server Linux của bạn thành một pháo đài với **UFW (Uncomplicated Firewall)**.

---

## 1. Chuẩn bị

Bạn cần một máy Linux (Ubuntu/Debian) hoặc máy ảo.
Kiểm tra trạng thái UFW:
```bash
sudo ufw status
# Output: Status: inactive (Chưa chạy)
```

---

## 2. Lab thực hành (Hardening)

### **Bước 1: Thiết lập chính sách mặc định (Default Policy)**
Luôn luôn chặn kết nối ĐẾN (Incoming) và cho phép kết nối RA (Outgoing).

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
```
-> Lúc này Server của bạn "im lặng" hoàn toàn với thế giới bên ngoài.

### **Bước 2: Mở cửa SSH (Quan trọng!)**
Nếu bạn đang remote qua SSH mà bật Firewall luôn thì sẽ bị **MẤT KẾT NỐI VĨNH VIỄN**.
Phải mở port SSH trước.

```bash
# Cách 1: Mở port mặc định 22
sudo ufw allow ssh

# Cách 2: Mở port custom (Ví dụ bạn đổi SSH sang 2222 để tránh scan)
sudo ufw allow 2222/tcp
```

### **Bước 3: Mở cửa Web Server (HTTP/HTTPS)**
Nếu server chạy web (Nginx/Apache), cần mở port 80 và 443.

```bash
sudo ufw allow http  # Port 80
sudo ufw allow https # Port 443
```

### **Bước 4: Chống Brute-force SSH (Rate Limiting)**
Hacker thường dùng tool dò mật khẩu SSH liên tục.
UFW có tính năng **Limit**: Nếu 1 IP kết nối sai quá 6 lần trong 30s -> Chặn IP đó.

```bash
sudo ufw limit ssh
```

### **Bước 5: Kích hoạt Firewall**
Sau khi cấu hình xong, bật nó lên.

```bash
sudo ufw enable
# Nhấn 'y' để xác nhận.
```

Kiểm tra lại:
```bash
sudo ufw status verbose
```

---

## 3. Quản lý nâng cao

### **Chặn IP cụ thể (Blacklist)**
Nếu thấy IP `1.2.3.4` đang tấn công bạn:
```bash
sudo ufw deny from 1.2.3.4
```

### **Chỉ cho phép IP cụ thể (Whitelist)**
Chỉ cho phép máy tính ở nhà bạn (IP `192.168.1.10`) truy cập SSH:
```bash
sudo ufw allow from 192.168.1.10 to any port 22
```

### **Xóa Rule**
Nếu lỡ tay mở port sai:
```bash
sudo ufw status numbered
# Tìm số thứ tự của rule muốn xóa (Ví dụ số 2)
sudo ufw delete 2
```

---

## 4. Kiểm tra (Verification)

Dùng máy khác (hoặc máy hacker) để scan thử server xem port nào đang mở.
Công cụ: **Nmap**.

```bash
nmap -p 1-65535 <IP_SERVER>
```
-> Kết quả chỉ nên thấy port 22, 80, 443 là `OPEN`. Các port khác phải là `FILTERED` (Bị Firewall chặn).

> **Ghi nhớ:** Firewall là lớp bảo vệ đầu tiên. Đừng bao giờ tắt nó trên Production!
