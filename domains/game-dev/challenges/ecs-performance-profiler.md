# ⚙️ Unity Coding Challenge #3 – ECS Performance Profiler

## Bối cảnh
Bạn chuyển gameplay system sang Unity DOTS/ECS. Có hệ thống **ProjectileSystem** bắn 20k viên đạn/giây. Performance target: giữ 120 FPS trên PC mid-range. Bạn cần thiết kế profiler + optimizer nội bộ để phát hiện bottleneck và tự động scale down effect.

## Input
- Entities: `Projectile` với component `Position`, `Velocity`, `Lifetime`, `DamageType`.
- Hệ thống collider custom (Jobs/Burst) + VFX trails.

## Yêu cầu
1. Viết `ProjectileProfilerSystem` đo thời gian chạy từng phase (Move, Collision, Cleanup).
2. Nếu phase nào > budget (ví dụ 1ms), bật chế độ degrade: giảm spawn rate hoặc disable VFX trail.
3. Ghi log vào `NativeText` buffer để UI hiển thị.
4. Cung cấp API `RegisterPhase(string name, float ms)` và `OnBudgetExceeded(Action callback)`.
5. Tạo editor window hiển thị sparkline FPS/phases.

## Gợi ý
- Sử dụng `Unity.Profiling` + `ProfilerMarker` trong Jobs.
- Dùng `DynamicBuffer` để lưu config degrade theo priority.
- Unit test: đo performance bằng `Playmode Performance Test`.

## Deliverable
- DOTS system + editor tool (IMGUI). Đảm bảo buildable trong Entities 1.3.