# Case Study: Customer Churn Analysis

> [← Data Analytics](../README.md) | [Challenge SQL](../../../challenges/data-analytics/challenge-sql-window-cte-dashboard.md)

## Bối cảnh
SaaS B2C: churn tháng tăng từ 4% → 6.5%. CEO hỏi: **ai đang rời, vì sao, làm gì tuần này?**

## Câu hỏi phân tích (theo thứ tự)
1. Churn definition: cancel trong 30 ngày sau hết cycle? hay inactive 14 ngày?
2. Cohort: signup month × plan × channel
3. Leading indicators: support tickets, feature usage drop, payment fail
4. Segment actionable: có thể save bằng win-back không?

## Deliverables
| Artifact | Nội dung |
| --- | --- |
| SQL notebook | CTE: active base, churn events, features 14d |
| Dashboard | Cohort retention curve + churn reason mix |
| One-pager | 3 insights + 2 experiments A/B |

## SQL skeleton
```sql
WITH base AS (
  SELECT user_id, plan, signup_date
  FROM users
),
churned AS (
  SELECT user_id, churn_date, reason
  FROM cancellations
)
SELECT
  date_trunc('month', signup_date) AS cohort,
  plan,
  COUNT(*) AS users,
  COUNT(c.user_id)::float / COUNT(*) AS churn_rate
FROM base b
LEFT JOIN churned c ON b.user_id = c.user_id
  AND c.churn_date < b.signup_date + INTERVAL '90 days'
GROUP BY 1, 2
ORDER BY 1, 2;
```

## Acceptance (portfolio)
- [ ] Định nghĩa churn viết rõ 1 đoạn
- [ ] ≥1 chart retention theo cohort
- [ ] ≥2 khuyến nghị có owner giả định (Growth / CS)
- [ ] Ghi hạn chế dữ liệu (thiếu reason = null %)

**Skills:** SQL window/CTE · storytelling · [data-analytics-thinking](../data-analytics-thinking.md)

> **Last Updated:** August 2026
