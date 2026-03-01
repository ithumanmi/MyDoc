# 📊 Personal Metrics Dashboard

> Bộ thang đo tự đánh giá toàn diện (tính cách, công việc, trình độ, kỹ năng). Chấm điểm 1-5 mỗi tuần/tháng để theo dõi tiến bộ.

## 1. Personality & Mindset Metrics

| Metric | Câu hỏi đánh giá | Thang điểm | Phương pháp cải thiện |
| --- | --- | --- | --- |
| **Self-discipline** | Tôi có hoàn thành 90% kế hoạch tuần? | 1: Thường xuyên trễ<br/>5: Gần như luôn đúng kế hoạch | Dùng [daily-log.md](./daily-log.md), áp dụng rule 2 phút, review cuối ngày |
| **Growth Mindset** | Khi gặp thất bại, tôi học được gì? | 1: Đổ lỗi/than vãn<br/>5: Có action item rõ | Ghi lại bài học vào [weekly-review.md](./weekly-review.md), áp dụng “lỗi = dữ liệu” |
| **Emotional Stability** | Tôi giữ bình tĩnh khi bị push deadline? | 1: Dễ bật lại<br/>5: Bình tĩnh giải quyết | Sử dụng [stoicism-for-modern-life.md](../guides/04-lifestyle-os/well-being/mental-resilience/stoicism-for-modern-life.md) |
| **Confidence & Presence** | Tôi có thể trình bày ý tưởng rõ ràng? | 1: Lắp bắp/mất ý<br/>5: Trình bày mạch lạc, có ví dụ | Luyện nói trước gương, tham gia sharing nhỏ trong cộng đồng |
| **Integrity** | Tôi có làm đúng cam kết không ai giám sát? | 1: Thường bỏ<br/>5: Tự giác hoàn thành | Ghi lại cam kết vào Notion/Trello, check-ins hằng tuần |

## 2. Career & Work Execution Metrics

| Metric | KPI đề xuất | Tracking tool |
| --- | --- | --- |
| **Application Velocity** | Số hồ sơ gửi/tuần (target: 5) | Sheet “Job Pipeline” hoặc Notion |
| **Interview Prep Hours** | Thời gian luyện DSA/system design (target: 6h/tuần) | [daily-log.md](./daily-log.md) |
| **Shipping Cadence** | Số feature/demo hoàn thành (target: 1 deliverable/2 tuần) | Kanban board (Trello/Linear) |
| **Networking Touchpoints** | Số cuộc chat/email follow-up (target: 2-3/tuần) | CRM cá nhân (Airtable/Notion) |
| **English Practice** | Số giờ nghe/nói/viết (target: 10h/tháng) | Notion habit tracker hoặc app (Duolingo log) |

## 3. Technical & Skill Proficiency Metrics

| Skill Cluster | Mô tả cấp độ | Thang đo 1-5 | Resource gợi ý |
| --- | --- | --- | --- |
| **Unity Gameplay Engineering** | OOP, Physics, Animation, Input System | 1: Chỉ làm theo tutorial<br/>5: Thiết kế gameplay system hoàn chỉnh | [unity-deep-dive](../domains/game-dev/unity-deep-dive/) |
| **Graphics & Optimization** | URP/HDRP, profiling, batching, DOTS | 1: Không tối ưu<br/>5: Giữ FPS ổn định trên đa nền tảng | [graphics modules](../domains/game-dev/graphics/) |
| **Backend NodeJS/TS** | API design, database, auth, deployment | 1: CRUD cơ bản<br/>5: Viết microservice production-ready | [api-design-guide](../domains/backend-dev/api-design-guide.md), [system-design-guide](../domains/backend-dev/system-design-guide.md) |
| **AI Integration** | Prompting, LLM API, gameplay AI | 1: Chỉ dùng lib có sẵn<br/>5: Xây custom pipeline/agent | [ai-engineering-roadmap-2026.md](../domains/ai-ml/ai-engineering-roadmap-2026.md) |
| **DevOps / Tooling** | CI/CD, cloud deploy (Render/Railway), logging | 1: Chạy local<br/>5: Thiết lập pipeline tự động | [devops-sre](../domains/backend-dev/devops-sre/) |

Chấm điểm từng skill mỗi tháng. Nếu skill nào ≤3: lập kế hoạch học tập (course, project, mentorship) cho tháng kế tiếp.

## 4. English & Communication Metrics

| Dimension | Mục tiêu | Thang đo | Gợi ý |
| --- | --- | --- | --- |
| **Listening** | Hiểu ≥80% podcast/game dev talk | 1: <30% hiểu<br/>5: ≥90% | Shadowing 15 phút/ngày (Fireship, GDC talks) |
| **Speaking** | Trình bày project 5 phút không lúng túng | 1: Dừng liên tục<br/>5: Tự nhiên, logic | Mock presentation/coffee chat mỗi tuần |
| **Writing** | Viết devlog/blog tiếng Anh ≥150 từ/lần | 1: Không viết<br/>5: Viết đều 1-2 bài/tuần | Devlog LinkedIn/itch.io, Grammarly check |
| **Reading** | Đọc doc Unity/Node không tra từ điển liên tục | 1: Cần dịch<br/>5: Đọc flow | Đọc release notes, API docs mỗi ngày 10 phút |

## 5. Review Template (Điền hàng tuần)

```markdown
### Weekly Metrics Review (Tuần __)

**1. Personality & Mindset**
- Self-discipline: __/5
- Growth mindset: __/5
- Emotional stability: __/5
- Confidence: __/5
- Integrity: __/5

**2. Career & Work Execution**
- Applications gửi: __ / 5
- Interview prep hours: __ / 6h
- Shipping deliverable: Hoàn thành? (Y/N)
- Networking touchpoints: __ / 2
- English hours: __ / 2.5h (≈10h/tháng)

**3. Technical Skills**
- Unity Gameplay: __/5
- Graphics/Optimization: __/5
- Backend Node/TS: __/5
- AI Integration: __/5
- DevOps/Tooling: __/5

**4. English & Communication**
- Listening: __/5
- Speaking: __/5
- Writing: __/5
- Reading: __/5

**Wins (3 điều đạt được):**
1. ...
2. ...
3. ...

**Bottlenecks & Fix:**
- Issue 1 → Action ...
- Issue 2 → Action ...

**Focus tuần tới:**
1. ...
2. ...
3. ...
```

> Lưu ý: Bảng metric này có thể mở rộng thêm vào Notion/Google Sheet để vẽ biểu đồ trend theo tháng.