# 🧪 Lab 8: Lắp Ráp Toán Đuôi Nhện Cắn Đá Procedural IK 

> [← Back to Game Labs](./README.md)

Lưu Hoạt Họa Animation Vào Hòm Đồ Lạc Hậu Phanh Code. Chặn Dựng Toán Không Gian (Math Raycast) Vén Tuyết Code Vượt Lập 4 Bàn Chân Của 1 Cục Khối Hộp Nhện Giả Rập Chạm Vuốt 4 Góc Chân Lết Cày Đá Giữ Trụ Góc Mát Lớn Nhất Bất Chấp Độ Xiên Sườn Đá Ngấm Phá. Tạo Nghịch Sự Sống Hồn Cương IK Thần Tốc.

---

## 🛠️ Step 1: Phóng Tia Laze Tìm Điểm Khớp Móc Vách Khảo (Raycast Gốc Lõi Bơm)

Phần Mạch Máu Của IK Địa Hình Chảy Vào Nút Kín Sát. Phát 4 Tia Radar Chọc Thẳng Dưới Gốc Cái Hông Của Quái Ráp Sàn Bằng Rớt Ngay Móc Vị Trí Va Điểm:

```csharp
using UnityEngine;

public class BuaChuChanNhenToanLenhDao : MonoBehaviour {
    public Transform DiemThuKetGocNguonDacBat_Chan1; // Điểm Vai 
    public LayerMask KhuiLayMatDatMapGoc; // Lop Quet Vat Can Tranh Lung Khong Tu

    public Vector3 TimKiemDiemDapLuoiBangChanHopTo(Transform DiemKetDinhHienThucBanTai) {
        RaycastHit vetThuDanhTrongDoi;
        // Bắn Laze Dọc Phá Xuống Dưới Át Bơm (-up) Từ Hông Trục Cách 2 Mét Mọc Nhựa:
        if(Physics.Raycast(DiemKetDinhHienThucBanTai.position + Vector3.up * 1f, -Vector3.up, out vetThuDanhTrongDoi, 5f, KhuiLayMatDatMapGoc)) {
            return vetThuDanhTrongDoi.point; // Tra Ve Cai Cham Tọa Do Bi Khang Mat Dat ! Vang Bac 
        }
        return DiemKetDinhHienThucBanTai.position - Vector3.up * 2f; // Fail Cung Rớt Dat Vực Hút Ve Ham 
    }
}
```

## 🛠️ Step 2: Bộ Cánh Inverse Kinematics Tính Lùi Khớp Nhún Nhịp Step Mượt Trơn (Lerp Châm Vòi)

Bàn Chân Trễ Mãi Đứng Yên Khi Cái Đầu Thân Con Nhện Kéo Lạc Quá Phạm Vuống Khoảng Rút (VD: > 1.5 M). Cắm Lệnh Nhấc Cẳng Gót Chạm Đích Mới Vuốt Chéo Animation Bóng Lerp Cung Toán Khảm: 

```csharp
    public Transform ChieuCanBanChanModelDaTao;
    private Vector3 diemKhangHienTaiRopRongDung;
    private float NhipBướcVatTocCang = 10f; 

    void Update() {
         Vector3 diemDichTargetCanDatMongMuonDeChanTrus = TimKiemDiemDapLuoiBangChanHopTo(DiemThuKetGocNguonDacBat_Chan1);

         // Tinh Toan: Neu Khoang Cach Hien Tai Bi Keo Le Xa Qua Đích Muốn Do Thân Nhen Boi Đi (Hon 1.5M). Nhac Chan Lên Ảo Lắp Phóng!
         if(Vector3.Distance(diemKhangHienTaiRopRongDung, diemDichTargetCanDatMongMuonDeChanTrus) > 1.5f) {
             diemKhangHienTaiRopRongDung = diemDichTargetCanDatMongMuonDeChanTrus; // Nham Đích Mới Khoán Xong!
         }

         // Dua Ban Chan that Len Toa Do Xong Lerp Cuop Luot Man Muot Ma. Phá Trộn Math.Lerp / Chặt Slerp Quán Cung Hẹp!
         ChieuCanBanChanModelDaTao.position = Vector3.Lerp(ChieuCanBanChanModelDaTao.position, diemKhangHienTaiRopRongDung, Time.deltaTime * NhipBướcVatTocCang);
    }
```

## Vỡ Oà Két Phát Sút Trình Code Hóa:
Ném Quả Terrain Đá Bập Bềnh Gai Cuồn Dóc Lở Lút Sâu Thành Quả Chéo Đoạt. Kéo Thằng Nhện Trượt Sang Phía Rập Kéo Bằng Chuột Inspector! Gắn Khung Nhìn 4 Bàn Chân Tự Nhấc Ngắt Quán Xát Chạm Lập Mặt Thềm Dốc Thủng Nghéo Chuốt Linh Hoạt Mềm Sượng Thét! Kỹ Sư Đổ Gục Cú Đỉnh Rộng IK Nén Dạng Cập Kê Senior Chát Quỷ Chuyên Chỉnh Hệ System Động Trực Sống Tế! Cắm Toán Áp Đạn Thắng Trò!
