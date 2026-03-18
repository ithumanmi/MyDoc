# Lab: Thiết Kế Clean Architecture CQRS & Event Sourcing bằng NestJS

> [← Back to Backend Labs](./README.md)

Lập trình viên Trung Cấp Viết Class Thụ Động: `Controller` gọi `Service` gọi `Repository` Ghi Database (Thường SQL DB Postgres).
Với 1 Table Đơn Lẻ. Khi Ống Ghi Gấp Quá Tái 100 User Sửa Dữ Liệu 1 Dòng Cùng Trận -> Lock Cứng Mềm Database -> Tất Cả Các Request Đi Nơi Khác Kêu `GET` Để Xem Cũ Đều Dính Vạ Chậm Văng Tắt Tắc Rụt Bóp Dòng Hồi (Database Contention).

**Command Query Responsibility Segregation (CQRS) Sinh Ra Trạch Không Gian DB 2 Lằn:**
1. Rạch Command Cổng Giao: Cấm Read! Dành Để Xử Lý Dữ Liệu Trọng Yếu Và Tường Chặn Ghi ACID Giao PostgreSQL Nhớ Trưởng.
2. Rạch Query Khung Soi: Điển Mặt Nhanh Rạch Sóng Ra Trục Read Siêu Tốc (Document NoSQL Nhu MongoDB) Bật Tăng 1 Triệu Họng Soi Không Bắn Rớt Cổng Trụ Mùa Màng Tới. Kéo Giao Diệp Bằng Microservices Nhờ Khung RabbitMQ/Kafka.

---

## 🏗️ Nặn Dựng Event Bus (Bộ Trái Tim Bóp Của NestJS/CQRS Thư Viện Sẵn Mảnh)

Trong Mật Ngữ Chuyên NodeJs. Chỉ Sài Rút **NestJS/CQRS Package**.

Thay vì Code Viết Bỏ Lệ `orderService.createOrder(dto)` Trực Tiếp Đè Repostitory Ra Đập.
Mọi Hành Động Viết Phải Hủy Thành Khối Cục: `Command`

```typescript
// command.ts (Ghep Khoi Thon De Nem Vao Bus Dien Vong Toan Tuyến)
export class DatMuaHangCommand {
  constructor(public readonly itemId: string, public readonly userId: string, public readonly so_luong: number) {}
}
```

```typescript
// handler.ts 
import { CommandHandler, ICommandHandler, EventPublisher } from '@nestjs/cqrs';

@CommandHandler(DatMuaHangCommand)
export class TiepDonHoanThanhTuTuHandler implements ICommandHandler<DatMuaHangCommand> {
  constructor(private readonly thung_ket_no_publisher: EventPublisher, private repository: PostgresOrderRepository) {}

  async execute(command: DatMuaHangCommand) {
     // 1. Chỉ Ghi Chuan SQL Toan Chinh POSTGRES DB. Khoong Giai Thich ! 
     const newOrderDb = this.repository.taoMoiDon(command.itemId, command.userId);
     await newOrderDb.save();

     // 2. Kích Nổ Quả Bom Sự Kiện Sang Phía READ DB (Mongodb) Thông Qua Event Bus
     const kichBanEvent = this.thung_ket_no_publisher.mergeObjectContext(newOrderDb);
     kichBanEvent.KichNgoiEventDatThemHang(command.itemId, command.so_luong);
     kichBanEvent.commit(); // Bóp Bay Truyền Nhanh Message Bus Đuổi Rẽ Kêu RabbitMQ !!
  }
}
```

### Hệ Query Nhanh Thốc ReadModel Trả Kế 

Vùng Đón Lệnh Đi Kèm Lại MongoDB (Document Giữ Tốc Cache).

```typescript
import { EventsHandler, IEventHandler } from '@nestjs/cqrs';

@EventsHandler(NhanViecHangMoiDatEvent)
export class XayViecUpdateChoBaoVeMongoHieuHandler implements IEventHandler<NhanViecHangMoiDatEvent> {
  constructor(private mongoReadRepo: MongoDbReadViewOrder) {}

  // Lắng Trống Khi Thằng POSTGRES VỪA BÁN XONG KÍCH LỆNH LÀ MONGODB UPDATED NHẬP GIÁ 
  handle(event: NhanViecHangMoiDatEvent) { 
     // Giao Nhan Va Sua Ganh Luong Cap Nhan Mongodb! View Cho Get ! Dang Cap CQRS ! 
     this.mongoReadRepo.UpdateThongKeCuaUserCapTung(event.userId, event.itemId, event.so_luong_dang_bay_toi);
  }
}
```

## 💯 Kết Cục System Architecture 

1. Controller Dành Quản Hàm Get: `GET /orders/me` Không Chọt Nhầm Cột Chắn Của Tên POSTGRES Đang Khoá Write Lên! Đi Thẳng Lôi File Document Gọn Rẻ Tốc Mượt Mongodb Về Trả Kế (Thời Gian 10ms!).
2. Code Đi Viết Lệnh `POST /order`: Tắt Ngủ Bằng Lửa `CommandBus.execute(new DatMuaHangCommand(...))` Cống Sự Ném Qua Khung Rớt Lệnh 1 Lần PostGres Sạch Không Vấp Mạch Khách Khác Ngắm Trông Cây Bật Khung (Tốc Tác System Giáp Rèn Khung Nét CQRS Rành Tách Biệt Read/Write Vĩ Đại Giao Chấn Microservices Hiện Thại)! Dứt Mệnh Nát Controller Cùi!
