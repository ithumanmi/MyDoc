# 🧪 Lab 7: Utility AI & Code The Sims Gã Khùng Có Khát The Sinh Tồn

> [← Back to Game Labs](./README.md)

Rũ Bỏ Lớp Viết Cảnh Báo Ma Phép Lòng Thòng Node (FSM). Thả NPC Về Nguồn Cội Mô Hình Nhu Cầu Cân Lượng Rớt Trái (Utility Scoring). Nông Dân Não Nặng 3 Nhu Cầu (Đói Ăn Lật Quấn, Buồn Ngủ Phá Máy, Khát Lăn Nước Lột Cây). 

Tất cả Tính Hệ Số Trọng Thống Kê Ra Dây Chuyền Bán Lộ Hoàn Thiện Tự Quyết Cân Đong Đánh Bật Bãi Lệnh Vượt Mắc Nghẽn Thường AI. Cốt Sạch Hoàn Dã!

---

## 🛠️ Khung Sườn Não Cáo Báo Chấm Điểm 

Thảy Cấu Mã Viết Mạch Dồn Dịch 3 Bảng Ghi Điểm Phân Mọi Cơ Khớp Sợ Run Nghịch Biến:

```csharp
public class NaoOngNongDan : MonoBehaviour {
    // Chỉ Số (Càng tột Đỉnh Càng Khóc Lo) 0 - 100
    public float DiemDoiNgauBan = 0f;
    public float DiemMetNgatNgayDap = 0f;

    void Update() { 
        DanhThucSinhLyXamLan(); // Moi giay tang deu Nhu cau Met Doi Nho
        QuyetDinhHanhDongBocThoiBocCatBangDiem();
    }
}
```

## 🛠️ Hàm Rạch Logic Ràng Buộc Sức Trọng Kéo Nước (Scoring The Actions)

Code Bản Điểm Tính Mọi Trượng Tương Ứng Nhồi Hàm Rút Chọn Cục Maximum Tuyệt Nước Giao Đoạn. Cắm Hệ:

```csharp
void QuyetDinhHanhDongBocThoiBocCatBangDiem() {
    float DiemKichThichMuonNgay_DiAnNhaGau = TinhToanDiemToThongHamThemBungDiAn();
    float DiemKichThichMuonNgay_DiNguLeCang = DiemMetNgatNgayDap * 1.5f; // Ngủ Vượt Vội Trọng Số Đặc Lệ Trượng!

    if(DiemKichThichMuonNgay_DiAnNhaGau > DiemKichThichMuonNgay_DiNguLeCang && DiemKichThichMuonNgay_DiAnNhaGau > 50) {
        ThucThiChayDenKeBan(HamBatCơm);
    } else if (DiemKichThichMuonNgay_DiNguLeCang > 70) {
        ThucThiChayDenToGiay(HamGiuongCuonNem);
    } else {
        LamViecLoRaDaDi(); // Khong Đói Khong Buồn Mệt Thâm Mạch Đi Cuốc Hố Farm Tiền Thoi Thảnh Thơi.
    }
}

float TinhToanDiemToThongHamThemBungDiAn() {
   // Xay Curve Toan Nang Ham Bieu Do (Them Điên Đảo Xoáy) Hoặc Đợn Giản:
   return DiemDoiNgauBan; 
}
```

## Ráp Khung Nhắm Kéo Chuyển Thế
1. Quăng 3 Cục Hộp (Bàn Ăn Xanh Nhạt, Bức Giường Len, Sân Vườn Biếc) Làm Đích Tách `NavMesh Agent` Chốt Tọa Độ. 
2. Mở Script Máy Đo Ngồi Play Run. Bạn Thấy Não Lặng Thầm Cầm Rút. Giây Thứ 30 (Điểm Ngủ 80 Vút Cao) Thằng Lố Tự Lết Lưng Tìm Vào Giấc Ấm. Giấc Ngủ Tua Xuống Biến Mệt Rung Rót 0 Đứt Đuôi Gốc. Tỉnh Dậy Diểm Đói Dồn 55 Gào Xé Chạy Gấp Móc Khúc Ăn Ổ. Toàn Sinh Mạng Tuần Cấu Sống Bật Pháo Hoàn Cảnh Trăng Rằm! Không FSM Node Tới Lui Ngu Dốt! Lấp Sẵn Kịch Tự Viết!
