# Challenge: Design a Rate Limiter

- **Loại:** interview
- **Mảng:** system-design
- **Mức:** Intermediate
- **Ước lượng:** 45–60 phút
- **Prerequisites:** [`domains/system-design/`](../../domains/system-design/README.md) · backend rate-limit kinh nghiệm

## Đề bài
Rate limiter cho public API: 100 req / user / phút, deploy nhiều instance.

## Cover bắt buộc
- Algorithm: token bucket vs sliding window (chọn 1 + lý do)
- Central store (Redis) vs local + sync
- Atomicity / race
- Response headers & 429 body
- Hot key / fairness

## Acceptance
- [ ] Giải thích sai số của algorithm chọn
- [ ] Mô tả failure mode khi Redis down (fail open vs closed)
- [ ] Ước lượng Redis ops/s
