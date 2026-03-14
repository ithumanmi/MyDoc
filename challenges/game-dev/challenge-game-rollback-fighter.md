# Challenge: Networked Rollback Fighter (1v1)

- **Loại:** project
- **Mảng:** game-dev
- **Mức:** Advanced
- **Ước lượng thời gian:** 5-7 ngày
- **Prerequisites (tùy chọn):** Kinh nghiệm netcode, rollback, input delay; hiểu deterministic simulation hoặc state save/load; profiler network.

## Mục tiêu học tập
- Xây dựng game 1v1 với rollback netcode (GGPO-style) cho input latency thấp.
- Quản lý state snapshot/save & fast-forward để bù trễ.
- Giảm divergence bằng deterministic simulation.

## Đề bài
Tạo prototype fighting 1v1 đơn giản (2 nhân vật, 4-6 moves) với rollback netcode:
- **Prediction:** client gửi input; giả định input đối thủ (prediction) khi chưa nhận kịp.
- **Rollback:** lưu snapshot gần nhất; khi nhận input trễ, rollback và re-sim frame để đồng bộ.
- **Deterministic:** logic combat/physics tối giản và determinism (fixed timestep, tránh RNG không seed).
- **Networking:** peer-to-peer hoặc relay; hiển thị jitter/rollback count để debug.

## Đầu ra (Output)
- Build 2 client chơi được; log/overlay hiện ping, rollback count, frames re-sim.
- README: giải thích kiến trúc rollback, format snapshot, hạn chế đã biết.

## Tiêu chí chấm (Acceptance)
- Chơi được ở 80-150ms với ít hitch; rollback không phá game state.
- Snapshot/restore ổn định, không leak; re-sim không gây sai lệch rõ.
- Divergence test: chạy deterministic script 1000 frame, 2 client khớp state.

## Gợi ý / Hint
- Fixed timestep; tránh floating nondeterministic (có thể dùng int/fixed-point cho quan trọng).
- Giới hạn số entity/physics đơn giản để rollback nhanh.
- Lưu/restore input buffer, RNG seed, state entity chính.

## Reference / Solution (tùy chọn)
- GGPO overview: https://www.ggpo.net/
- Fighting rollback guide: https://github.com/pond3r/ggpo/blob/master/doc/intro_to_ggpo.md
- Deterministic sim tips: https://www.gafferongames.com/post/deterministic_lockstep/