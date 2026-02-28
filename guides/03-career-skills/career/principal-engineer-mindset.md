## 🧠 Tư duy của Principal Engineer & Lộ trình rèn luyện

Principal Engineer = “engineer lãnh đạo hệ thống” (không cần danh xưng quản lý). Họ mở khóa tầm ảnh hưởng thông qua thiết kế kiến trúc dài hạn, dẫn dắt kỹ thuật liên phòng ban và đảm bảo sản phẩm vận hành bền vững.

### 1. Vai trò & phạm vi trách nhiệm
- **System Ownership:** Chịu trách nhiệm end-to-end cho các hệ thống cốt lõi (availability, resilience, cost, roadmap 12–24 tháng).
- **Technical Strategy:** Định nghĩa guardrails kiến trúc, tiêu chuẩn code, adoption công nghệ mới.
- **Execution Lever:** Hỗ trợ từ pre-design → execution → launch, xử lý escalations, ra quyết định khi có mâu thuẫn.
- **Talent Multiplier:** Mentor Staff/Senior, thiết kế career ladder, tổ chức chương trình nâng cấp kỹ năng trong team.

### 2. Bộ tư duy cốt lõi
| Tư duy | Mô tả | Ví dụ áp dụng |
|:------|:------|:--------------|
| **Systems Thinking** | Nhìn toàn bộ lifecycle (client → service → data → ops) và các feedback loop | Khi thiết kế feature mới, họ dự đoán tác động tới capacity, incident protocols, chi phí hạ tầng |
| **Long-term Architecture** | Quyết định dựa trên 3–5 năm, ưu tiên tính tiến hóa hơn “giải nhanh” | Chọn kiến trúc modul hóa để dễ mở rộng cho multi-region hơn là default single region |
| **Leverage Mindset** | Hỏi “làm thế nào để một quyết định tạo tác động x10?” | Viết RFC chuẩn, template runbook để nhiều team reuse |
| **Communication as API** | Xem giao tiếp như hợp đồng: rõ ràng, có input/output | Tổ chức design review với agenda chuẩn, log lại quyết định |
| **Business-aware Engineer** | Hiểu KPI, chi phí, khách hàng để ưu tiên kỹ thuật đúng | Trade-off giữa tối ưu latency và cost để đạt margin mục tiêu |

### 3. Bộ kỹ năng & rèn luyện
1. **Architecture & Platform Thinking:**
   - Đọc/viết RFC cấp hệ thống, thực hành ADR (Architecture Decision Record).
   - Luyện Habit “Design Review”: tham gia review của team khác để học perspective mới.
2. **Technical Breadth:**
   - Mỗi quý chọn 1 domain bổ sung (Infra, Data, Security, ML, FinOps…).
   - Shadow team khác 1–2 sprint để hiểu context thực tế.
3. **Executive Communication:**
   - Storytelling cho non-tech stakeholder: BLUF (Bottom Line Up Front), link đến số liệu kinh doanh.
   - Tập viết memo tóm tắt rủi ro, chi phí, ROI cho ban lãnh đạo.
4. **Mentoring & Influence:**
   - Monthly mentorship session với Senior/Staff.
   - Dựng “Tech Guild” hoặc “Architecture Forum” để lan tỏa best practice.
5. **Operational Excellence:**
   - Lãnh đạo postmortem, root cause analysis multi-team.
   - Thiết kế playbook incident (SLO/SLA/SLA Breach).

### 4. Lộ trình rèn luyện 6–12 tháng
| Giai đoạn | Mục tiêu | Hoạt động chính |
|:---------|:---------|:----------------|
| Tháng 1–2 | Audit năng lực hiện tại | Đánh giá technical breadth, influence scope; xin feedback từ EM/Staff |
| Tháng 3–4 | Deep Dive 1 domain mới | Chọn dự án cross-team, viết RFC, trình bày design review |
| Tháng 5–6 | Scale qua mentorship | 1:1 mentoring, xây template hướng dẫn onboarding, chủ trì tech talk |
| Tháng 7–8 | Operational Mastery | Dẫn postmortem lớn, chuẩn hóa incident process |
| Tháng 9–10 | Strategic Impact | Đề xuất technical strategy 12–18 tháng, bảo vệ trước leadership |
| Tháng 11–12 | Document & Evangelize | Viết “Playbook Principal Engineer” nội bộ, chia sẻ tại community |

### 5. Checklist hành động nhanh
- [ ] Viết Architecture Vision cho hệ thống bạn phụ trách (roadmap 12 tháng).
- [ ] Thiết lập lịch review định kỳ với EM/PM để cập nhật risk & priority.
- [ ] Tổ chức ít nhất 1 design review/tháng (có template agenda).
- [ ] Mentor 2–3 kỹ sư cấp dưới, log lại tiến độ học tập.
- [ ] Dẫn dắt 1 postmortem quan trọng, ra action items theo S.M.A.R.T.
- [ ] Viết 1 bài internal blog hoặc public talk chia sẻ chiến lược kỹ thuật.

### 6. Tài nguyên gợi ý
- [System Design Guide](../../backend-dev/system-design-guide.md)
- [Monitoring & Observability](../../backend-dev/monitoring-observability.md)
- [Leadership Communication Checklist](../../productivity/meta-skills/working-with-ai.md)
- [Project Management Fundamentals](../productivity/meta-skills/project-management-fundamentals.md)
- Sách: *Staff Engineer* (Will Larson), *The Manager’s Path* (Camille Fournier), *An Elegant Puzzle* (Will Larson).

> **Ghi nhớ:** Principal Engineer là “voice of the system”. Họ không chỉ sửa bug lớn mà định hình cách tổ chức suy nghĩ về kỹ thuật. Mỗi tuần tự hỏi: *“Mình vừa tăng hay giảm entropy của hệ thống?”*