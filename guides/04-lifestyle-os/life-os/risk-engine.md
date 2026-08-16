# 3️⃣ Risk Engine (Động cơ Phòng thủ)

> **"Để về đích thứ nhất, trước tiên bạn phải về đích đã."**

## 🎯 Mission & Outcomes
- **Mục tiêu:** Giữ hệ thống luôn sống sót trước tail risk và biến động lớn.
- **Output chính:** Risk Register, Risk Radar, Plan B playbook, Margin of Safety checklist.
- **Success Metrics:**
  - Quỹ khẩn cấp ≥ 6-12 tháng chi phí.
  - SPOF (single point of failure) count = 0 hoặc luôn có kế hoạch dự phòng.
  - Tail risk scenario được diễn tập ít nhất 1 lần/ quý.

## 🧠 Mental Model Stack
1. **Fat-tailed Distribution & Black Swan**
   - Thế giới không tuân theo phân phối chuẩn. Chuẩn bị cho sự kiện cực đoan.
2. **Ergodicity**
   - EV cao nhưng có xác suất phá sản → không chơi. Bảo toàn để tiếp tục lặp lại trò chơi.
3. **Barbell Strategy & Redundancy**
   - Phân bổ tài nguyên: 80% an toàn, 20% high-risk/high-upside.
4. **Antifragile / Hormesis**
   - Hưởng lợi từ va chạm nhỏ, luyện cơ chống chịu. Deep: [`antifragile-thinking.md`](../../01-mental-models/antifragile-thinking.md).
5. **Entropy & Maintenance**
   - Mọi thứ sẽ hỏng, nên bảo dưỡng trước khi hỏng.
6. **Tail vs Routine Risk**
   - Routine risk → automation, checklist. Tail risk → buffer, optionality.

## 🔍 Diagnostic Questions
1. Tôi đang phụ thuộc vào duy nhất một nguồn thu/khách hàng/nhà cung cấp?
2. Nếu mất thu nhập 6-12 tháng, tôi sống sao?
3. Hệ thống có SPOF nào không? Nếu điểm đó chết, toàn bộ hệ thống sập?
4. Tôi có đang sống quá sát biên (no buffer, no rest)?
5. Có tail risk nào bị bỏ qua chỉ vì xác suất thấp?

## 🛠️ Execution Playbook (Identify → Quantify → Mitigate → Monitor)
1. **Identify:** Liệt kê rủi ro theo domain (Finance, Health, Work, Geo, Network).
2. **Quantify:** Ước lượng impact, likelihood, time-to-impact. Phân nhóm tail vs routine.
3. **Mitigate:** Thiết kế buffer (margin of safety), Plan B, bảo hiểm, redundancy.
4. **Monitor:** Thiết lập trigger cảnh báo, review risk radar hàng quý.

## 📈 Metrics & Rituals
- **Risk Exposure Score:** điểm tổng theo risk register (impact × likelihood).
- **Runway:** số tháng sống được nếu thu nhập = 0.
- **Resilience Cadence:** Quarterly Risk Review, Monthly Burnout Check, Yearly Disaster Drill.

## 📡 Risk Radar mẫu

| Rủi ro | Trigger cảnh báo | Plan B / Hành động |
| --- | --- | --- |
| **Mất việc chính (Tech Layoff)** | - Tin đồn cắt giảm headcount<br>- KPI team đỏ 2 quý<br>- Sếp mới không ủng hộ | - Quỹ khẩn cấp 6 tháng<br>- Side income ≥30% lương<br>- Cập nhật portfolio + ping network mỗi quý |
| **Khủng hoảng sức khỏe (Burnout)** | - Ngủ <6h liên tục<br>- HRV tụt <40ms<br>- Dấu hiệu chán việc, khó tập trung | - Block lịch nghỉ 1 tuần<br>- Gặp bác sĩ/therapist<br>- Giảm 20% workload, chuyển giao task |
| **Biến động chính trị/khu vực** | - Tin hạn chế visa<br>- Quy định mới ảnh hưởng ngành<br>- Căng thẳng Mỹ–Trung leo thang | - Phân bổ tài sản đa quốc gia<br>- Theo dõi `politics/vietnam-system.md` & `world-order.md` mỗi tháng<br>- Chuẩn bị phương án remote/di chuyển |
| **Lệ thuộc 1 khách hàng lớn (Freelance)** | - Invoice trả chậm >15 ngày<br>- Scope creep liên tục<br>- Client thay đổi leadership | - Giới hạn 40% doanh thu/client<br>- Retainer hợp đồng<br>- Pipeline inbound 3-4 lead/tháng |
| **Rủi ro thanh khoản cá nhân** | - Chi tiêu >80% thu nhập<br>- Không còn hạn mức tín dụng<br>- Nợ xấu tăng | - Thiết lập budget 50/30/20<br>- Giữ cash ≥12 tháng chi phí<br>- Tái cấu trúc nợ, đàm phán lãi suất |

> **Tip:** Cập nhật Risk Radar mỗi quý. Khi trigger xảy ra, kích hoạt Plan B ngay.

## 🔗 Related Engines
- **Decision Engine:** Khi EV dương nhưng rủi ro cao, quay lại bảng `EV + Check Ruin` → [Decision Engine](./decision-engine.md).
- **Strategy Engine:** Sử dụng risk radar để chọn game có payoff bất đối xứng tốt → [Strategy Engine](./strategy-engine.md).

## 📝 Templates & Tools
- [Risk Radar Template](../../templates/productivity/risk-radar.md)
- [Disaster Simulation Checklist](../../templates/productivity/disaster-drill.md)
- [Cash Buffer Planner](../../templates/productivity/cash-buffer.md)
