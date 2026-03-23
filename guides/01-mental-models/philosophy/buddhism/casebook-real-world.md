# 📂 Casebook thực chiến (Buddhist Ops)

> 10 tình huống thật thường gặp trong tech/business. Mỗi case: Chẩn đoán (Tam độc + hệ thống) → Phương án → Thực thi → Postmortem. Dùng để retro, huấn luyện leader, và giảm khổ trong tổ chức.

## Case Template (dùng cho mọi tình huống)
- **1) Chẩn đoán (2–5 phút):** Khổ đang lộ ở đâu? (stress, trust, xung đột, lỗi lặp lại). Tam độc nào nổi bật? Duyên khởi/điều kiện nào đang nuôi vấn đề?
- **2) Ái/Thủ cần thấy rõ:** Mình/đội đang bám vào “cái gì” và thiếu dữ liệu “gì” (vô minh) khiến phản ứng leo thang?
- **3) Phương án (5–10 phút):** Viết 2–3 lựa chọn khác đòn bẩy (không chỉ tweak nhỏ). Chọn option nào giảm khổ sớm nhất mà vẫn bền.
- **4) Thực thi (checklist ngắn):** Áp dụng 1 nghi thức STOP hoặc ritual giao tiếp; quyết định rõ ai chịu trách nhiệm và timeline.
- **5) Postmortem (sau 2–8 tuần):** 3 câu: “Điều gì làm khổ giảm?”, “Điều gì làm khổ tái xuất?”, “System change mới là gì?”
- **6) Metrics (để không biến thành cảm tính):** đo cả biến nội tâm (pause trước phản ứng, stress) và biến hệ thống (lỗi lặp lại, conflict rate, trust pulse).

## 1) Layoffs (Cắt giảm nhân sự)
- **Chẩn đoán:** Stress hệ thống (burn rate, runway), Sân (cáu với áp lực), Tham (giữ vanity projects), Si (delay quyết định). Culture trust đang mỏng.
- **Phương án:** (A) Cắt sâu một lần + minh bạch; (B) Cắt nhiều đợt nhỏ (tệ cho trust); (C) Pivot mô hình để giữ người cốt lõi.
- **Thực thi:** Dùng “STOP” tổ chức 2h để thu thập fact; công bố reason minh bạch (data + compassion); gói hỗ trợ (severance, giới thiệu việc). Giữ lại ritual lắng nghe sau thông báo.
- **Postmortem:** Đo trust/NPS nội bộ sau 2-4-8 tuần; kiểm tra liệu “khổ” có giảm (stress, rò rỉ talent). Document decision log để tránh lặp lại.

### Bài tập retro (leader/coaching)
- Fact nào chúng ta biết rõ (không tranh cãi)?
- Tam độc nào đã lái lựa chọn (Tham/Sân/Si)?
- System change mới là gì để khổ giảm lâu dài?

## 2) Conflict liên phòng ban (Product vs Sales/Marketing)
- **Chẩn đoán:** Sân (đổ lỗi), Si (bám narrative riêng), thiếu alignment về mục tiêu/định nghĩa “thành công”. Duyên khởi: incentive lệch.
- **Phương án:** Workshop alignment 90’: fact-base + user pain; OKR chung với 1-2 North Star; thiết kế incentive không triệt tiêu nhau.
- **Thực thi:** Facilitator trung lập, áp dụng Nonviolent Communication; ghi rõ quyết định và chủ sở hữu; thiết lập “escalation-free window” 2 tuần để thử.
- **Postmortem:** Review KPI chung + cảm xúc đội; log lần nào Tam độc nổi lên để tinh chỉnh ritual giao tiếp.

### Bài tập retro (leader/coaching)
- Fact nào đã sai/thiếu khiến conflict leo thang?
- Tam độc nào nổi bật nhất ở mỗi bên?
- Ritual/gate nào sẽ đổi để lần sau dễ align hơn?

## 3) Product rollback (Thu hồi tính năng lỗi)
- **Chẩn đoán:** Si (ảo tưởng kiểm soát, thiếu canary), Tham (push nhanh để kịp KPI), Sân (đổ lỗi QA/dev). Hệ thống thiếu guardrail.
- **Phương án:** (A) Rollback ngay + comms rõ; (B) Hotfix trong 24h nếu an toàn. Thêm canary/feature flag.
- **Thực thi:** Kích hoạt playbook incident; thông báo user minh bạch, nhận lỗi; retrospective trong 48h với 5 Whys.
- **Postmortem:** Thêm test/flag/monitor; đo giảm khổ: lỗi lặp lại? on-call stress? user trust?

### Bài tập retro (leader/coaching)
- Vì vô minh nào mà canary/guardrail không kích hoạt?
- Tham/Sân/Si nào làm chúng ta chậm rollback hoặc chậm thừa nhận?
- Guardrail nào cần thêm vào pipeline để giảm khổ lặp lại?

## 4) Founder burnout
- **Chẩn đoán:** Tham (overwork), Si (tưởng mình không thể nghỉ), Sân (cáu bẳn với team). Hệ thống: thiếu delegation, không ranh giới thời gian.
- **Phương án:** (A) Tạm nghỉ ngắn + chuyển giao; (B) Giảm phạm vi/OKR; (C) Mang vào co-founder/lead tạm.
- **Thực thi:** Daily mindfulness 10’; sleep/protein/movement check; delegation list 10 tasks; thiết lập “no-meeting blocks”.
- **Postmortem:** Stress score, sleep, conflict incidence sau 4 tuần; quyết định structural (hiring ops/Chief of Staff).

### Bài tập retro (leader/coaching)
- Điều kiện nào khiến founder vẫn rơi vào overwork (Si: “không thể nghỉ”)?
- Tam độc nào đang lái phản ứng với team?
- Thay đổi hệ thống/delegation nào giảm khổ bền vững?

## 5) Team trust collapse (mất niềm tin)
- **Chẩn đoán:** Sân (phản ứng phòng thủ), Si (thiếu fact), lời hứa vỡ, incentive lệch. Duyên khởi: giao tiếp mơ hồ.
- **Phương án:** Listening tour 1-1; công khai fact & lỗi hệ thống; co-create 3 cam kết ngắn hạn có thể đo.
- **Thực thi:** Weekly check-in 30’; public dashboard cam kết; “no blame, all learn” rule cho 1 tháng.
- **Postmortem:** Trust pulse survey; nếu không cải, thay đổi nhân sự chủ chốt hoặc incentive.

### Bài tập retro (leader/coaching)
- Lời hứa nào bị “đứt dây” và vì điều kiện gì?
- Tam độc nào làm đội phản thủ/đổ lỗi?
- Cam kết tiếp theo cần rõ owner + timeline + metric nào?

## 6) Security incident (data leak nhẹ)
- **Chẩn đoán:** Si (coi nhẹ bảo mật), Tham (ưu tiên velocity), hệ thống thiếu runbook. Sân tiềm ẩn khi blame.
- **Phương án:** Contain → Communicate → Cure. Minh bạch với user/partner.
- **Thực thi:** Kích hoạt incident commander; thông báo theo pháp lý; vá lỗ hổng; credit on-call.
- **Postmortem:** Add tabletop drills; rate-limit, secrets scan; đo on-call burnout.

### Bài tập retro (leader/coaching)
- Vô minh nằm ở “thiếu hiểu biết” hay “thiếu quy trình”?
- Tham/Sân/Si nào làm chúng ta xem nhẹ hoặc phản ứng không tử tế?
- Hệ thống phòng ngừa nào (runbook, scan, drills) cần nâng cấp?

## 7) Acquisition offer (đề nghị mua lại)
- **Chẩn đoán:** Tham (exit nhanh), Sân (chán vận hành), Si (ảo tưởng synergy). Duyên khởi: runway, thị phần.
- **Phương án:** (A) Bán toàn bộ; (B) Bán một phần/earn-out; (C) Từ chối và raise/nhảy thị trường khác.
- **Thực thi:** Decision log EV + Regret; tư vấn pháp lý; bảo vệ team core (retention plan).
- **Postmortem:** Đánh giá sau 6-12 tháng: retention, văn hóa, stress, sản phẩm.

### Bài tập retro (leader/coaching)
- Fact nào về thị trường/runway giúp quyết định “tỉnh” hơn?
- Tam độc nào làm ta nghiêng về một option quá sớm?
- System change nào giúp retention/khổ giảm sau M&A?

## 8) Mass hiring rồi low performance
- **Chẩn đoán:** Tham (scale nhanh), Si (đánh giá sai fit), hệ thống onboarding yếu. Sân trong review.
- **Phương án:** Freeze + đánh giá lại; thiết kế onboarding 30/60/90; pairing với high-performer.
- **Thực thi:** Reset kỳ vọng rõ; coach hoặc chuyển vai; không đạt thì tách sớm nhưng tử tế.
- **Postmortem:** Hire bar, loop, JD rõ outcome; check ratio manager/IC.

### Bài tập retro (leader/coaching)
- “Sai vì thiếu dữ liệu” hay “sai vì hệ thống tuyển dụng/onboarding”?
- Tam độc nào làm chúng ta đánh giá/feedback lệch?
- Cần đổi onboarding loop nào để performance lên dần?

## 9) Founder/Board conflict
- **Chẩn đoán:** Tham (control), Sân (phòng thủ), Si (khác mental model). Duyên khởi: mục tiêu/ánh xạ rủi ro khác nhau.
- **Phương án:** Mediation trung lập; re-contract mục tiêu 12-18 tháng; clarity về quyền quyết định.
- **Thực thi:** Session data-first; tách người/vấn đề; nếu không, xem xét tách lộ trình hoặc buyout.
- **Postmortem:** Thiết lập nhịp thông tin đều; check-in niềm tin hàng quý.

### Bài tập retro (leader/coaching)
- Nút thắt là “mục tiêu sai” hay “bất đối xứng thông tin”?
- Tam độc nào làm đối thoại thiếu thật?
- Cần thay nhịp/cơ chế thông tin nào để giảm xung đột?

## 10) Product dark patterns backlash
- **Chẩn đoán:** Tham (đẩy metric), Si (xem nhẹ ethics), Sân (ignore feedback). Hệ thống thiếu review đạo đức.
- **Phương án:** Ngừng pattern gây hại; công bố sửa; thiết lập review ethics.
- **Thực thi:** Audit UX; sửa onboarding/consent; đền bù nếu cần.
- **Postmortem:** Thêm checklist “user dignity”; đo churn/trust sau 4-12 tuần.

### Bài tập retro (leader/coaching)
- Fact nào chứng minh pattern “tăng khổ” cho người dùng?
- Si/Tham/Sân nào khiến ta trì hoãn sửa?
- System change nào đảm bảo ethics review chạy trước release?

## System Levers (cẩm nang thay đổi điều kiện)
- **Thông tin (Information):** tăng fact-base, minh bạch reason, dashboards thay vì rumor.
- **Incentives/Constraints:** chỉnh KPI/ownership để hành vi “giảm khổ” được thưởng.
- **Ranh giới (Boundaries):** firm but kind: rõ cái không chấp nhận + đường escalation/HR.
- **Quy trình & guardrails:** feature flags, rollback/circuit breakers, runbook cho incident.
- **Giao tiếp (Communication protocols):** chánh ngữ, NVC, facilitator trung lập; “no blame, all learn”.
- **Ritual & feedback loops:** STOP trước quyết định; retro định kỳ; pause windows để tránh escalating.
- **Nuôi nền tâm (Inner practice):** deep work block, metta, label Tam độc để giảm phản xạ tự vệ.

## Decision Log Sheet (copy/paste)
Điền theo nhịp retro (2–8 tuần), tránh biến thành “tự sự cảm xúc”:

| Trường | Template |
|---|---|
| Case/Tình huống | Mô tả 1–2 câu, tập trung vào điều đang xảy ra |
| Mục tiêu giảm khổ | Khổ cụ thể đang giảm là gì (stress/trust/conflict/lỗi lặp lại)? |
| Tam độc nổi bật | Chọn 1–2 độc (Tham/Sân/Si) + dấu hiệu quan sát được |
| Facts (bằng chứng) | 3 fact ít tranh cãi nhất (số liệu, log, lời nói thô) |
| Options | 2–3 lựa chọn khác đòn bẩy (không tweak nhỏ) |
| Quyết định & lý do | Chọn option nào + lăng kính EV/Regret hoặc “giảm khổ sớm nhất” |
| Kill-switch/tiêu chí dừng | Nếu metric X < / > threshold Y trong Z tuần thì dừng/đổi |
| System change | Levers nào sẽ đổi: Information / Incentives / Boundaries / Guardrails / Communication / Ritual |
| Chủ sở hữu + timeline | Ai làm, deadline, ngày review |
| Postmortem update | 2 tuần sau: “điều gì giảm khổ?”, 8 tuần sau: “điều gì tái xuất?” |

---

> Dùng mỗi case như bài tập: viết decision log, Tam độc nổi bật, và 1 thay đổi hệ thống để giảm khổ lâu dài.