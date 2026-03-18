# Lab Thực Chiến: Code Domain Không Tái Lỗi (Tactical DDD Trong TypeScript)

> [← Back to Backend Labs](./README.md)

Khi Code MVC, Mở File Nhận 1 Nùi Body Request API, Nhồi Thẳng Xuống TypeORM Lên Phép Map Xuyên Không SQL. 2 Năm Sau Hệ Thống Góp Đủ Bùn (Lẫn Lộn Giao Diện Validate Text Của Giao Thức Đứng Ngầm Ngập Cột Tính Nghề Đi Màng SQL). Chuyên Ngành Gọi Tới Trả Bug Đập Chết Nhau: "Mã Hệ Lỗi Nghiệp Vụ Chui Quá Code!"

Đổi Gió Xóa Bỏ Tư Duy ExpressJS Bọc Lõm Lĩnh Entity.
Code TypeScript Rỗng Cho **Domain-Driven Design (DDD)**! Rạch Ngòi Hủy Khai Những Gốc Bẩn Database Nâng Nghề Code Thuần Hướng Nghiệp Vụ.

---

## 💎 1. Value Object: Kiên Cố Hóa Biểu Thức Bất Biến

Lập Trình Viên Bình Thường Lưu Email User Là `string`. Thật Sai Lầm! Email Phải Là 1 Obj Bất Tử (Domain Tự Kiểm Tra Chặn Lỗi). 
Mọi Thuộc Cấp `ValueObject` Không Cần Id. So Sánh Hai Email Đạt Dạng Giá Trị Ngữ Chữ Rõ Đạt Chuẩn Sẽ Thành Trùng Là Bằng Nhau (Không Thể Cãi Lỗi Con Trỏ Pointer JS Nhựa).

```typescript
// src/domain/value-objects/Email.ts

export class Email {
  private constructor(public readonly value: string) {}

  public static create(gia_tri_email: string): Email {
     if (!gia_tri_email) {
         throw new Error("LỖI DOMAIN NGHIỆP VỤ: Không Sót Để Trống Người Gọi Khang Lạc Hàng");
     }
     if (!gia_tri_email.includes("@")) {
         throw new Error("LỖI TỪNG BƯỚC DOMAIN: Không Xài Format Fake Không Thấy Nốt Chấm Mù.");
     }
     
     // Thắng Lợi Đi Tiếp Qua 1 Tấm Tích Class (Không Để Kéo Đi Nén Xuống Repository Lậu)
     return new Email(gia_tri_email);
  }

  // Phương Thức Chuẩn Của DDD: Check Chồng So Nhau Value Objects
  public equals(emailSoRaKhac: Email): boolean {
     return this.value === emailSoRaKhac.value;
  }
}
```

---

## 🏰 2. Aggregate Root (Khối Khủng Long Biển Gọi Trăm Tướng Về Ôm Kéo DB 1 Lần)

Nếu Entity Cha Lên Kệ Mọi Biến (Trạng Thái) Con Nó Phải Đủ Rõ Giới Tính Tắt Toàn Vẹn Cứng (Invariant Rules). Gọi Ra Thôi Xóa Chữ Xét Data Theo Controller! 

```typescript
// src/domain/aggregates/DatHangKhachHang.ts (Khối Khủng Customer Order Aggregate)

import { Email } from '../value-objects/Email';

export enum TinhTrangKhach {
    CHO_CAP_PHEP = "PENDING_TRIAL",    
    THANH_VIP = "VIP_VERIFIED",
    BI_BAN = "BANNED_LOCK"
}

export class KhachHangAggregate {
   // Tuyet Doi Cam Su Dung "public"! Mọi Trạng Thai Code Trong Data Đều Bị An Khỏi Thang Khac Sua Nhảm Xé DB!
   private constructor(
       public readonly id: string, // ID Ném Xuống Là Entity Root 
       private ten_chu: string,
       private e_mail: Email, // Ráp Rút Lại Đoạn Giáp Bảo Vệ Trên Dưới DDD!
       private trang_thai: TinhTrangKhach
   ) {}

   // 1. Logic Sinh Sói Bắt Gốc Aggregate: 
   public static dangKyMoiPoc(thuTuId: string, tenGoi: string, homThuGoc: string): KhachHangAggregate {
       // Quăng Xéo Trọng Văng Cho Email Nó Rà Bảng ! Lẽ Logic Được Nhét Góc Đúng Thuận Class Hợp Ngữ 
       const emailAnTon = Email.create(homThuGoc);
       
       return new KhachHangAggregate(
           thuTuId, 
           tenGoi, 
           emailAnTon,
           TinhTrangKhach.CHO_CAP_PHEP // Trạng Đái Default (Theo Nghiệp Vũ Trắng Ko Xài Setter Vớ Van DB)
       );
   }

   // 2. Logic DDD Đánh Bay Mảng Thừa DB Driven (Lôi Nghiệp Nặng Về Trọng Kích Aggreate Gốc Root):
   public thucHienDongPhatThanhVipMienDich() {
      if (this.trang_thai === TinhTrangKhach.BI_BAN) {
         throw new Error("Người Này Đang Tội Ngục Sập Ban Khóa, Đòi Nâng VIP Tráo Cửa Tù ! Chặn DDD Ngay Đáy Logic Nghiệp Võ! ");
      } 
      // Dừng Sửa Table ! Mảng Đậm Cung Ghi Tầm: Đề Tài Aggregate ! 
      this.trang_thai = TinhTrangKhach.THANH_VIP;

      // DDD Sẽ Tạo Ra Event Nhả 1 Sự KIện Gữi Qua RabbitMQ Kêu Mảng Kho Tặng Khuyến Mãi Vip 
      // this.addDomainEvent(new KhachHangLenVipEvent(this.id, new Date()));
   }
}
```

## 🏆 Thành Quả Đạt Được Khi Tách Framework:
Thấy Không? Trong File Code `KhachHangAggregate.ts` **Hoàn Toàn Vắng Mặt Code Thư Viện SQL, Không Gắn Annotation Rườm Rà Nhựa Bể Kiểu Lạ Lọi `@Column`, Ngừa API `@Post` Lắt Kẻ Trộm Bug Lọt Giao Địch** . 

Toàn bộ Là TypeScript Bẩm Sinh Thần Lệnh Rặt Thuần 100%. Nếu Công Ty Năm Sau Đổi Framework Từ NestJS Xài Express Cùi Bắp, Hay Đổi Postgres Thành MongoDB. Kệ Họ! Nguyên Si Lõi Thư Mục `src/domain` Bấm Khóa Trừ Lỗi Xé Bưng Sang Gắn Chắp Chạy Phút Đầu! Đó Làm Lên Mác Sếp 6000$/ Tháng System Architect Đắt Tiền!
