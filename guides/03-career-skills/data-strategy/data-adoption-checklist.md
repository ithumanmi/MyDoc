# ✅ Data Strategy Adoption Checklist

> Đảm bảo chiến lược dữ liệu không chỉ nằm trên slide mà được triển khai thực tế.

## 1. Governance & Ownership

- [ ] Data Council hoạt động hàng tháng với agenda rõ ràng
	- Tham khảo [Data Council Agenda Template](./templates/data-council-agenda.md)
- [ ] Data Owner/Steward gán cho 100% bảng critical
- [ ] Document catalog + SLA ở một nơi dùng chung (Notion/Confluence)
- [ ] Incident playbook gắn liền với alert thực tế

## 2. Stack & Quality

- [ ] Mỗi job ETL có monitoring + retry logic
- [ ] dbt/transform có test (unique, not null, freshness)
- [ ] Semantic layer (metric definitions) lưu version control
- [ ] Observability dashboard báo cáo SLA tuần/tháng

## 3. Literacy & Enablement

- [ ] KPI dictionary truy cập được cho toàn công ty
- [ ] Bootcamp/Workshop định kỳ (ít nhất 1 quý/lần)
	- Dùng [Enablement Session Plan](./templates/data-enable-session.md)
- [ ] Slack/Teams channel #ask-data có người trực trả lời < 24h
- [ ] Newsletter hoặc townhall chia sẻ “Data Win” hàng tháng

## 4. Adoption Metrics

- [ ] Theo dõi % người dùng đăng nhập BI tool hàng tuần
- [ ] Dashboard usage heatmap (top 10 dashboard)
- [ ] Số yêu cầu thủ công vào BI team giảm dần theo quý
- [ ] Feedback survey sau mỗi enablement session

## 5. Change Management

- [ ] OKR của leader gắn với outcome dữ liệu (ví dụ giảm churn 2% nhờ insight)
- [ ] Roadmap truyền thông (email, all-hands) nêu rõ kỳ vọng
- [ ] Training buddy/mentor cho phòng ban mới onboard
- [ ] Retro hàng quý: điều gì cản trở adoption?

## 6. Continuous Improvement Backlog

- [ ] Tổng hợp yêu cầu tính năng / dashboard mới trong backlog
- [ ] Ưu tiên theo Impact/Effort và cập nhật công khai
- [ ] Ghi nhận thời gian lead time từ yêu cầu → deliverable

> 🧭 *Usage tip:* In checklist này và review cùng Data Council mỗi tháng để đảm bảo chiến lược chuyển hóa thành thói quen và kết quả đo được.