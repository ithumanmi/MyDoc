# 🔁 IP Rotation Algorithms

## 1. Goals
- Tránh bị fingerprint bởi pattern IP.
- Balance giữa trust (sticky) và an toàn (rotate).

## 2. Strategies

### Time-based Rotation
- Đổi IP sau mỗi `T` phút (ví dụ 10-15 phút).
- Implementation: cron job gửi AT command reset.
- Use case: nuôi tài khoản, flow cần session dài.

### Request-based Rotation
- Đổi IP sau `N` request/API call.
- Proxy layer track count per client.
- Dùng khi crawl dữ liệu hoặc brute form.

### Failure-based Rotation
- Khi gặp error (HTTP 403, captcha), trigger reset ngay.
- Cần log error code để phân loại.

## 3. Scheduler Design
- Maintain queue dongle với trạng thái (busy, cooling, offline).
- Assign client → dongle, lock sticky window.
- Khi cần rotate: release + enqueue reset.

Pseudo:
```python
if strategy == "failure" and resp.status in BLOCK_CODES:
    rotate(dongle)
elif strategy == "time" and session.age > TTL:
    rotate(dongle)
```

## 4. Metrics
- Success rate per IP.
- Avg session duration trước khi rotate.
- Block/captcha rate before vs after.

## 5. Checklist
- [ ] Log rotation reason (time/request/failure).
- [ ] Cooldown sau reset (chờ IP mới).
- [ ] Alert nếu một dongle rotate quá nhiều (có thể lỗi phần cứng).