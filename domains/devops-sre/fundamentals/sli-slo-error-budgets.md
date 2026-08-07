# SLI, SLO & Error Budgets

> [← DevOps & SRE](../README.md)

## Định nghĩa nhanh
- **SLI:** chỉ số đo được (availability, latency p99, success rate)
- **SLO:** mục tiêu theo thời gian (vd availability 99.9%/30 ngày)
- **Error budget:** phần “được hỏng” = 100% − SLO

## Ví dụ API
| SLI | Công thức | SLO |
| --- | --- | --- |
| Availability | successful / total (non-4xx-client) | 99.9% / 30d |
| Latency | p99 < 300ms | 99% requests |
| Freshness (batch) | data lag < 15m | 99% windows |

## Cách dùng error budget
- Budget còn → ship nhanh, experiment
- Budget cháy → freeze feature, ưu tiên reliability
- Review tuần: top burners theo endpoint/region

## Checklist viết SLO
- [ ] Gắn với user journey thật (login, checkout…)
- [ ] Có dashboard + alert burn-rate
- [ ] Có owner + review cadence

**Next:** [Three pillars of observability](../observability/three-pillars.md)

> **Last Updated:** August 2026
