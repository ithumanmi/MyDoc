# Challenge: Networked Co-op Mini Game

- **Loại:** project
- **Mảng:** game-dev
- **Mức:** Intermediate
- **Ước lượng thời gian:** 3-5 ngày
- **Prerequisites (tùy chọn):** Kiến thức cơ bản networking game (client/server, lag compensation), engine hỗ trợ netcode (Unity Netcode/Photon/Mirror; Unreal replication; Godot multiplayer).

## Mục tiêu học tập
- Xây dựng game co-op đơn giản với state sync ổn định, xử lý latency cơ bản.
- Thiết kế kiến trúc client/server và event/state replication.
- Thử nghiệm lag compensation/ interpolation để giảm jitter.

## Đề bài
Tạo một mini-game co-op 2-4 người (vd: thu thập vật phẩm, đẩy box puzzle, hoặc wave defense) với yêu cầu:
- **Kết nối & phòng:** Tạo/join room; hiển thị danh sách player trong phòng.
- **State sync:** vị trí/animation/state entity được sync; dùng snapshot + interpolation hoặc command queue.
- **Latency handling:** đơn giản hoá: client-side prediction cho di chuyển; reconciliation khi nhận state server.
- **Gameplay loop:** 1-2 mục tiêu phối hợp (vd: phải cùng đứng trên 2 nút để mở cửa; hoặc hợp tác đẩy vật nặng).

## Đầu vào (Input)
- Asset basic hoặc primitive shapes.

## Đầu ra (Output)
- Build chơi được (2+ client) + hướng dẫn chạy host/join.
- README: kiến trúc netcode (client/server, replication), thông số tick/snapshot, giới hạn đã thử.

## Tiêu chí chấm (Acceptance)
- Join/leave phòng ổn định; sync state không “teleport” quá nhiều ở latency 80-120ms.
- Prediction/reconciliation hoạt động cho di chuyển; jitter giảm nhờ interpolation.
- Gameplay mục tiêu rõ, có thể hoàn thành co-op; xử lý disconnect cơ bản (timeout). 
- Log hoặc metric đơn giản (tick rate, snapshot rate) để debug.

## Gợi ý / Hint
- Tick rate 20-30 Hz cho prototype; snapshot 10-20 Hz; lerp/interp giữa snapshot.
- Ưu tiên UDP (nếu engine hỗ trợ); nếu dùng WebRTC/WebSocket, chấp nhận thêm latency.
- Giới hạn authority: server giữ state nguồn; client prediction chỉ cho input di chuyển.

## Reference / Solution (tùy chọn)
- Gaffer on Games netcode: https://gafferongames.com/
- Valve networking guide: https://developer.valvesoftware.com/wiki/Source_Multiplayer_Networking
- Unity Netcode sample: https://github.com/Unity-Technologies/com.unity.netcode.gameobjects.samples