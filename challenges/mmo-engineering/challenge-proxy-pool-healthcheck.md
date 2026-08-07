# Challenge: Proxy Pool Healthcheck

- **Loại:** project
- **Mảng:** mmo-engineering
- **Mức:** Intermediate
- **Ước lượng:** 1–2 ngày
- **Prerequisites:** [`domains/mmo-engineering/`](../../domains/mmo-engineering/README.md) (network/proxy docs)

## Đề bài
Xây service nhỏ quản lý danh sách proxy:
- Đăng ký proxy (host, port, protocol, meta)
- Healthcheck định kỳ (TCP hoặc HTTP egress check do bạn định nghĩa)
- API: list healthy proxies, mark bad, latency percentile
- Evict proxy fail N lần liên tiếp

## Acceptance
- [ ] Healthcheck chạy theo interval cấu hình được
- [ ] API trả về only-healthy mặc định
- [ ] Metrics: success rate, p95 latency (log hoặc /metrics)
- [ ] README lab + docker-compose optional
- [ ] Không hardcode credential trong git

## Gợi ý
Dùng queue/worker đơn giản; lưu state SQLite/Redis.
