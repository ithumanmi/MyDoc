# 🌐 Game Server & Multiplayer Architecture: A Deep Dive

> [← Back to Game Dev Roadmap](./README.md) | [Home](../../README.md)

Tài liệu chuyên sâu về kiến trúc Multiplayer, lập trình Game Server và DevOps dành cho Game Developers.

---

## 🏗️ 1. Multiplayer Architecture Overview

Hiểu đúng kiến trúc là bước đầu tiên để không phải đập đi xây lại khi game có >100 người chơi.

### 1.1. Network Topologies

| Mô hình | Mô tả | Ưu điểm | Nhược điểm | Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Peer-to-Peer (P2P)** | Các client kết nối trực tiếp với nhau (Mesh). Một người làm Host. | 💸 **Rẻ tiền** (Không tốn server). <br> ⚡ Latency thấp nếu người chơi ở gần. | 🛡️ **Dễ Hack** (Host toàn quyền). <br> 🔌 NAT Traversal phức tạp. <br> ❌ Host out = Game sập (Host Migration khó). | Game đối kháng 1vs1, Coop LAN (Stardew Valley). |
| **Dedicated Server** | Server chạy độc lập trên Cloud/VPS. Clients chỉ gửi input và nhận state. | 🛡️ **Anti-cheat tốt nhất** (Server là trọng tài). <br> 🌍 Ổn định, công bằng. <br> 📈 Dễ scale. | 💰 **Tốn kém** (Thuê VPS/Cloud). <br> 🛠️ Dev phức tạp hơn (Build headless). | FPS (CS:GO, Valorant), MOBA (LoL), Battle Royale. |
| **Listen Server** | Một người chơi vừa chơi vừa làm Server. | 💸 Tiết kiệm chi phí Server. <br> 🛠️ Dễ setup hơn Dedicated. | ⚖️ Host có lợi thế (0 latency). <br> ❌ Host out = Game sập. <br> 🛡️ Host có thể cheat. | Among Us, Minecraft (LAN), Call of Duty (Older versions). |

### 1.2. State Management Strategies

#### **Authoritative Server (Server là Cha)**
*   **Nguyên tắc:** Client là "dumb terminal". Client chỉ gửi Input (`MoveForward`, `Shoot`). Server tính toán Physics, Logic, Máu, Vị trí rồi gửi kết quả về.
*   **Ví dụ:**
    1. Client A: Bấm nút bắn.
    2. Client A -> Server: "Tao bắn hướng (1,0,0)".
    3. Server: Kiểm tra súng có đạn không? Cooldown chưa?
    4. Server: Raycast thấy trúng Enemy B. Trừ máu B.
    5. Server -> All Clients: "A bắn trúng B, B mất 50 máu".
*   **Tại sao:** Chống hack Speed, Teleport, Aim bot (một phần).

#### **Client-side Prediction (Dự đoán)**
*   **Vấn đề:** Nếu đợi Server trả lời, game sẽ bị delay (bấm nút -> 200ms sau mới chạy).
*   **Giải pháp:** Client bấm nút -> Di chuyển nhân vật **ngay lập tức**. Đồng thời gửi Input lên Server.
*   **Reconciliation:** Khi Server trả kết quả về:
    *   Nếu khớp: Tuyệt vời.
    *   Nếu lệch (do lag/hack): Client phải giật (snap) nhân vật về vị trí Server bảo.

---

## ⚙️ 2. Core Concepts (Chi tiết)

### 2.1. Network Transport: UDP vs TCP

| Protocol | Đặc điểm | Tại sao dùng trong Game? |
| :--- | :--- | :--- |
| **TCP** | ✅ Đảm bảo thứ tự. <br> ✅ Không mất gói tin (Retransmit). <br> ❌ Chậm (Handshake, Ack). | Chat, Login, Inventory, Shop, Leaderboard (Meta-game). |
| **UDP** | ❌ Không đảm bảo thứ tự. <br> ❌ Có thể mất gói tin. <br> ✅ **Cực nhanh** (Fire and Forget). | **Gameplay Realtime:** Di chuyển, Bắn súng. <br> *Mất gói tin vị trí cũ không sao, vì gói tin mới sẽ đè lên.* |

> **Lưu ý:** Các thư viện như Unity Netcode/Mirror thường xây dựng một lớp **Reliable UDP** (RUDP) trên nền UDP để gửi các tin quan trọng (Spawn object, Game Start) mà vẫn nhanh hơn TCP.

### 2.2. Serialization
Dữ liệu trong RAM (Object) ➡️ Bytes ➡️ Mạng ➡️ Bytes ➡️ Object.

*   **Không dùng JSON** cho Gameplay packet vì quá nặng (String overhead).
*   **Dùng Binary:** Bit packing.
    *   Vd: Bool chỉ tốn 1 bit. Float tốn 4 bytes.
    *   Compress: Gửi `Rotation` (Quaternion) chỉ cần 3 float (bỏ w) hoặc nén thành 1 integer.

### 2.3. Latency Compensation (Bù Lag)

#### **Interpolation (Nội suy - Cho người khác)**
*   Bạn thấy đối thủ di chuyển mượt mà dù gói tin chỉ đến 10 lần/giây.
*   **Cách làm:** Client hiển thị đối thủ ở **quá khứ** (vd: 100ms trước). Client nội suy tuyến tính (Lerp) giữa Snapshot A (t=0) và Snapshot B (t=0.1).
*   *Kết quả:* Mượt mà nhưng vị trí hiển thị trễ hơn thực tế một chút.

#### **Lag Compensation (Server Rewind - Cho việc bắn súng)**
*   Vấn đề: Bạn bắn trúng đầu địch trên màn hình của bạn, nhưng Server bảo trượt vì địch đã chạy qua chỗ khác rồi.
*   **Giải pháp:**
    1. Client gửi: "Tao bắn lúc `timestamp = 1000`".
    2. Server nhận được lúc `timestamp = 1200`.
    3. Server: "Ok, tao sẽ tua ngược (rewind) hitbox của tất cả player về thời điểm 1000".
    4. Server Raycast kiểm tra va chạm.
    5. Server tua lại hiện tại.

### 2.4. RPC (Remote Procedure Call)
Gọi hàm trên máy khác.

*   `ServerRpc`: Client gọi -> Chạy trên Server. (Vd: `RequestSpawnUnit`)
*   `ClientRpc`: Server gọi -> Chạy trên Client. (Vd: `PlayExplosionEffect`)

### 2.5. Network Ownership
*   Mỗi Object (Player, Bullet) phải có 1 Owner.
*   Owner có quyền gửi update `Transform` lên Server (nếu Server tin tưởng) hoặc gửi Input.
*   Server có thể thay đổi Owner (vd: Nhặt súng -> Súng thuộc về Player).

---

## 🏗️ 3. Game Server Architecture

### 3.1. Dedicated Server Setup
*   **Headless Build:** Unity Build Setting -> Server Build (No Graphics, No Audio). Chạy nhẹ, tiết kiệm RAM.
*   **Docker:** Đóng gói Server build vào Docker Image.
    ```dockerfile
    FROM ubuntu:20.04
    COPY ./Build/LinuxServer /app
    WORKDIR /app
    ENTRYPOINT ["./MyGameServer.x86_64", "-batchmode", "-nographics"]
    ```

### 3.2. Matchmaking System
Không chỉ là "tìm đại 1 phòng".
1.  **Ticket:** Player gửi request "Tìm trận" -> nhận về Ticket ID.
2.  **Queue:** Server xếp Ticket vào hàng đợi (Redis).
3.  **Matcher:** Worker quét Queue, gom nhóm theo tiêu chí (Elo rating, Region, Ping).
4.  **Allocation:** Matcher gọi Game Server Manager -> Spin up một Docker container mới.
5.  **Response:** Gửi IP + Port của Server mới cho các Players.

### 3.3. Anti-Cheat Architectures
*   **Authoritative Physics:** Server chạy physics simulation y hệt Client. Nếu Client bay xuyên tường -> Server teleport ngược lại (Rubber banding).
*   **Sanity Check:**
    *   Speed Hack: `distance / time > max_speed`?
    *   Rate Limit: Bắn 10 viên/giây trong khi súng chỉ bắn được 5?
*   **Obfuscation:** Mã hóa gói tin UDP để tránh Man-in-the-middle attack.

---

## 🎮 4. Thực hành Projects (Roadmap)

### 🟢 Project 1: Simple Chat Room & Lobby
*Mục tiêu: Hiểu RPC, Connection flow, UI Sync.*
1.  **Setup:** Unity + Netcode for GameObjects (NGO).
2.  **Connection:** Tạo nút "Host", "Client".
3.  **Lobby:** Hiển thị danh sách người chơi trong phòng.
4.  **Chat:** Input Field -> `ServerRpc(message)` -> Server broadcast `ClientRpc(message)` -> Update UI.
5.  **NetworkVariable:** Đồng bộ biến `IsReady` (Bool) cho từng player.

### 🟡 Project 2: Tank Battle (Top-down)
*Mục tiêu: Movement Prediction, Transform Sync.*
1.  **Movement:** Dùng `ClientNetworkTransform`.
2.  **Shooting:** Spawn Bullet Prefab (NetworkObject).
3.  **HP System:** `NetworkVariable<int> Health`. Khi về 0 -> Despawn.
4.  **Physics:** Xử lý va chạm trên Server (`OnCollisionEnter` chỉ chạy trên Server).

### 🔴 Project 3: Battle Royale Mini (Advanced)
*Mục tiêu: Lag Compensation, Optimization, Dedicated Server.*
1.  **Lag Comp:** Tự viết logic Rewind Hitbox (không dùng Collider mặc định).
2.  **Loot System:** Spawn vật phẩm random trên Server. Client nhặt -> Server update inventory.
3.  **Zone:** Vòng bo thu hẹp (Sync bán kính vòng bo).
4.  **Build & Deploy:** Build Linux Server, chạy thử trên máy ảo (WSL/VPS).

---

## 🚀 5. Production & DevOps

### 5.1. Hosting Options

| Option | Chi phí | Độ khó | Phù hợp cho |
| :--- | :--- | :--- | :--- |
| **Self-hosted VPS** (DigitalOcean/Linode) | $5 - $20/tháng | ⭐⭐⭐⭐ (Cần biết Linux, Docker) | Hobby Project, Test. |
| **AWS GameLift / Azure PlayFab** | Pay as you go (Đắt) | ⭐⭐⭐ (Document nhiều) | Game thương mại, Scale toàn cầu. |
| **Agones (K8s)** | Rẻ nếu scale lớn | ⭐⭐⭐⭐⭐ (Cần Master K8s) | Enterprise Studio (Ubisoft, EA). |
| **Unity Gaming Services (UGS)** | Free tier hào phóng | ⭐⭐ (Tích hợp sẵn Unity) | Indie Dev, Prototyping. |

### 5.2. Monitoring & Observability
Server game là "hộp đen". Cần đèn pin để soi.
*   **Logs:** Đẩy log từ Unity (`Debug.Log`) ra file hoặc dịch vụ log (ELK Stack, Loki).
*   **Metrics:**
    *   **CCU:** Concurrent Users.
    *   **CPU/RAM Usage:** Server có bị leak memory không?
    *   **Tick Rate:** Server có duy trì được 60Hz không hay bị tụt xuống 20Hz (Lag)?
    *   **Network In/Out:** Băng thông tiêu thụ.

### 5.3. CI/CD Pipeline (GitHub Actions)
Tự động hóa quy trình build.
```yaml
name: Build Server
on:
  push:
    branches: [ "main" ]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build Unity Server
        uses: game-ci/unity-builder@v2
        with:
          targetPlatform: StandaloneLinux64
          buildName: MyGameServer
      - name: Push to Docker Hub
        run: |
          docker build . -t myrepo/gameserver:latest
          docker push myrepo/gameserver:latest
```

---

## 📚 Resources

### Documentation
*   [Unity Netcode for GameObjects](https://docs-multiplayer.unity3d.com/)
*   [Mirror Networking Wiki](https://mirror-networking.gitbook.io/docs)
*   [Agones Documentation](https://agones.dev/site/docs/)

### Books
*   *"Multiplayer Game Programming"* - Joshua Glazer & Sanjay Madhav.
*   *"Development and Deployment of Multiplayer Online Games"* - Volkan Ilbeyli.

### Channels
*   **Dapper Dino:** Tutorials chi tiết về Mirror/NGO.
*   **GDC Talks:** Tìm các bài nói chuyện của Overwatch/Halo developers về Networking.
