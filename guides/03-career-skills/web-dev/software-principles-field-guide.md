---
title: "Software Principles Field Guide"
description: "Tổng hợp SOLID, DRY, KISS, YAGNI và các pattern giúp viết hệ thống bền vững."
last_updated: 2026-03-04
---

# 🧭 Software Principles Field Guide

> Khi dự án phình to, code style thôi là chưa đủ. Bạn cần nguyên tắc để ra quyết định kiến trúc nhanh mà vẫn đúng. Dưới đây là “cẩm nang bỏ túi” các nguyên tắc quan trọng nhất.

---

## 0. Bản đồ tổng quan

| Nhóm | Nguyên tắc | Ghi nhớ nhanh |
| --- | --- | --- |
| **Thiết kế hướng đối tượng** | SOLID | Tách trách nhiệm, mở rộng dễ, phụ thuộc ngược |
| **Tối ưu effort** | DRY, KISS, YAGNI | Đừng lặp lại, keep simple, không làm sớm |
| **Kiến trúc** | CQRS, Hexagonal, Layered | Tách đọc/ghi, cô lập domain |
| **Đồng bộ team** | Convention over Configuration, Twelve-Factor | Quy tắc chung giúp scale |

---

## 1. SOLID bằng tiếng Việt dễ nhớ

### S – Single Responsibility Principle

- Mỗi module/class chỉ nên có **1 lý do để thay đổi**.
- Áp dụng: Controller chỉ nhận request + gọi service; validation tách riêng.

> Checklist: Khi product đổi một rule, bạn chỉ cần chạm 1 file?

### O – Open/Closed Principle

- “Open for extension, closed for modification”.
- Ví dụ: Thêm phương thức thanh toán qua Strategy mới, không sửa switch-case cũ.

### L – Liskov Substitution Principle

- Subclass phải thay thế được superclass mà không đổi behavior.
- Dấu hiệu vi phạm: override mà throw “NotImplemented”.

### I – Interface Segregation Principle

- Interface nhỏ, cụ thể; client không bị ép implement method không dùng.
- Ví dụ: `ReadableStream` & `WritableStream` tách riêng.

### D – Dependency Inversion Principle

- Module cấp cao không phụ thuộc module cấp thấp; cả hai phụ thuộc abstraction.
- Thực thi bằng DI container, interface, hoặc event bus.

---

## 2. DRY, KISS, YAGNI, SOC

| Principle | Khi áp dụng | Anti-pattern |
| --- | --- | --- |
| **DRY (Don’t Repeat Yourself)** | Khi 2 đoạn code implement chung 1 rule nghiệp vụ | Copy/paste fix bug 2 nơi |
| **KISS (Keep It Simple, Stupid)** | Ưu tiên giải pháp đơn giản nhất đáp ứng yêu cầu hiện tại | Over-engineer microservice cho app todo |
| **YAGNI (You Aren’t Gonna Need It)** | Reject tính năng chưa có user cần | “Để sau dễ hơn” → rewrite |
| **SoC (Separation of Concerns)** | Tách UI/logic/data, tách read/write | Controller chứa cả SQL query |

> ⚠️ Đừng biến DRY thành WET (Write Everything Twice) bằng việc trừu tượng hóa quá sớm. Ưu tiên duplication có chủ đích trước khi tạo abstraction xấu.

---

## 3. Principle cho kiến trúc hiện đại

### 3.1 CQRS

- **Command Query Responsibility Segregation**: tách luồng đọc (query) và ghi (command).
- Lợi ích: tối ưu performance từng luồng, dễ scale.
- Dùng khi: hệ thống có nhiều báo cáo đọc-heavy, logic ghi phức tạp.

### 3.2 Event Sourcing

- Lưu **chuỗi sự kiện** thay vì trạng thái cuối.
- Dùng cho hệ thống audit, fintech, game state.

### 3.3 Hexagonal / Ports and Adapters

- Domain nằm giữa, I/O (DB, API, Queue) là adapter.
- Giúp test domain mà không cần infra thật.

### 3.4 Twelve-Factor App

- Hướng dẫn build SaaS cloud-native: config qua env, stateless, log stdout…

> Tip: Không cần áp dụng hết, hãy chọn 1-2 nguyên tắc phù hợp với quy mô.

---

## 4. Khi nào nguyên tắc bị lạm dụng?

| Symptom | Nguyên nhân | Cách xử lý |
| --- | --- | --- |
| Abstraction quá sâu | DRY cực đoan | Chấp nhận duplicate có chủ đích, refactor sau khi rule ổn định |
| Module nhỏ li ti | SOLID hiểu sai | Gom lại theo domain, tránh class chỉ có 1 method |
| Không con nào hiểu code | Pattern chồng lên pattern | Viết ADR (Architecture Decision Record) giải thích lý do |
| Không ship được tính năng | YAGNI/KISS cực đoan (thiếu chuẩn) | Có roadmap kỹ thuật rõ ràng trước khi tối giản |

---

## 5. Checklist áp dụng nguyên tắc

- [ ] Viết ADR mỗi lần quyết định kiến trúc lớn.
- [ ] Pull Request template có mục “Nguyên tắc áp dụng”.
- [ ] Code review: hỏi “quyết định này dựa trên principle nào?”.
- [ ] Quarterly Architecture Review để loại bỏ abstraction lỗi thời.
- [ ] Onboarding doc giải thích pattern/domain chính.

---

## 6. Tài nguyên đào sâu

- **Design Patterns (GoF)** – nền tảng OOP patterns.
- **Implementing Domain-Driven Design (Vaughn Vernon)** – domain-first architecture.
- **Clean Architecture (Uncle Bob)** – boundary giữa domain và infra.
- **Patterns of Enterprise Application Architecture (Martin Fowler)** – catalog pattern backend.

---

## 7. Bài tập tự luyện

1. Chọn 1 module cũ → viết ADR giải thích hiện trạng + nguyên tắc cần áp dụng.
2. Refactor 1 class God object bằng SOLID (tách interface, apply strategy).
3. Viết PoC microservice theo Hexagonal (controller → use case → port).
4. Tạo workshop nội bộ: mỗi dev trình bày 1 principle + demo code.
5. Đặt rule commit: thêm tag `[DRY]`, `[SOLID]` khi refactor theo nguyên tắc.

> 🎯 Mục tiêu: biến principles từ lý thuyết thành “muscle memory” trong mọi review và thiết kế.

---

**Next Steps:**

- Lưu bài này vào wiki team, bổ sung ví dụ từ codebase thực.
- Đặt lịch 1 giờ/tuần cho “Architecture Office Hour” để bàn về principles.

**Remember:** Nguyên tắc là la bàn—dùng để định hướng, không phải xiềng xích. Áp dụng đúng lúc sẽ giúp bạn ship nhanh hơn, không phải chậm hơn.