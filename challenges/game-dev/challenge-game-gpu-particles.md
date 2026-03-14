# Challenge: GPU Particles & VFX Scene

- **Loại:** project
- **Mảng:** game-dev
- **Mức:** Advanced
- **Ước lượng thời gian:** 3-5 ngày
- **Prerequisites (tùy chọn):** Kiến thức shader cơ bản (HLSL/GLSL), compute/particle system; hiểu batching/draw call; profiler GPU cơ bản.

## Mục tiêu học tập
- Xây hệ thống particle GPU (compute/vertex) để render số lượng lớn hiệu ứng ổn định FPS.
- Quản lý spawn/update/render pipeline trên GPU, truyền tham số từ CPU.
- Tối ưu overdraw/batching và đo hiệu năng.

## Đề bài
Tạo một scene VFX với nhiều particle (>=50k) gồm 2-3 effect (vd: explosion, spark, smoke/ribbon):
- **Spawn/update trên GPU**: dùng compute shader hoặc vertex shader với buffer; tránh update CPU nặng.
- **Render**: instancing/billboard hoặc point sprite; material tối ưu; hạn chế overdraw.
- **Control**: tham số hoá từ CPU (spawn rate, color ramp, lifetime); hỗ trợ random seed.
- **Profiling**: đo frame time GPU/CPU; so sánh trước/sau tối ưu.

## Đầu ra (Output)
- Scene chạy ~60 FPS ở cấu hình trung bình (tuỳ engine/hardware), hoặc báo cáo FPS/frame time với cấu hình GPU cụ thể.
- README: pipeline particle, tham số, số lượng, kết quả đo.

## Tiêu chí chấm (Acceptance)
- Particle chạy ổn định, không drop nặng khi spawn burst.
- Sử dụng GPU cho update/render; số draw call hợp lý (instancing/batching).
- Có số đo FPS/frame time và mô tả tối ưu (overdraw, culling, LOD).

## Gợi ý / Hint
- Dùng compute buffer (positions/velocities) + indirect draw; hoặc VFX Graph/Niagara nếu engine có.
- Giảm overdraw: depth pre-pass, soft particle với giới hạn, fade khi gần camera.
- Batch texture/material; tránh branch nặng trong shader; profile bằng GPU profiler.

## Reference / Solution (tùy chọn)
- GPU particle concepts: https://realtimevfx.com/ (forum, tutorials)
- Unity VFX Graph sample: https://github.com/Unity-Technologies/VisualEffectGraph-Samples
- Unreal Niagara docs: https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-visual-effects-in-unreal-engine