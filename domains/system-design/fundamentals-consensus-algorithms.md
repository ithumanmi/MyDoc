# Thuật Toán Đồng Thuận (Consensus Algorithms)

> [← Back to System Design Index](./README.md)

Trong một hệ thống đơn lẻ (1 Server), nếu Máy chủ báo `X = 5`, thì `X` chắc chắn bằng `5`. Lập trình rất yên bình.

Nhưng trong **Hệ thống phân tán (Distributed System)**, nếu bạn có 5 Server ở 5 quốc gia khác nhau.
*   Server A: `X = 5`
*   Server B: `X = 8` (Do mới nhận Request từ khu vực Châu Á)
*   Server C: *Rớt mạng không thể kết nối*

Vậy cuối cùng `X` bằng mấy? Làm sao để 5 Server này "đồng thuận" ra 1 con số duy nhất trước khi trả kết quả cho người dùng? Chào mừng đến với **Consensus Algorithms (Thuật toán Đồng Thuận)**.

---

## 🗳️ 1. Split-Brain Problem (Hội Chứng Não Lưỡng Phân)

Nguyên tắc tối thượng: Một hệ thống có `N` máy chủ sẽ cần **Quorum** (Số phiếu quá bán) để đưa ra quyết định hợp lệ. Công thức: `Quorum = (N / 2) + 1`.

*Vì sao không bao giờ thiết lập cụm (Cluster) 2 hoặc 4 Server? Mà luôn là số lẻ 3, 5, 7?*
> Vì nếu có 4 Server (Mạng bị đứt gãy làm đôi, mỗi bên có 2 Server). Cả 2 bên đều tưởng bên kia chết, tự bầu mình lên làm Node Chủ (Leader / Master). Database của bạn sẽ bị rách làm hai nửa ghi đè lẫn nhau dữ dội (Split-brain). 
> Nếu là 5 Server, đứt mạng 1 bên 2 và 1 bên 3. Nhóm 3 (Quá bán) sẽ tiếp quản quyền lực, nhóm 2 tự động ngắt ghi dữ liệu (Read-only) bảo vệ toàn vẹn Data.

---

## 🛳️ 2. RAFT Algorithm (Đóng Thuyền Vượt Biển Quản Trị)

Raft là thuật toán dễ hiểu nhất, thống trị lõi của các dịch vụ như **etcd (Trái tim của Kubernetes)** hay **Consul**. 

Mọi Server trong Raft luôn ở 1 trong 3 trạng thái: `Follower`, `Candidate`, hoặc `Leader`.

### A. Leader Election (Bầu Cử Lãnh Đạo)
1.  Khởi đầu, cả 3 Server đều là *Followers*. Mỗi Server có một bộ đếm lùi thời gian ngẫu nhiên (vd: 150ms - 300ms).
2.  Server nào đếm lùi về 0 trước, tự động biến thành *Candidate* và hô to: *"Bầu cho tôi đi!"* (Gửi RequestVote RPC cho 2 Server kia).
3.  2 Server kia (do chưa đếm xong) đành ngoan ngoãn Vote "Đồng ý". 
4.  *Candidate* gom đủ 2/3 phiếu -> Lên làm **Lãnh Đạo (Leader)**. Nó bắt đầu bắn luồng tim đều đặn (Heartbeats) cho đàn em biết mình còn sống.

### B. Log Replication (Sao Chép Sổ Xố)
Bây giờ, mọi Request (Ví dụ: `SET X=5`) từ Client đều PHẢI gửi qua Leader. Đàn em không nhận.
1. Leader nhận `X=5`, ghi tạm thời vào file Log nội bộ rỗng (Uncommitted).
2. Leader phát loa: *"Ghi X=5 vào nhé Followers"*.
3. Followers ghi tạm, rồi gửi thư "Dạ Vâng" (Acknowledge) về cho Leader.
4. Leader nhận được phần Đa Số (Quorum) phiếu "Dạ Vâng", nó mới chính thức chốt (Commit) `X=5` vào Database và báo cho Client *"Ghi Thành Công"*. Xong xuôi nó nhắc lại đàn em: "Tao Commit Mốc Đó Rồi, Tụi Bay Commit Vững Vào Đi!". An Tâm Tuyệt Đối!

---

## 🎭 3. Cựu Binh PAXOS 

Trước thời kỳ Raft nắm trùm thế giới, **Paxos** là Vua. (Viết bởi siêu trí tuệ Leslie Lamport).
*   Chuyên biệt cho các hệ thống như **ZooKeeper (Kafka Cục Lõi)**, Google Spanner.
*   **Điểm Khác:** Paxos không có Leader cố định Cứng. Mọi Node đều có thể đứng lên đề xuất (Propose) 1 Giá trị. Các Node sẽ đàm phán 2 Vòng Nhận Diện (Phase 1: Chuẩn Bị, Phase 2: Chấp Cập) lắt léo như Hợp đồng Luật Sư.

**Ứng dụng vào System Design Interview:**
Chức Khảo Cứu: Nhắc đến **Raft** ngay khi người phỏng vấn hỏi: *"Làm sao nếu Service Registry Của Anh Crash Thắng Hệ Không Phân Quyền?"* -> *"Tôi Sẽ Đóng Container Lõi Thành Cụm 3 Node Chạy Thuật Raft Phán Quyết! Giống Như Mạng Cơ Tim Đảm Bảo High Availability Bất Khả Chết Khúc Data!"* 💯
