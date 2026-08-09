---
title: "Nghiên cứu kỹ hành vi con người — method playbook"
description: "Quan sát hành vi có kỷ luật: ABC, baseline, thí nghiệm nhỏ, đo lường, ethics; tránh đọc ý định thay hành vi"
updated: "2026-08-09"
canonical: true
tags: [behavior, research-methods, observation, psychology, ethics, habit, user-research]
audience: [beginner, intermediate]
related:
  - ../fundamentals/behavior.md
  - ../schools-of-thought/behaviorism.md
  - social-psychology.md
  - art-of-reading-people.md
  - reading-people-responsibility.md
  - ../fundamentals/perception-through-models.md
  - ../cognitive-biases.md
  - ../../../03-career-skills/productivity/meta-skills/meta-thinking-bias-filter.md
  - ../../../02-wealth-business/market-research/core/user-research-persona.md
  - cognitive-emotional-empathy.md
sensitivity: public
---

# Nghiên cứu kỹ hành vi con người — method playbook

> [← Psychology](../README.md) · [Behavior fundamentals](../fundamentals/behavior.md) · [Behaviorism](../schools-of-thought/behaviorism.md) · [Ethics đọc vị](./reading-people-responsibility.md)

**Nghiên cứu kỹ hành vi** ≠ đoán tính cách từ ấn tượng hay “đọc vị” để khoe. Là quan sát / đo / kiểm chứng **việc người ta làm** (và điều kiện xung quanh) một cách có kỷ luật — rồi mới suy ra động cơ với mức tin cậy rõ.

Educational. Nghiên cứu trên người thật cần consent & ethics; không thay IRB / luật dữ liệu khi làm nghiên cứu chính thức.

## Agent SUMMARY

- Ưu tiên **hành vi quan sát được** hơn nhãn tính cách; tách data vs diễn dịch ([perception-through-models](../fundamentals/perception-through-models.md)).
- Khung lõi: **ABC** (Antecedent–Behavior–Consequence) · baseline · thí nghiệm nhỏ · triangulation.
- Anti: mind-reading, confirmation sampling, n=1 phóng đại, Groupthink khi họp insight.
- Ethics: nghiên cứu để hiểu/phối hợp/bảo vệ — không khai thác ([reading-people-responsibility](./reading-people-responsibility.md)).
- Tool stack: sổ quan sát · Fogg MAP · habit loop · user interview + shadowing · Meta-Filter bias.
- Theory thói quen/động lực: [`behavior.md`](../fundamentals/behavior.md). Conditioning: [`behaviorism.md`](../schools-of-thought/behaviorism.md).

---

## 1. Nguyên tắc vàng

| # | Nguyên tắc | Ý |
| ---: | --- | --- |
| 1 | **Behavior > story** | “Họ nói sẽ…” ≠ “Họ đã…” — ghi cả hai nếu cần |
| 2 | **Context là nửa công thức** | Cùng người, khác môi trường / mệt / quyền lực → hành vi khác ([social psychology](./social-psychology.md)) |
| 3 | **Baseline trước can thiệp** | Không baseline = không biết có thay đổi thật |
| 4 | **Tách quan sát / suy diễn** | Cột A: camera. Cột B: hypothesis (gắn độ tin) |
| 5 | **n nhỏ vẫn được nếu khiêm tốn** | Insight định tính ≠ tổng quát dân số |
| 6 | **Ethics trước kỹ thuật** | Consent, tối thiểu hại, không vũ khí hóa |

---

## 2. Khung ABC (hành vi học ứng dụng)

```text
A Antecedent (trước)  →  B Behavior (hành vi)  →  C Consequence (sau)
   cue / người / chỗ        quan sát được           thưởng / phạt / thoát
```

| Cột | Hỏi | Ví dụ |
| --- | --- | --- |
| **A** | Ngay trước đó có gì? | Deadline, tin nhắn, đám đông |
| **B** | Họ *làm* gì (động từ)? | Trì hoãn gửi PR, cắt lời, rời họp sớm |
| **C** | Ngay sau nhận được gì? | Giảm lo tạm, tiếng cười nhóm, tránh conflict |

Habit loop Cue–Routine–Reward là ABC lặp ([`behavior.md`](../fundamentals/behavior.md)).  
Fogg: Behavior khi **Motivation × Ability × Prompt** hội tụ — dùng khi thiết kế/phân tích “vì sao không làm”.

---

## 3. Pipeline nghiên cứu (cá nhân → đội → user)

### Bước 1 — Câu hỏi hành vi (không câu hỏi tính cách)

| Tránh | Đổi thành |
| --- | --- |
| “Họ có phải narcissist không?” | “Trong 5 tương tác gần: họ cắt ai, nhận lỗi thế nào?” |
| “Team lười?” | “PR median lead time? % meeting không có agenda?” |
| “User không thích feature?” | “% complete activation bước 3 trong 7 ngày?” |

### Bước 2 — Quan sát có cấu trúc

**Shadowing / fly-on-the-wall** (user, đồng nghiệp — có phép):
- Khoảng thời gian cố định (vd 45′).  
- Ghi timestamp + hành vi + môi trường.  
- Không hỏi giữa chừng (làm bẩn data).

**Sổ 3 cột:**

| Time | Behavior (data) | Note / hypothesis |
| --- | --- | --- |
| 10:12 | Mở Slack 4 lần / 10′ khi ticket đỏ | Escape difficulty? |

### Bước 3 — Baseline
Đếm / tỷ lệ **trước** thay đổi: số lần, thời lượng, tần suất trong ≥3–7 ngày (tùy chu kỳ).

### Bước 4 — Triangulation
Ghép ≥2 nguồn:
1. Quan sát hành vi  
2. Artifact (log, commit, tin nhắn đã đồng ý dùng)  
3. Lời tự thuật (interview) — dùng để *giả thuyết*, không thay quan sát  

User research hệ thống: [`user-research-persona.md`](../../../02-wealth-business/market-research/core/user-research-persona.md) nếu có.

### Bước 5 — Thí nghiệm nhỏ (không cần lab)
- Đổi **một** biến A hoặc C (vd: ẩn prompt; đổi reward).  
- Giữ đo B.  
- Thời gian đủ ngắn để học, đủ dài để noise hạ.  

Conditioning cổ điển / operant: [`behaviorism.md`](../schools-of-thought/behaviorism.md).

### Bước 6 — Kết luận có độ tin
Viết: *Quan sát → Giả thuyết → Mức tin (thấp/TB/cao) → Việc làm tiếp / thử gì thêm.*  
Chạy Meta-Filter nếu kết luận “quá khớp” niềm tin sẵn ([`meta-thinking-bias-filter.md`](../../../03-career-skills/productivity/meta-skills/meta-thinking-bias-filter.md)).

---

## 4. Lỗi thường gặp khi “nghiên cứu” hành vi

| Lỗi | Nhận diện | Sửa |
| --- | --- | --- |
| **Mind-reading** | Gán động cơ không có data | Chỉ viết động từ đã thấy |
| **Confirmation sampling** | Chỉ nhớ case ủng hộ mình | Chủ động tìm case phản |
| **Fundamental attribution** | “Họ là người X” bỏ qua tình huống | Hỏi lại A (antecedent) |
| **Halo** | Một điểm tốt → suy mọi mặt | Tách trait / behavior instances |
| **Availability** | 1 case sốc = quy luật | Hỏi base rate / mẫu rộng hơn |
| **Interview ≠ behavior** | Tin survey hơn log | Ưu tiên observed khi mâu thuẫn |
| **Groupthink insight** | Họp “ai cũng thấy vậy” | Silent note trước rồi mới share (pre-mortem vibe) |

Nền bias: [`cognitive-biases.md`](../cognitive-biases.md).

---

## 5. Ethics — nghiên cứu sắc vẫn phải cẩn thận

| Được | Không |
| --- | --- |
| Quan sát công khai / có consent | Theo dõi lén riêng tư |
| Ghi pattern để thiết kế UX / coaching lành | Hồ sơ weakness để thao túng |
| Feedback dựa hành vi cụ thể | Dán nhãn nhân cách trước đám đông |
| Defense: nhận gaslighting / pressure | Offense: dùng psych để ép |

→ [`reading-people-responsibility.md`](./reading-people-responsibility.md) · [`dark-psychology-defense.md`](../dark-psychology-defense.md).

Cognitive empathy (hiểu model) hỗ trợ nghiên cứu; đừng nhầm với kết luận đã chứng minh ([`cognitive-emotional-empathy.md`](./cognitive-emotional-empathy.md)).

---

## 6. Bộ công cụ theo mục tiêu

| Mục tiêu | Dùng |
| --- | --- |
| Đổi thói quen bản thân | ABC + Fogg + baseline 7 ngày ([behavior](../fundamentals/behavior.md), [PP habits](./predictive-processing-anxiety-habits.md)) |
| Đọc động thái phòng họp | Body leak + consistency theo thời gian ([reading people](./art-of-reading-people.md), [bond-body](../../../04-lifestyle-os/life-os/bond-body-language.md)) |
| Hiểu áp lực xã hội | Conformity / obedience / bystander ([social psychology](./social-psychology.md)) |
| Sản phẩm / GTM | Shadowing + activation metrics + persona research |
| Quyết định nhóm | Pre-mortem để lộ hành vi né rủi ro ([pre-mortem](../../../03-career-skills/innovation/pre-mortem-technique.md)) |

---

## 7. Protocol 14 ngày (luyện “mắt hành vi”)

| Ngày | Việc |
| ---: | --- |
| 1–2 | Chọn 1 người/1 user journey; chỉ ghi động từ 20′/ngày |
| 3–4 | Thêm cột A–C cho mỗi hành vi quan trọng |
| 5–7 | Baseline đếm 1 metric (vd: lần mở phone khi bắt đầu deep work) |
| 8–10 | 1 thí nghiệm đổi A hoặc C; giữ đo B |
| 11–12 | Interview ngắn: so lời nói vs quan sát — ghi lệch |
| 13 | Chạy bias check trên kết luận |
| 14 | Viết 1 trang: Evidence / Confidence / Next test |

---

## 8. Map Docs

| Cần | Doc |
| --- | --- |
| Động lực, habit, Fogg | [`behavior.md`](../fundamentals/behavior.md) |
| Conditioning | [`behaviorism.md`](../schools-of-thought/behaviorism.md) |
| Xã hội | [`social-psychology.md`](./social-psychology.md) |
| Não / model | [`perception-through-models.md`](../fundamentals/perception-through-models.md) |
| Ethics | [`reading-people-responsibility.md`](./reading-people-responsibility.md) |
| User research | [`user-research-persona.md`](../../../02-wealth-business/market-research/core/user-research-persona.md) |

---

## One-liner

> Nghiên cứu kỹ hành vi = **camera trước, câu chuyện sau**: ghi việc đã xảy ra trong ngữ cảnh, đo baseline, thử một biến — và giữ ethics khi mắt đã sắc.
