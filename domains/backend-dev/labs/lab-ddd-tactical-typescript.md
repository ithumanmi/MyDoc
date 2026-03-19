# Lab: Tactical DDD với TypeScript

> [← Quay lại Backend Labs](./README.md)

Mục tiêu: tách logic nghiệp vụ khỏi framework/ORM, mô hình hóa domain bằng Value Object và Aggregate Root để hạn chế bug và phụ thuộc hạ tầng.

---

## 💎 Value Object: bất biến, tự kiểm soát tính hợp lệ

Tránh dùng primitive (string) cho dữ liệu có quy tắc riêng. Gói vào Value Object để kiểm tra ngay khi tạo và so sánh theo giá trị.

```typescript
// src/domain/value-objects/Email.ts

export class Email {
  private constructor(public readonly value: string) {}

  static create(raw: string): Email {
    if (!raw) throw new Error("Email không được để trống");
    if (!raw.includes("@")) throw new Error("Email không hợp lệ");
    return new Email(raw);
  }

  equals(other: Email): boolean {
    return this.value === other.value;
  }
}
```

---

## 🏰 Aggregate Root: gom logic nghiệp vụ, bảo vệ bất biến

Aggregate giữ trạng thái nhất quán và phơi bày hành vi (method), không để controller/service thao tác trực tiếp field tùy ý.

```typescript
// src/domain/aggregates/DatHangKhachHang.ts

import { Email } from '../value-objects/Email';

export enum TinhTrangKhach {
  CHO_CAP_PHEP = "PENDING_TRIAL",
  THANH_VIP = "VIP_VERIFIED",
  BI_BAN = "BANNED_LOCK",
}

export class KhachHangAggregate {
  private constructor(
    public readonly id: string,
    private ten: string,
    private email: Email,
    private trangThai: TinhTrangKhach,
  ) {}

  static dangKyMoi(id: string, ten: string, emailRaw: string): KhachHangAggregate {
    const email = Email.create(emailRaw);
    return new KhachHangAggregate(id, ten, email, TinhTrangKhach.CHO_CAP_PHEP);
  }

  nangVIP() {
    if (this.trangThai === TinhTrangKhach.BI_BAN) {
      throw new Error("Khách hàng bị khóa, không thể nâng VIP");
    }
    this.trangThai = TinhTrangKhach.THANH_VIP;
    // Phát domain event nếu cần
  }
}
```

## 🏆 Lợi ích

- Domain không phụ thuộc ORM/framework; code thuần TypeScript.
- Quy tắc nghiệp vụ tập trung trong domain, giảm bug do thao tác trực tiếp DB.
- Dễ di chuyển giữa framework/DB: giữ nguyên thư mục `src/domain`, chỉ thay adapter/infrastructure.
