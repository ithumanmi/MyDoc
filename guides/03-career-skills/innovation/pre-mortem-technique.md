---
title: "Pre-mortem Technique — chống Groupthink & Confirmation Bias"
description: "Gary Klein-style pre-mortem: giả định thất bại trước khi ship; SOP họp dự án; phá đồng thuận giả & confirmation"
updated: "2026-08-09"
canonical: true
tags: [pre-mortem, groupthink, confirmation-bias, project-management, decision-making, risk]
audience: [beginner, intermediate]
related:
  - design-sprint.md
  - rat-testing.md
  - brainstorming.md
  - facilitation-skills.md
  - ../../04-lifestyle-os/life-os/decision-engine.md
  - ../../04-lifestyle-os/life-os/risk-engine.md
  - ../../01-mental-models/psychology/cognitive-biases.md
  - ../productivity/meta-skills/meta-thinking-bias-filter.md
  - ../../01-mental-models/history/counterfactuals.md
  - ../../../templates/productivity/project-pre-mortem.md
sensitivity: public
---

# Pre-mortem Technique — phân tích trước thất bại

> [← Innovation](./README.md) · [Decision Engine](../../04-lifestyle-os/life-os/decision-engine.md) · [Bias Filter](../productivity/meta-skills/meta-thinking-bias-filter.md) · [Worksheet](../../../templates/productivity/project-pre-mortem.md)

**Pre-mortem** (Gary Klein): trước khi commit/launch, đội **giả định dự án đã thất bại thảm hại**, rồi lần ngược *vì sao* — viết độc lập, gom rủi ro, gán owner + mitigation.

Khác post-mortem (sau khi vỡ): pre-mortem = **học giả định thất bại khi còn đủ thời gian sửa**.

Cùng họ Stoic *Premeditatio Malorum* / prospective hindsight — nhưng thiết kế cho **nhóm dự án** để phá **Groupthink** và **Confirmation bias**.

## Agent SUMMARY

- Frame: *“Đã là tháng +N. Dự án fail nặng. Mỗi người: vì sao?”* — không “liệu có rủi ro không?”.
- Viết **độc lập trước** thảo luận → giảm Groupthink / sợ sếp.
- Confirmation bị phá vì nhiệm vụ = tìm bằng chứng *fail*, không bảo vệ kế hoạch đẹp.
- SOP: Set frame → Silent write 5–10′ → Round-robin → Cluster → Top risks → Owner + trigger + mitigation → Update plan.
- Worksheet: [`project-pre-mortem.md`](../../../templates/productivity/project-pre-mortem.md). EV + pre-mortem: [`decision-engine.md`](../../04-lifestyle-os/life-os/decision-engine.md).

---

## 1. Vì sao phá được hai bias

| Bias | Cơ chế trong dự án | Pre-mortem làm gì |
| --- | --- | --- |
| **Groupthink** | Đồng thuận sớm, ít ai “phá không khí”, thiểu số im | Yêu cầu mỗi người *phải* sinh nguyên nhân fail; silent generation trước when group talk |
| **Confirmation** | Chỉ tìm data ủng hộ roadmap / “chắc sẽ ổn” | Đổi nhiệm vụ nhận thức: não săn *bằng chứng thất bại* (prospective hindsight) |

Prospective hindsight (nghiên cứu nhận thức): tưởng tượng sự kiện **đã xảy ra** tăng khả năng nêu nguyên nhân cụ thể hơn hỏi “có thể sai ở đâu?”.

Không thay risk register đầy đủ — là **session kích hoạt** để rủi ro “ai cũng nghĩ thầm” lộ ra ([`risk-engine.md`](../../04-lifestyle-os/life-os/risk-engine.md)).

---

## 2. Khi nào chạy

| Nên chạy | Có thể skip |
| --- | --- |
| Kickoff dự án lớn / pivot | Task 1–2 ngày rõ ràng |
| Trước launch / demo / go-live | Quyết định đã hoàn toàn đảo ngược được zero-cost |
| Trước all-in budget / hiring wave | Brainstorm ý tưởng thô (dùng ideation trước) |
| Khi phòng họp “quá đồng thuận nhanh” | — |

Gắn Design Sprint / RAT: sau khi chọn direction, trước build nặng ([`design-sprint.md`](./design-sprint.md), [`rat-testing.md`](./rat-testing.md)).

---

## 3. SOP họp Pre-mortem (45–75′)

### Chuẩn bị
- Facilitator trung lập (không phải người “bán” kế hoạch mạnh nhất nếu được).  
- Artifact: 1 trang mục tiêu dự án + timeline + success metric (không 40 slide).  
- Tool: sticky / doc chung / worksheet in.

### Diễn biến

| Phút | Bước | Chi tiết |
| ---: | --- | --- |
| 0–5 | **Frame** | *“Hôm nay là [ngày tương lai]. Dự án đã thất bại nặng — trễ / over budget / user bỏ / uy tín thủng. Không thảo luận cứu chữa vội. Nhiệm vụ: giải thích vì sao điều đó đã xảy ra.”* |
| 5–15 | **Silent write** | Mỗi người ≥5 nguyên nhân cụ thể, viết riêng. Cấm nói chuyện. (Phá Groupthink) |
| 15–35 | **Round-robin** | Lần lượt đọc 1 ý / người, xoay vòng; chưa debate, chỉ clarify. Facilitator gộp trùng. |
| 35–50 | **Cluster** | Nhóm: Tech · People · Market · Process · External. Đánh dấu anti-confirmation: ý đi ngược “kế hoạch đẹp”. |
| 50–65 | **Prioritize** | Vote ảnh hưởng × khả năng (dot vote). Chọn Top 5–7. |
| 65–75 | **Mitigate** | Mỗi rủi ro: Owner · Early warning trigger · Hành động trước ngày D · Plan B nếu trigger cháy |

### Output bắt buộc
1. Danh sách rủi ro đã cluster.  
2. Top N có owner + trigger.  
3. 3 thay đổi kế hoạch *trong tuần này* (không chỉ “theo dõi”).

---

## 4. Câu hỏi kích hoạt (khi đội bí ý)

- *Giả định nào trong pitch nếu sai là chết dự án?* (RAT)  
- *Ai trong phòng đang không dám nói mối lo thật?*  
- *Chúng ta tin điều gì vì “sếp/khách thích” chứ không vì evidence?*  
- *Thất bại nào từng xảy ra ở team/công ty tương tự?* (availability có chủ đích — base rates)  
- *Nếu confirmation đang chạy: data nào sẽ chứng minh kế hoạch sai?* ([bias filter](../productivity/meta-skills/meta-thinking-bias-filter.md))

---

## 5. Facilitation — chống Groupthink trong phòng

| Làm | Không |
| --- | --- |
| Silent trước speak | Brainstorm miệng ngay (người lớn tiếng chiếm) |
| Người junior / mới nói sớm trong round | Sếp nêu “theo tôi chỉ có 2 rủi ro” trước |
| Thưởng ý “khó nghe” bằng cách ghi nhận | Tranh cãi “ý đó bi quan quá” giữa chừng |
| Tách **liệt kê fail** khỏi **bảo vệ ego plan** | Biến session thành pep talk |

Psychological safety nền: [`innovation-culture.md`](./innovation-culture.md) nếu có. Facilitation: [`facilitation-skills.md`](./facilitation-skills.md).

---

## 6. Ví dụ rút gọn (ship feature B2B)

**Frame:** *6 tháng nữa feature flop — churn tăng, sales không bán được.*

Silent ideas (mẫu):
- Onboarding giả định user đã hiểu jargon → activation thấp  
- Integration API đối tác trễ → demo luôn “coming soon”  
- Success metric chỉ vanity (signups) không retention  
- Sales overpromise scope → CS overload  
- Không ai own pricing experiment  

Mitigation mẫu:

| Rủi ro | Trigger | Hành động tuần này | Owner |
| --- | --- | --- | --- |
| Activation thấp | <40% complete setup / 7 ngày | Usability test 5 user + cắt jargon | PM |
| API trễ | Đối tác chưa sandbox ngày T−30 | Mock + contract date trong SOW | Eng lead |

---

## 7. Pre-mortem vs bà con gần

| Kỹ thuật | Thời điểm | Câu hỏi |
| --- | --- | --- |
| **Pre-mortem** | Trước commit | “Đã fail — vì sao?” |
| **Post-mortem / retro** | Sau sự cố | “Đã xảy ra — học gì?” |
| **Premeditatio (Stoic)** | Cá nhân / ngày | Worst-case + Plan B |
| **RAT** | Trước build | Giả định rủi ro nhất test rẻ ra sao? |
| **Risk register** | Liên tục | Catalog sống; pre-mortem *nạp* vào đây |

Counterfactual lịch sử: [`counterfactuals.md`](../../01-mental-models/history/counterfactuals.md).

---

## 8. Checklist 10 phút (cá nhân / lead)

- [ ] Ngày tương lai + định nghĩa “fail” đã nói rõ  
- [ ] Có silent write  
- [ ] ≥1 rủi ro “phá narrative đẹp” được giữ lại  
- [ ] Top rủi ro có owner + trigger  
- [ ] ≥1 thay đổi kế hoạch trong 7 ngày  
- [ ] Ghi vào Decision / Risk log  

Worksheet copy: [`templates/productivity/project-pre-mortem.md`](../../../templates/productivity/project-pre-mortem.md).

---

## One-liner

> Pre-mortem = bắt cả phòng **đóng vai lịch sử đã thua** trước khi thua thật — để Groupthink hết chỗ trốn và Confirmation phải nhìn bằng chứng fail.
