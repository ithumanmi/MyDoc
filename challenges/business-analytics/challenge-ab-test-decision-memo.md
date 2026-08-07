# Challenge: A/B Test Decision Memo

- **Loại:** project
- **Mảng:** business-analytics
- **Mức:** Intermediate
- **Ước lượng:** 4–8 giờ
- **Prerequisites:** [`domains/business-analytics/`](../../domains/business-analytics/README.md) (A/B / metrics docs)

## Đề bài
Cho bảng kết quả giả lập experiment checkout button:
- Control vs Treatment: visitors, conversions, revenue
- Chạy 14 ngày, SRM check stub

Viết **decision memo ≤ 1 trang** cho VP Product: ship / iterate / abort.

## Acceptance
- [ ] Nêu primary metric + guardrails trước khi “p-value”
- [ ] Tính (hoặc giả lập đúng công thức) lift + CI / significance
- [ ] Kiểm tra sample ratio mismatch ý tưởng
- [ ] Quyết định rõ + risk nếu ship sớm
- [ ] Không chỉ nói “p < 0.05 nên ship”

## Output
Markdown memo + notebook/SQL phụ lục tính toán.
