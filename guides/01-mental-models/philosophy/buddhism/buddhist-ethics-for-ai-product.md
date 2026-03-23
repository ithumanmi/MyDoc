# 🛡️ Buddhist Ethics for AI/Product

> “Giảm khổ” làm tiêu chí sản phẩm. Tránh dark patterns, tôn trọng attention và dignity của người dùng.

## 1) Nguyên tắc
- **Giảm khổ:** Feature có giảm stress, thao túng, nghiện? Nếu tăng khổ → thiết kế lại.
- **Từ bi + Trí tuệ:** Hiểu bối cảnh người dùng (compassion) + dữ liệu thực (wisdom).
- **Vô thường:** Kết quả thay đổi theo thời gian; cần review định kỳ tác động ngoài ý muốn.
- **Vô ngã:** Team không đồng nhất bản thân với metric; sẵn sàng rollback khi gây hại.

## 2) Red-flag Matrix
| Khu vực | Red flag | Tác hại | Hành động |
|---------|----------|---------|-----------|
| Attention | Infinite scroll, auto-play không giới hạn | Nghiện, mất thời gian, stress | Thêm “stop points”, nhắc nghỉ, tắt auto-play mặc định |
| Consent | Opt-out bury, pre-checked boxes | Vi phạm quyền riêng tư, mất trust | Opt-in rõ ràng, ngôn ngữ dễ hiểu, tắt pre-check |
| Dark UX | Hidden fees, bait-and-switch | Bất mãn, mất niềm tin | Minh bạch giá, confirm step |
| Data/AI | Shadow profiling, unclear model use | Xâm phạm privacy, bias | Data minimization, model card, explainability |
| Vulnerable users | Push upsell cho nhóm dễ tổn thương | Khai thác yếu điểm, hối hận | Guardrails theo ngữ cảnh, limit upsell |

## 3) Pre-launch Checklist (rút gọn)
- [ ] **Harm scan:** Ai có thể bị tăng khổ? (stress, nghiện, financial harm)
- [ ] **Consent rõ:** Opt-in minh bạch, dễ rút lại.
- [ ] **Data minimization:** Thu thập đủ dùng, có retention policy.
- [ ] **Bias & fairness:** Đã test bias? Có kênh phản hồi?
- [ ] **Kill-switch:** Điều kiện rollback khi vượt ngưỡng hại (churn tăng, complaint spike, báo chí tiêu cực).
- [ ] **Wellbeing signals:** Cho phép user đặt giới hạn, nhắc nghỉ, tắt thông báo dạng gây nghiện.

## 4) Scoring (Ethics Readiness)
- **Green:** Tác động tích cực rõ, guardrail đủ.
- **Yellow:** Có risk nhưng đã có kill-switch/monitor; cần launch hạn chế.
- **Red:** Dark patterns, thiếu consent/bias test → không launch.

## 5) Playbook xử lý vi phạm
1) **Pause & Acknowledge:** Ngừng feature gây hại, thông báo minh bạch.
2) **Repair:** Sửa UX, đền bù nếu cần.
3) **Prevent:** Thêm rule/checklist vào quy trình release; đào tạo team về ethics.

## 6) Ritual team (15’ trước release lớn)
- 5’ chạy Red-flag matrix trên feature.
- 5’ chọn kill-switch & metric theo dõi (complaint rate, time-on-task bất thường).
- 5’ viết 3 dòng “Nếu là người dùng dễ tổn thương, tôi thấy gì?”.

> Nhắc mình: “Metric tốt không đáng nếu nó tăng khổ cho người dùng.”