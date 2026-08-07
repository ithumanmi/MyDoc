# Challenge: Design a URL Shortener

- **Loại:** interview
- **Mảng:** system-design
- **Mức:** Intermediate
- **Ước lượng:** 60–90 phút
- **Prerequisites:** [`domains/system-design/README.md`](../../domains/system-design/README.md)

## Mục tiêu
Luyện flow phỏng vấn: requirements → API → data → scale → trade-offs.

## Đề bài
Thiết kế `short.ly` hỗ trợ:
- Tạo short URL từ long URL (auth optional)
- Redirect 302/301 với latency thấp
- Analytics clicks cơ bản (optional stretch)
- Scale: 100M URLs, 10k RPS read

## Bạn phải cover
1. Functional / non-functional requirements + assumptions
2. API sketch (`POST /v1/links`, `GET /{code}`)
3. Encoding ID (base62) vs hash collision
4. DB schema + cache (Redis) cho hot keys
5. Availability: multi-region? redirect path critical
6. Abuse: rate limit, spam URLs

## Acceptance (self-score)
- [ ] Có ước lượng storage + QPS
- [ ] Có bottleneck và cách scale (read replica / cache)
- [ ] Nêu 2 trade-offs có chủ đích (consistency vs latency…)
- [ ] Diagram text/mermaid đọc được

## Hint
Đọc case URL shortener trong system-design domain nếu có; tự làm trước khi mở.
