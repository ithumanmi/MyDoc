---
title: "Clean Code Playbook cho Web Developer"
description: "Mindset, checklist và quy trình refactor giúp code sống khỏe lâu dài."
last_updated: 2026-03-04
---

# 🧼 Clean Code Playbook cho Web Developer

> Code sạch không phải là code “đẹp mắt”, mà là code “dễ sống cùng” trong nhiều năm. Bài này gói gọn mindset, nguyên tắc và checklist giúp bạn ship nhanh nhưng vẫn bảo trì được.

---

## 0. Clean Code Mindset

| Tư duy | Giải thích | Câu hỏi tự soi |
| --- | --- | --- |
| **Độc giả > tác giả** | Code viết xong là để người khác đọc lại (future-you). | Người khác đọc không cần hỏi bạn? |
| **Sự thật duy nhất** | Mỗi logic chỉ nên tồn tại một lần. | Có 2 nơi xử lý cùng rule? |
| **Tên nói hết ý** | 80% thời gian đọc code → đặt tên phải descriptive. | Biến/hàm có thể đoán qua tên? |
| **Fail fast** | Phát hiện bug càng sớm càng tốt (test, assert). | Có check input invalid ngay đầu? |
| **Iterate** | Code sạch là kết quả của refactor liên tục, không phải 1 lần viết xong. | Sau mỗi feature có refactor vòng nhỏ? |

---

## 1. Đặt tên như Product Designer

### 1.1 Rule chung

- Dùng danh từ cho class, object: `Invoice`, `UserSession`.
- Dùng động từ + object cho function: `calculateTax`, `generateReport`.
- Tránh viết tắt: `cnt`, `usr` chỉ làm bạn tương lai khóc.
- Context rõ ràng: nếu module đã là `auth/`, không cần prefix `authUserService`.

### 1.2 Checklist

- [ ] Tên phản ánh domain (ví dụ “CartItem”, không phải “ItemDto”).
- [ ] Không chứa type trong tên (`userList` → `users`).
- [ ] Tránh số vô nghĩa (`processData2`).
- [ ] Tên boolean bắt đầu bằng `is/has/should/can`.

> 💡 Tip: Nếu bạn mất >1 phút để đặt tên, hãy viết comment mô tả. Tên tốt sẽ xuất hiện từ comment đó.

---

## 2. Cấu trúc hàm & module

### 2.1 Hàm nhỏ, làm một việc

```ts
function applyCoupon(cart: Cart, coupon: Coupon): Cart {
  if (!isCouponValid(cart, coupon)) {
    throw new InvalidCouponError();
  }
  const discountedItems = cart.items.map(item => applyDiscount(item, coupon));
  return { ...cart, items: discountedItems };
}
```

- Hàm dưới 20 dòng ⇒ dễ test, dễ reuse.
- Early return thay vì lồng if sâu.
- Logic phức tạp ⇒ tách thành helper hoặc Strategy pattern.

### 2.2 Module theo domain

```
src/
  cart/
    cart.service.ts
    cart.controller.ts
    cart.schema.ts
  payment/
  user/
```

- Gom file theo domain (feature folder) thay vì layer thuần (`controllers/services`).
- Interface/contract nằm gần nơi dùng.
- Shared utils phải thật sự dùng chung và ổn định.

---

## 3. Comment & Documentation

- Comment để giải thích **tại sao**, không phải **làm gì**.
- Thay vì comment, hãy chuyển sang test (ví dụ giải thích edge case bằng test).
- Dùng docstring cho API/public functions (param, return, exception).
- Nếu phải viết TODO, luôn thêm owner + deadline: `TODO(vietanh, 2026-03-10): handle VAT change`.

---

## 4. Code Smells Radar

| Smell | Dấu hiệu | Cách xử lý |
| --- | --- | --- |
| **Long Function** | >50 dòng, nhiều comment phân đoạn | Tách thành hàm nhỏ theo domain verbs |
| **God Object** | Class xử lý quá nhiều trách nhiệm | Áp dụng SRP, domain service riêng |
| **Primitive Obsession** | Truyền `string` lung tung | Bọc bằng Value Object (`Email`, `Money`) |
| **Duplicate Logic** | Copy/paste giữa module | Tạo service chung hoặc decorator |
| **Magic Number/String** | Giá trị hardcode khó hiểu | Đổi thành constant có tên |
| **Shotgun Surgery** | Sửa một feature phải touch 5 file | Refactor để gom logic (module hóa) |

> 📌 Checklist: Mỗi lần review PR, quét qua bảng này để phát hiện sớm.

---

## 5. Quy trình Refactor 5 bước

1. **Đặt test bảo vệ**: Unit/integration test đảm bảo behavior cũ.
2. **Nhỏ hóa phạm vi**: Refactor từng module, không ôm cả repo.
3. **Đổi tên trước**: Rename giúp lộ rõ logic trước khi tách.
4. **Tách chức năng**: Extract function/class, đảm bảo dependency rõ.
5. **Dọn dependency**: Xóa import, file thừa; cập nhật doc.

> 🎯 Rule: Refactor chỉ hoàn thành khi CI xanh + diff dễ đọc hơn ban đầu.

---

## 6. Clean Code cho Frontend vs Backend

| Khía cạnh | Frontend | Backend |
| --- | --- | --- |
| **State management** | Tránh state global, ưu tiên derived state | Tách domain logic khỏi controller |
| **UI logic** | Component nhỏ, props rõ ràng | Template/response builder đơn giản |
| **Side effect** | Dùng custom hook/service để gom effect | Service layer quản lý I/O |
| **Performance** | Memoization, lazy load | Cache, batching query |
| **Testing** | Storybook, RTL, Cypress | Unit, integration, contract test |

---

## 7. Checklist PR Clean Code

- [ ] Tên branch + commit rõ ràng.
- [ ] Hàm/class mới có test kèm theo.
- [ ] Không duplicate logic.
- [ ] Không có console.log, TODO vô chủ.
- [ ] Config/secret không nằm trong code.
- [ ] README/Doc cập nhật nếu có breaking change.

> Tip: Turn checklist này thành PR template để ép team tuân thủ.

---

## 8. Tài nguyên đề xuất

- **Clean Code (Robert C. Martin)** – kinh điển nhưng nên chọn lọc áp dụng.
- **Refactoring (Martin Fowler)** – catalog các smell + kỹ thuật refactor.
- **Clean Architecture in Typescript** – ví dụ modern stack.
- **Kent C. Dodds blog** – testing-first mindset.

---

## 9. Bài tập luyện Clean Code

1. Lấy project cũ → viết thêm test cho module critical.
2. Refactor 1 file God-class thành nhiều domain service.
3. Tạo PR “naming-only” để luyện đặt tên (không đổi logic).
4. Dùng ESLint + SonarLint để scan smell và fix dần.
5. Viết tài liệu “Style Guide” riêng cho team sau khi thống nhất quy tắc.

> 📈 Sau 1-2 tháng luyện, bạn sẽ code chậm hơn trong ngày đầu nhưng nhanh hơn hẳn sau 1 sprint.

---

**Next Steps:**

- Chọn 1 repo cá nhân để áp dụng checklist trên ngay tuần này.
- Hẹn 1 buổi “Clean Code Kata” cùng team để nâng chuẩn đồng loạt.

**Remember:** Code bẩn khiến bạn “vay nợ” từ thời gian tương lai. Code sạch giúp bạn khỏi vỡ nợ kỹ thuật.