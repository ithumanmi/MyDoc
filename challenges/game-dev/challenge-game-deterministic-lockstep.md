# Challenge: Deterministic Lockstep (RTS/Lite)

- **Loại:** project
- **Mảng:** game-dev
- **Mức:** Advanced
- **Ước lượng thời gian:** 4-6 ngày
- **Prerequisites (tùy chọn):** Kiến thức lockstep, determinism, fixed-step simulation; đồng bộ command tick; tránh float nondeterminism.

## Mục tiêu học tập
- Xây một prototype RTS-lite (hoặc top-down) với lockstep deterministic.
- Đồng bộ command theo tick; tái hiện đồng nhất giữa client.
- Test divergence và xử lý desync.

## Đề bài
Xây prototype top-down (vd: di chuyển unit, spawn, simple attack) với lockstep:
- **Command buffer:** client gửi command cho tick T+n; server/host broadcast command cho mọi client.
- **Deterministic sim:** fixed timestep; tránh float nondeterministic (có thể fixed-point); seed RNG.
- **Desync detection:** hash state mỗi N tick; log/alert khi khác nhau.

## Đầu ra (Output)
- Build nhiều client; log hash/state mỗi 100 tick; report nếu lệch.
- README: giải thích command schedule, tick rate, format command, cách detect desync.

## Tiêu chí chấm (Acceptance)
- Command thực thi đồng nhất ở mọi client sau 1000+ tick (desync ~0).
- Hash desync check hoạt động; có log cho diff.
- Không jitter: mọi client tiến cùng tick (có thể dùng delay để đệm).

## Gợi ý / Hint
- Tick cố định (vd 20-30 Hz); lùi command 1-2 tick để bù latency.
- Hash state: CRC/xxhash trên subset state (position/HP/commands). 
- Tránh nhập nhằng: sắp xếp command theo id/time, tránh random không seed.

## Reference / Solution (tùy chọn)
- Deterministic lockstep: https://www.gafferongames.com/post/deterministic_lockstep/
- Age of Empires lockstep notes: https://www.gamasutra.com/view/feature/131503/1500_archers_on_a_288_network_.php
- Fixed-point tips: https://randomascii.wordpress.com/2013/07/08/floatprecision/