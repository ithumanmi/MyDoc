# 🛠️ Virtual Lab Setup: Hướng dẫn xây dựng phòng Lab an toàn

> [← Back to Network Security](../README.md)

Để luyện tập Security, bạn cần một nơi an toàn để phá hoại.
KHÔNG BAO GIỜ thực hành tấn công trên máy thật hoặc mạng công ty!

---

## 1. Kiến trúc Lab (Mô hình 2 máy ảo)

Chúng ta sẽ dùng **VirtualBox** (miễn phí) để tạo một mạng nội bộ ảo (Internal Network).

*   **Máy Attacker (Kẻ tấn công):** Kali Linux.
    *   IP: `192.168.56.10`
    *   Công cụ: Nmap, Metasploit, Burp Suite, Wireshark.
*   **Máy Victim (Nạn nhân):** Metasploitable 2 (Linux dính đầy lỗ hổng).
    *   IP: `192.168.56.20`
    *   Lỗ hổng: SSH yếu, Website lỗi, Database mở, Backdoor...

---

## 2. Chuẩn bị (Download)

1.  **VirtualBox:** [Download](https://www.virtualbox.org/wiki/Downloads)
2.  **Kali Linux (VirtualBox Image):** [Download](https://www.kali.org/get-kali/#kali-virtual-machines)
    *   *Lưu ý:* Chọn bản Pre-built Virtual Machine (đuôi `.vbox` hoặc `.ova`) cho tiện, đỡ phải cài đặt từ đầu.
3.  **Metasploitable 2:** [Download](https://sourceforge.net/projects/metasploitable/)
    *   Đây là một file Zip chứa ổ cứng ảo (`.vmdk`).

---

## 3. Cài đặt & Cấu hình Mạng (Quan trọng!)

Để đảm bảo an toàn và 2 máy nhìn thấy nhau, chúng ta dùng chế độ mạng **"Host-only Adapter"**.

### **Bước 1: Tạo mạng Host-only trong VirtualBox**
*   Mở VirtualBox -> `File` -> `Tools` -> `Network Manager`.
*   Tạo mới một mạng (thường tên là `vboxnet0`).
*   IP Address: `192.168.56.1` / Subnet Mask: `255.255.255.0`.
*   **Tắt DHCP Server** (Chúng ta sẽ đặt IP tĩnh hoặc để máy ảo tự nhận).

### **Bước 2: Setup máy Kali Linux**
*   Import file `.ova` vừa tải về.
*   Vào `Settings` -> `Network`:
    *   Adapter 1: Chọn **Host-only Adapter** (Chọn `vboxnet0`).
*   Start máy ảo. User/Pass mặc định: `kali` / `kali`.

### **Bước 3: Setup máy Metasploitable 2**
*   Tạo máy ảo mới (New) -> Chọn Type: Linux / Version: Ubuntu (64-bit).
*   Phần Hard Disk: Chọn **"Use an existing virtual hard disk file"** -> Trỏ đến file `.vmdk` của Metasploitable vừa giải nén.
*   Vào `Settings` -> `Network`:
    *   Adapter 1: Chọn **Host-only Adapter** (Chọn `vboxnet0`).
*   Start máy ảo. User/Pass mặc định: `msfadmin` / `msfadmin`.

---

## 4. Kiểm tra kết nối (Ping Test)

### **Trên máy Kali:**
Mở Terminal, gõ:
```bash
ifconfig
# Tìm xem interface eth0 có IP lớp 192.168.56.x chưa.
# Ví dụ: 192.168.56.101
```

### **Trên máy Metasploitable:**
Đăng nhập, gõ `ifconfig`.
Ví dụ IP là: `192.168.56.102`.

### **Ping thử:**
Từ Kali, ping sang Metasploitable:
```bash
ping 192.168.56.102
# Nếu thấy phản hồi (bytes from...) là thành công!
```

---

## 5. Bắt đầu tấn công (Reconnaissance)

Bây giờ bạn đã có một "bao cát" để tập đấm.
Thử dùng Nmap trên Kali để quét xem máy nạn nhân đang mở những cổng nào:

```bash
nmap -sV 192.168.56.102
```
-> Bạn sẽ thấy một danh sách dài dằng dặc các cổng mở (FTP, SSH, Telnet, SMTP, HTTP...). Mỗi cổng là một con đường để xâm nhập!

> **Cảnh báo:** Tuyệt đối không để card mạng ở chế độ **Bridged Adapter** khi dùng Metasploitable, vì hacker ngoài internet có thể tấn công vào máy tính thật của bạn thông qua máy ảo này!
