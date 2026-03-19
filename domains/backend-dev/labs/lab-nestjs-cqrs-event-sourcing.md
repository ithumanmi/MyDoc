# Lab: Thiết kế CQRS & Event Sourcing bằng NestJS

> [← Quay lại Backend Labs](./README.md)

Mục tiêu: tách luồng đọc/ghi để tránh contention, dùng event bus đẩy dữ liệu sang store đọc riêng, áp dụng thư viện `@nestjs/cqrs`.

---

## 🧭 Vấn đề

Kiến trúc CRUD đi thẳng DB khiến luồng ghi có thể khóa bảng và làm chậm luồng đọc. CQRS tách biệt:

1. **Command**: xử lý ghi, đảm bảo ACID (Postgres/MySQL).
2. **Query**: phục vụ đọc nhanh, có thể dùng NoSQL (MongoDB/Elastic) và được cập nhật qua event.

---

## 🏗️ Thiết lập command & handler

Khai báo command:

```typescript
// command.ts
export class DatMuaHangCommand {
  constructor(
    public readonly itemId: string,
    public readonly userId: string,
    public readonly soLuong: number,
  ) {}
}
```

Handler ghi vào DB và phát sự kiện:

```typescript
// handler.ts
import { CommandHandler, ICommandHandler, EventPublisher } from '@nestjs/cqrs';

@CommandHandler(DatMuaHangCommand)
export class DatMuaHangHandler implements ICommandHandler<DatMuaHangCommand> {
  constructor(
    private readonly publisher: EventPublisher,
    private readonly repo: PostgresOrderRepository,
  ) {}

  async execute(command: DatMuaHangCommand) {
    const order = this.repo.taoMoiDon(command.itemId, command.userId, command.soLuong);
    await order.save();

    const aggregate = this.publisher.mergeObjectContext(order);
    aggregate.datHangThanhCong(command.itemId, command.soLuong);
    aggregate.commit(); // phát event ra bus (RabbitMQ/Kafka)
  }
}
```

---

## 🔍 Xử lý event để cập nhật read model

Lắng nghe event và cập nhật view MongoDB:

```typescript
import { EventsHandler, IEventHandler } from '@nestjs/cqrs';

@EventsHandler(NhanViecHangMoiDatEvent)
export class CapNhatViewDonHangHandler implements IEventHandler<NhanViecHangMoiDatEvent> {
  constructor(private readonly mongoReadRepo: MongoDbReadViewOrder) {}

  handle(event: NhanViecHangMoiDatEvent) {
    this.mongoReadRepo.updateUserOrderStats(event.userId, event.itemId, event.soLuong);
  }
}
```

---

## 🧾 Kết quả kiến trúc

1. `GET /orders/me` đọc từ MongoDB/Elastic, không bị ảnh hưởng bởi lock ghi trên Postgres.
2. `POST /order` gọi `CommandBus.execute(new DatMuaHangCommand(...))`; ghi vào Postgres và phát event để đồng bộ view đọc. Luồng đọc/ghi tách biệt, hệ thống chịu tải tốt hơn và dễ mở rộng.
