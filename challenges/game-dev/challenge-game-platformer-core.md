# Challenge: Platformer Core Loop (Prototype)

- **Loại:** project
- **Mảng:** game-dev
- **Mức:** Beginner
- **Ước lượng thời gian:** 2-4 ngày
- **Prerequisites (tùy chọn):** Cơ bản về engine 2D (Godot/Unity/Unreal hoặc lib như Phaser/LÖVE), physics 2D cơ bản.

## Mục tiêu học tập
- Xây dựng core loop của một 2D platformer: movement, jump, collision, camera.
- Cải thiện feel/juice: acceleration/deceleration, coyote time, jump buffer, particles/screen shake.
- Thiết kế level nhỏ để test flow (intro → challenge → mastery).

## Đề bài
Xây một prototype 2D platformer ngắn (~3-5 màn) với các yêu cầu:
- Movement: chạy/trượt, nhảy (coyote time + jump buffer), có gravity và friction hợp lý.
- Collision & platform: tilemap/mesh; xử lý va chạm cạnh; slope (tùy chọn).
- Camera: follow smoothing; limit biên; (tùy chọn) lookahead.
- UX/Feel: particles khi tiếp đất/nhảy, screen shake nhẹ khi va mạnh, SFX cơ bản.
- Level: 3-5 màn tăng dần độ khó, có checkpoint hoặc restart nhanh.

## Đầu vào (Input)
- Asset tự chọn (free pack) hoặc primitive shapes.

## Đầu ra (Output)
- Build chơi được (web/desktop) + file project.
- README: controls, engine/tool version, cách build/run.

## Tiêu chí chấm (Acceptance)
- Movement cảm giác mượt, không bị kẹt/cross tile; coyote time + jump buffer hoạt động.
- Camera không gây chóng mặt; giữ nhân vật trong frame hợp lý.
- Màn chơi rõ ràng độ khó tăng dần; restart nhanh (≤2s) để thử lại.
- Code: tách logic movement/collision; config tham số (gravity, accel, friction, jump height).

## Gợi ý / Hint
- Tham số feel: accel/decel, max speed, gravity scale, jump apex, coyote time (~100-200ms), jump buffer (~100-200ms).
- Dùng debug overlay để xem velocity/collision box.
- Playtest ngắn, giảm latency input (vsync/input events).

## Reference / Solution (tùy chọn)
- Platformer feel notes: https://github.com/kittykatattack/feel-engineering
- Godot sample: https://github.com/godotengine/godot-demo-projects/tree/master/2d/platformer
- Unity 2D sample: https://github.com/Unity-Technologies/2d-platformer-challenge