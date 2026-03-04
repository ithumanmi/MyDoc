---
title: "Design Patterns Playbook"
description: "Map tư duy, nhóm pattern cơ bản đến nâng cao, và cách áp dụng vào dự án web/backend thực tế."
last_updated: 2026-03-04
---

# ♟️ Design Patterns Playbook cho Developer hiện đại

> Design Pattern không phải là “thuộc lòng 23 mẫu GoF”, mà là từ điển giúp bạn chọn đúng cấu trúc cho vấn đề. Bài này giúp bạn ghi nhớ nhanh và áp dụng được ngay trong dự án web/backend.

---

## 0. Bản đồ tư duy

| Nhóm | Pattern | Khi dùng |
| --- | --- | --- |
| **Creational** | Factory, Abstract Factory, Builder, Prototype, Singleton | Quản lý cách khởi tạo object, đảm bảo thống nhất config |
| **Structural** | Adapter, Facade, Composite, Decorator, Proxy, Flyweight, Bridge | Bọc, kết hợp hoặc mở rộng object mà không sửa code gốc |
| **Behavioral** | Strategy, Observer, Command, Chain of Responsibility, State, Mediator, Visitor, Template Method | Tổ chức luồng behavior/phản ứng giữa các object |

> 🔑 Nguyên tắc: Pattern chỉ nên xuất hiện khi **đau đủ lớn**. Đừng ép mọi thứ thành pattern.

---

## 1. Creational Patterns áp dụng nhanh

### Factory / Abstract Factory

- **Use case:** Chọn implementation dựa trên config runtime (Payment, Notification).
- **Example:**

```ts
interface PaymentGateway { charge(amount: number): Promise<void>; }

class StripeGateway implements PaymentGateway { /* ... */ }
class MoMoGateway implements PaymentGateway { /* ... */ }

class PaymentFactory {
  static create(provider: string): PaymentGateway {
    switch (provider) {
      case 'stripe': return new StripeGateway();
      case 'momo': return new MoMoGateway();
      default: throw new Error('Unsupported');
    }
  }
}
```

### Builder

- **Giải quyết:** Object có nhiều optional param (ví dụ query phức tạp, email template).
- Dùng Fluent API để chain config.

### Singleton

- Chỉ dùng khi resource thực sự duy nhất (ConfigService). Với framework hỗ trợ DI, ưu tiên DI container hơn singleton thủ công.

---

## 2. Structural Patterns cho web service

| Pattern | Vấn đề giải quyết | Ví dụ thực tế |
| --- | --- | --- |
| **Adapter** | Interface cũ vs thư viện mới | Bọc thư viện SMS khác nhau thành interface chung |
| **Facade** | API phức tạp → interface đơn giản | Service gom nhiều microservice call |
| **Decorator** | Thêm behavior mà không chạm class gốc | Thêm caching/logging cho repository |
| **Composite** | Cấu trúc cây, xử lý như một | Menu đa cấp, scene graph |
| **Proxy** | Điều khiển truy cập, lazy load | Rate limit, auth trước khi gọi service |

### Decorator Example (TypeScript)

```ts
interface ReportGenerator { generate(data: ReportData): string; }

class PdfReport implements ReportGenerator {
  generate(data: ReportData) { /* render pdf */ return 'pdf'; }
}

class CachedReport implements ReportGenerator {
  constructor(private inner: ReportGenerator, private cache: CacheService) {}
  generate(data: ReportData) {
    const key = hash(data);
    if (this.cache.has(key)) return this.cache.get(key);
    const result = this.inner.generate(data);
    this.cache.set(key, result);
    return result;
  }
}
```

---

## 3. Behavioral Patterns – “não bộ” của hệ thống

### Strategy

- Tránh `switch-case` khổng lồ cho logic lựa chọn.
- Ví dụ: chiến lược pricing, thuật toán sort, AI behavior.

### Observer

- Publish/Subscribe event, tối ưu cho UI hoặc domain events.
- Web: WebSocket event bus, frontend state management.

### Command

- Đóng gói hành động + dữ liệu, hỗ trợ log/undo/retry.
- Ví dụ: xử lý queue (email, webhook), macro editor.

### Chain of Responsibility

- Pipeline xử lý validation, middleware, hoặc rule engine.
- Ví dụ:

```ts
abstract class Handler {
  protected next?: Handler;
  setNext(next: Handler) { this.next = next; return next; }
  handle(req: Request) { return this.next?.handle(req); }
}

class AuthHandler extends Handler {
  handle(req: Request) {
    if (!req.user) throw new Error('Unauthorized');
    return super.handle(req);
  }
}
```

### State

- Mỗi trạng thái là object riêng: tránh `if(status === 'pending')` khắp nơi.
- Dùng cho order lifecycle, workflow engine, UI wizard.

---

## 4. Kết hợp pattern với architecture hiện đại

| Bối cảnh | Pattern gợi ý | Lưu ý |
| --- | --- | --- |
| **Microservice** | Facade, Circuit Breaker, Saga | Xem thêm microservices-patterns.md |
| **DDD** | Factory, Aggregate, Domain Event (Observer), Repository | Pattern luôn bám domain |
| **Frontend SPA** | Strategy (theme), Observer (state), Command (undo), Mediator (component bus) | Kết hợp với framework hook/store |
| **Event-driven** | Observer, CQRS + Event Sourcing | Event log = Command history |

---

## 5. Checklist chọn pattern

- [ ] Đã xác định rõ “đau” (code smell) chưa?
- [ ] Pattern giúp giảm duplication & coupling?
- [ ] Có làm khó test hơn không?
- [ ] Tên pattern hiểu được trong team?
- [ ] Có ADR/diagram ghi lại quyết định?

> ❗ Pattern không thay thế kiến trúc: nó chỉ là công cụ để diễn đạt giải pháp.

---

## 6. Tài nguyên học nhanh

- **Refactoring.Guru** – visual hóa mọi pattern.
- **Game Programming Patterns (Robert Nystrom)** – pattern qua lăng kính game (dễ hiểu).
- **Head First Design Patterns** – bản GoF nhưng hình ảnh, dễ đọc.
- **Clean Architecture** – hướng dẫn dùng pattern để bảo vệ domain.

---

## 7. Bài tập vận dụng

1. Refactor module Payment để dùng Strategy + Factory.
2. Viết decorator thêm caching cho service đọc DB.
3. Thiết kế pipeline middleware bằng Chain of Responsibility.
4. Document một ADR mô tả vì sao chọn pattern X cho feature Y.
5. Tạo demo repo: mỗi pattern một folder, có README giải thích khi dùng.

> 🎯 Sau khi luyện, mục tiêu là bạn có thể **nhận diện smell → chọn pattern → triển khai → giải thích** cho teammate trong code review.

---

**Next Steps:**

- Tạo wiki nội bộ ghi lại các pattern đã áp dụng trong công ty.
- Đưa checklist pattern vào template kiến trúc/ADR để chuẩn hóa.

**Remember:** Pattern là ngôn ngữ chung giúp team trao đổi nhanh chóng—khi ai đó nói “dùng Strategy ở đây”, mọi người hiểu ngay cấu trúc bạn định làm.