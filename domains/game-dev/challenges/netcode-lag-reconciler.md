# 🌐 Unity Coding Challenge #2 – Netcode Lag Reconciler

## Bối cảnh
Bạn làm game PvP 2.5D (Unity Netcode for GameObjects). Mỗi client gửi input (move, dash, skill) đến server authoritative. Kết nối mạng có thể spike 120ms. Bạn cần cơ chế **client-side prediction + server reconciliation** để character không bị teleport.

## Input
- Input buffer per client: `(tick, inputVector, actionFlags)`.
- Server gửi về state snapshot `(tick, position, velocity)`.
- `MaxRollbackTicks = 8`.

## Yêu cầu
1. Client phải dự đoán chuyển động đến tick hiện tại dựa trên input local.
2. Khi server trả state có tick cũ hơn, client phải rollback tới tick đó, áp dụng state và re-simulate các input sau tick.
3. Phải handle skill dash (tốc độ thay đổi lớn) và knockback từ enemy khác.
4. Giảm jitter bằng cách blend giữa predicted và server state (Lerp hạn chế).
5. Unit test mô phỏng input loss 10% và latency ±50ms.

## Gợi ý
- Dùng circular buffer lưu 16 snapshot.
- ECS/DOTS hoặc MonoBehaviour tùy chọn nhưng cần `FixedUpdate` determinism.
- Cần guard chống replay actions (ví dụ skill đã dùng).

## Deliverable
- Component `LagReconciler` với API `OnServerState(ServerSnapshot snapshot)`.
- Demo scene với 2 client 1 server, hiển thị số lần rollback mỗi phút.