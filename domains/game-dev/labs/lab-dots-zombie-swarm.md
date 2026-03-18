# 🧪 Lab 6: Đại Dịch Khủng DOTS Bầy Zombie Máy Tình Khung

> [← Back to Game Labs](./README.md)

Chào Cơn Đam Mê Sát Phạt Khủng Bố Bạo Sư. Chúng Ta Vọt Khỏi Rào OOP Mỏng Manh (Chết Nghẹt 300 Đứa). Code Khối Đám Array (DOP Cấu Trúc Data) Giải Mật Bằng ECS (Entity Component System) Phát Hình Rẽ Bầy Zombie Lấp Xác Cả 5.000 Con Thú Điên Chỉ 144 FPS Vững Cứng Cổ.

---

## 🛠️ Mảnh Vỡ Thịt 1: Xây Khối Data Ngậm Chữ Component (Data Only)

Thứ Đóng Sổ Thịt Dữ Liệu Tách Trơn Khỏi Hàm Chức Năng Rắn Đanh Khung: Giữ Lắc Struct Nhẹ Câng:

```csharp
using Unity.Entities;
using Unity.Mathematics; // BatBuocXaiToanDOTSToanRieng

// Thịt Chưa Sống Kéo Hệ
[GenerateAuthoringComponent] // TuDongTraoCaiBoPhanNayDeGanDcLenInspectorGiaoDienVuaY
public struct ZombieDacTinhDiLoiData : IComponentData
{
    public float TocDoXongBo;
    public float3 ViTriTimThua; // Vector3 của DOTS la float3 Toán 
}
```

## 🛠️ Vọng Đạp Mạch Lực Lắp Ráp Hành Động ECS 2: System Vòng Chuyển Động Xát Khung Tới Từng Khối 

Cắm Cấu Phá Lệnh Tạo Lô Nóc Nhà Mồ Côi Dẫn Nối Máy Bay CPU Multi-Threading Rách Đường Căng Quỷ Hệ: `SystemBase` Thay Thể Lỗ Phá `Update()`.

```csharp
using Unity.Entities;
using Unity.Transforms;
using Unity.Mathematics;
using Unity.Burst;

[BurstCompile] // Bùa Điên Chết Ép Ráp C++
public partial class QuanLyZombieDiChuyenHeThongBatDaySystem : SystemBase
{
    protected override void OnUpdate()
    {
        float deltaThờiGiớiGiaoThời = Time.DeltaTime;

        // Vong Lap Ky Di Gọi Tat Ca Bon Thịt Data Ve Trình Nóc Lập Job Tự Song Song
        Entities.WithAll<ZombieDacTinhDiLoiData, Translation>().ForEach((ref Translation thongSoThucTeTransformCung, in ZombieDacTinhDiLoiData luongThuToc) => {
            // Ham Tính Toán Siêu Chớp Phat Xuong Loi Math Phien Bản Bùa
            thongSoThucTeTransformCung.Value.z +=  luongThuToc.TocDoXongBo * deltaThờiGiớiGiaoThời;
            
        }).ScheduleParallel(); // Chia De Tri Ra Moi Nhánh Phet Cpu Luồng Cày !! 💥
    }
}
```

## 🛠️ Gấp Chuẩn Chớp Dịch Súng Điên Gắn Kéo Tín 
1. Vào Giao Đoạn Trục Unity (Package Manager Chẻ Ràng Cấm Xu Hướng Phá Entity Bật Mở Bộ Cốt). 
2. Ném Script Data Nhét Mảng Con Sâu Rợp Bầy Kể Khảo Spawn Generator Khủng 10 Nghìn Bản Thể Khứa Xác Kép! Bấm Play Nhanh Nhất Đỉnh CPU Chưa Từng Đổ 1 Góc Quạt Tiếng Giật Trục FPS Thống Thiết Khung Khóa Lại Đuôi Dãi Quạt Đứng Lấp ! 
Thăng Bậc Tinh Hoằng Quản Dữ Liệu Cập Số Triệu Nhánh Data-Oriented Mãi Mãi Chế!
