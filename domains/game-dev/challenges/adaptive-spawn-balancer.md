# 🎮 Unity Coding Challenge #1 – Adaptive Spawn Balancer

## Bối cảnh
Bạn xây dựng game roguelite top-down (Unity URP). Mỗi wave spawn enemy theo **RoomDifficulty**. Tuy nhiên, người chơi có thể nâng cấp vũ khí và di chuyển giữa các phòng với tốc độ khác nhau. Bạn cần một hệ thống spawn thích ứng dựa trên **Player Power Score** và **Room Stress Score**.

## Input signals
- `PlayerPower` (float): tổng hợp từ DPS, defense, relic.
- `RoomStress`: dựa trên số enemy sống, số đạn trên màn, thời gian chưa clear.
- `SpawnBudget`: scriptable object chứa cấu hình min/max spawn per wave.

## Yêu cầu
1. Viết algorithm chạy mỗi 0.5s để quyết định lượng enemy spawn thêm.
2. Ưu tiên spawn loại enemy khác nhau dựa vào `PlayerPower` (power thấp → spawn chậm).
3. Đảm bảo tổng `ActiveEnemies` không vượt `SpawnBudget.maxAlive`.
4. Hỗ trợ **multiplayer co-op**: tính `PlayerPower` trung bình + highest modifier.
5. Tối ưu: hệ thống phải chạy dưới 0.2ms/frame trên target device.

## Gợi ý kỹ thuật
- Dùng `AnimationCurve` hoặc `Burst compiled job` để map power → spawn rate.
- Lưu `SpawnTicket` queue để tránh spike.
- Viết unit test với `PlayMode Test` mô phỏng PlayerPower thay đổi liên tục.

## Deliverable
- Class `AdaptiveSpawnDirector` với API `RequestSpawn(float deltaTime)`.
- Inspector UI hiển thị real-time budget usage.