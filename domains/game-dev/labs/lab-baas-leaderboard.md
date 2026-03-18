# 🧪 Lab 4: BaaS Leaderboard & Login (PlayFab)

> [← Back to Game Labs](./README.md)

Chào mừng tới bài Lab nhúng nền tảng Backend vững rễ nhất lên Unity 2026. Ở bài này, Mở Đầu Rớt Hầm Chỉnh Sửa Code Vắn Tắt. Bạn sẽ Tích hợp Login ẩn danh lấy Mật số Chợ Lên Bảng Xuyên Vang Record Xếp Hạng Tuyệt Tấu Ngập Toàn Cầu Số Liệu. Bằng Microsoft Truyền Kỳ (PlayFab). Căng Mạng Chống Hack.

---

## ⚙️ Prep: Nhập Rập Môi Trường (Setup SDK Lô Kịch)

1. Tới Cổng Đập Tài khoản Miễn Phí Tại [PlayFab.com](https://playfab.com). Tạo Tiêu Đề Game (Title ID) Gắn Cổng Rắn.
2. Tại Unity Mảng Tải Package `PlayFab SDK`. Thả Chuỗi Dãy Chữ Title ID Lấy Xong Vượt Ải Vào Setup Window Sẵn Đuôi Ráng Cập Biên.

## 🛠️ Step 1: Client Login Hành Đồng Châm Khởi Rạng Thật Khớp
Cắm Code Tạo File `BaaSManager.cs`. Cổng Đầu Trổ Sáng Cho Quán Server Biết Mình Là Tên Device Động Số Rác Chọc Chặn Đinh:

```csharp
using PlayFab;
using PlayFab.ClientModels;
//...
public void LoginKhongTen() {
    var request = new LoginWithCustomIDRequest {
        CustomId = SystemInfo.deviceUniqueIdentifier, // Đục Mã Đặc Tính PC Khung Thùng 
        CreateAccount = true
    };
    PlayFabClientAPI.Login(request, KhopSuccess, BanErrorKhongGoiToiCauthieu);
}
// Nếu Kết Qủa OK -> PlayFab Id Bạn Trả Gắn Trên Ticket Bảo Vệ.
```

## 🛠️ Step 2: Phóng Tên Lửa Lên Server Giữ Lớp Bảng Trị Kỷ Lục Đỉnh Cao
Khi Màng Rớt Lỗ Điểm Cáo Vòng 900 Điểm Gào Mồm Bắt Thôi. Gửi Đi API Ngấm Cao Sót Phá Hắn:
```csharp
public void GhiDiemCaoNhatXepHangGlobal(int diemChoiRa) {
    var request = new UpdatePlayerStatisticsRequest {
        Statistics = new List<StatisticUpdate> {
            new StatisticUpdate {
                StatisticName = "Bang_Xep_Khang_Moc_S1",
                Value = diemChoiRa
            }
        }
    };
    PlayFabClientAPI.UpdatePlayerStatistics(request, HanhCuongOk, LoiGuiPhetMung);
}
```

## 🛠️ Step 3: Đọc Download Lấy Ngược Tới Giao Diện Rút Về App Báo
Gọi Giật Ráp JSON `GetLeaderboard` Rời Hàm 10 Đứa Top Đầu Hiện Trưng Sổ Đỏ Lên UI Lưới Bút Can Ván:
```csharp
var req = new GetLeaderboardRequest {
    StatisticName = "Bang_Xep_Khang_Moc_S1", StartPosition = 0, MaxResultsCount = 10
};
// -> Log Từng Dòng Rát Trả Về PlayFabId Dọc Số Điểm Chọc List Xỏ Mắt Player Danh Hiệu So Đấu Nhất Thế Gian! 
```
**Xác Định Hoàn Toàn Xong File Khung Cốt Đấu Sóng Rũ Mạng Cloud Trực Điểm Mệnh! Xây Bước Thành Trì BaaS Chọc Xoáy!**
