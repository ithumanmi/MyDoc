# Game Backend (BaaS) & LiveOps: Sống Sót Ảo Dạng 

> [← Back to Programming & Networking](../README.md) | [Home](../../../README.md)

Làm sao để lưu `Gold = 9999` mà Hacker xài Cheat Engine không thể sửa được? Làm sao cập nhật Shop bán hàng dịp Giáng sinh mà không bắt Player tải lại 100MB qua AppStore?

Chào mừng bạn bước khỏi ngai vàng Single-Player. Đây là Kỷ nguyên của **BaaS (Backend as a Service)** và **Server-Authoritative**.

---

## 🗄️ 1. Mảnh Ghép Của Một Game Online Hiện Đại

Game không nhất thiết phải là Real-time Multiplayer (Bắn nhau rầm rầm) mới cần Backend. Một game Nông Trại hay Xếp Hình Match-3 vẫn cần Server để sống.

1.  **Authentication (Đăng nhập):** Định danh người chơi (Device ID ẩn danh, Google, Apple ID).
2.  **Cloud Save (Lưu trữ đám mây):** Xóa game cài lại không mất Level. Chống Hack bằng cách Validate dữ liệu trên mây.
3.  **Economy & Inventory (Túi đồ & Tiền tệ):** Nơi chứa danh sách Đồ Víp. Giao dịch mua bán IAP phải được đối chiếu qua biên lai Server.
4.  **LiveOps (Title Data & Events):** Thay đổi chỉ số Máu của Rồng, Đổi Banner Gacha mà đụng 0 dòng code ở Client.

---

## ⚖️ 2. Top Đầu Các Dịch Vụ BaaS (2026 Edition)

Cho Solo Dev và Indie Studio, đừng dại dột bật NodeJS lót SQL tự code từ đầu.

### 🥉 Firebase (Hàng Phổ Thông)
*   **Điểm mạnh:** Cực kỳ nổi tiếng, đồ nhà Google. Push Notifications vô địch. Firestore (NoSQL) rẽ nhánh dữ liệu sướng.
*   **Điểm yếu:** Nó làm ra cho Web/Mobile App. Quản lý hệ thống tiền tệ game rất mệt mỏi. Không có các cấu trúc Game cơ bản (Inventory, Matchmaking).

### 🥈 Nakama (Heroic Labs) (Ngự Quân Open-Source)
*   **Điểm mạnh:** Dedicated Game Server đích thực. Mã nguồn mở 100%. Viết script logic server bằng Lua, JavaScript, Go. Hỗ trợ Real-time Multiplayer siêu xịn.
*   **Điểm yếu:** Không có nền tảng Cloud xài ngay miễn phí. Phải tự thuê VPS Linux dựng Docker Nakama lên. Hơi chua vụ DevOps.

### 🥇 PlayFab (Microsoft) (Trùm Cuối Của Game Indie)
*   **Điểm mạnh:** Chuyên biệt 100% cho Game. Có mọi thứ: Login, Cloud Script, Leaderboard, Matchmaking, Title Data, In-App-Purchase Receipt. Free tới 100k User (Đủ thành tỉ phú). Documentation SDK Unity chuẩn chỉnh.
*   **Trái Tim Của Kiến Trúc Cứng:** Ngay khi đăng nhập, Client Nhận Ticket. Mọi API gọi lên lấy vàng/thay đồ đều bắn kèm Ticket định danh.

---

## 🛡️ 3. Thiết Kế (Server-Authoritative Save) Chống Hack

Cheat Engine hoạt động bằng cách quét bộ nhớ RAM máy tính. Thấy số Lượng Vàng = 50. Đổi 50 thành 90000. 

### Quy Trình Kẻ Lười (Client-Authoritative -> Dễ Bị Hack):
1. User đánh lụm được Rìu. Hệ thống Unity (Client) gọi API: `PlayFab.Cập_Nhật_Kho_Đồ(Rìu)`.
2. Hacker sửa gói tin giữa đường thành: `PlayFab.Cập_Nhật_Kho_Đồ(10.000_Vàng)`. Server gật đầu cái rụp. Game Nát!

### Quy Trình Chuẩn (Server-Authoritative -> Kiên Cố):
1.  Hệ thống Unity gọi API: `PlayFab.Hành_Động(Mở_Rương_Số_5)`. KHÔNG CHỨA Tham số Đồ Vật bên trong gửi đi!
2.  Cloud Script (Chạy ẩn trên Server PlayFab bằng Javascript C#) bóc gói tin ra. Kiểm chứng ID thằng này có chía khóa Rương 5 Không? Nếu có. Random hàm ở Server thả ra Món Đồ. Chỉnh Sửa Trực Tiếp Kho Đồ Của Thằng Kia Dưới DataCenter.
3.  Server Trả ngược Về Client Chuỗi JSON: `Kết_Quả: "Mày Nhận Được Rìu"`. 
4.  Client chiếu Ui hình cái rìu bay hờ hững. Hack bằng Mắt!

> 🧪 **Chuyển sang Hành Động:** Đã đến lúc vứt bỏ `PlayerPrefs` và thực hành [Lab: Tích Hợp PlayFab Leaderboard](../../labs/lab-baas-leaderboard.md) với SDK C#.
