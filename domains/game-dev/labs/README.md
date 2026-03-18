# 🧪 Game Dev Practical Labs & Challenges

> [← Back to Game Dev Roadmap](../README.md)

Đây không phải là kho Code để bạn copy & paste. Đây là các "Thao trường" (Labs) nhỏ gọn giáp lá cà, nhổ rễ lý thuyết khô khan và biến bạn thành Technical/Gameplay Engineer cứng cáp. Tắt IDE Copilot, và hãy tự cào bàn phím với Unity/Godot.

---

## 🌊 Lab 1: Giải Phẫu Lượng Giác & Vẽ Water Shader Số 0 

Chúng ta sẽ ứng dụng kiến thức tại [Advanced Game Math](../fundamentals/advanced-game-math.md) lồng vào việc học [Tech Art: Shader](../art-tech/graphics/shader-programming.md).

**Mục tiêu:** Tạo cục Mesh 3D hình vuông bình thường. Tác động sức mạnh Lượng giác lượn sóng Y-axis biến nó thành mặt hồ trên Shader Graph (hoặc HLSL). Đừng dùng Animation.

**Các bước (Flowchart nhẩm):**
1. Nhận Time (`Time.time`) truyền vảo Shader biến `$t` .
2. Nhận Local UV (bản đồ X/Y) truyền biến mảng `$uv`.
3. Trong Vert Shader (Vùng thay đổi khung xương hình học đỉnh), Kéo điểm `$y` lên/xuống cắm thức:
   `NewY = sin( $uv.x * TầnSốCơnSóng + $t * TốcĐộ)` 
4. Gắn thêm sự hỗn độn (Nhân chồng thêm 1 sóng `cos` nhỏ bên hông)
   `NewY += cos( $uv.z * 1.5 + $t * 2.0) * BiênĐộRút`
   
**Kết quả Check:** Di chuyển Cube, Mặt nước gợn sóng biển cuồn cuộn không dính 1% CPU xử lý do GPU Gánh 100%. Đạt chuẩn Technical Artist sơ cấp.

---

## 🤖 Lab 2: Máy Trạng Thái Của Siêu Boss (FSM)

Vứt hàng lô `if(Distance < 10) Đánh else if (Máu < 30) Chạy`. Đống rác [Spaghetti code đó](../production/unity-deep-dive/unity-clean-code-solid.md) không bao giờ quản trị Boss Final có 10 Phase và 30 skills.

**Mục tiêu:** Viết C# Base Class (hoặc Resource Godot) cho Pattern State Machine Cơ bản gồm bộ Lõi Vận Hành `(IState Interface: Enter, Execute, Exit)`.

**Bài tập thiết kế State:**
- Boss `IdleState`.
- Nếu Nhìn thấy Player -> Chuyển ngàm cái Cúp máy sang `ChaseState`.
- Nếu máu Boss < 10% ngay giữa lúc rượt (`Exit() chase state lập tức`), Nhấn ga bám máy Tối đa hủ lên trời vào Mode `EnragedState` xả lửa vĩnh cửu.

**Kết quả Check:** Gắn Script vào khối Cube Xanh. Khi Player Cube đỏ lại gần, Cục xanh tự bám theo gắt gỏng, in log màn hình rành mạch `Enemy Transitions [Idle -> Chase]`. Đạt mức Mid-Dev architecture.

---

## 🛠️ Lab 3: Tích Hợp AI "Lính Gác Biết Đau" Local vào Game

Bài test thực chiến cho file [AI-Assisted Game Dev](../production/ai-assisted-gamedev.md). Hầm hầm đưa mô hình Ngôn ngữ Local SLM vô chửi nhau với Player thời gian thực.
*(Đây là Level siêu Khó nhằn dành cho Technical Director tham vọng năm 2026).*

**Yêu cầu môi trường:** Cài Ollama bản Llama-3 local, cắm điện chạy ngầm server ở Port 11434 Máy Mẹ. 

**Code ở Game Engine:**
1. Unity: Tạo Event OnTriggerEnter chọt kiếm vào mông con NPC Lính gác. Viết mã Trừ 20 Máu nó đi.
2. Unity: Xài `UnityWebRequest` nhấc Post Call đâm qua Localhost mạng mẻo của Máy Tính gởi Chuỗi JSON:
   Báo Thức con AI dậy: *"Prompt Hệ Thống: Cậu là lính canh Thành Phố sùng đạo tàn bạo ác ngôn. {Context biến: Cậu vừa bị tao Đâm tụt 20hp Cậu Còn 80%. Đau rát. Vũ Khí thằng trước mặt là Kiếm}. Sổ ra một câu thoại 1 dòng Phản Ứng!"* 
3. Game Đợi JSON Stream Rớt rớt từng chữ qua C# Async/Task Parse Cắm lên UI Bubble Chat lơ lủng trên đầu lính Gác. OẰN! 

**Kết quả check:** Đóng game thành file `Build.exe.`. Mỗi nhát chém lính gác gào xin 1 kiểu khác nhau. Chưa chết thì nhây, mà gần chết quỳ lạy khóc lóc gõ text thảm não nề! 🤯 Đỉnh cao nhập vai!

---

## 🌩️ Senior Engineering Labs (Thách Thức Tối Thượng)

*   **[Lab 4: BaaS Leaderboard & Login (PlayFab) ✨](./lab-baas-leaderboard.md)**
    *   *Nhiệm vụ:* Tích hợp SDK PlayFab, Code Login ẩn danh bằng Device ID, và Bắn điểm/Kéo danh sách Leaderboard Global.
*   **[Lab 5: Tự Build Bằng GitHub Actions (CI/CD) ✨](./lab-unity-github-actions.md)**
    *   *Nhiệm vụ:* Viết file `main.yml` giấu License Unity. Đẩy nhánh `main` là GitHub tự động Build chạy đẻ ra file WebGL.
*   **[Lab 6: Đại Dịch Zombie (Unity DOTS / ECS) ✨](./lab-dots-zombie-swarm.md)**
    *   *Nhiệm vụ:* Tách Data (ComponentData) rời Code (SystemBase). Ép Burst Compile đẩy FPS lên 144 khi spawn 5,000 Zombie.
*   **[Lab 7: AI Sinh Tồn Yếu Sinh Lý (Utility AI) ✨](./lab-utility-ai-sims.md)**
    *   *Nhiệm vụ:* Xây hệ đo não Nông Dân chấm điểm nổi (Đói/Ngủ). Viết code tự so sánh điểm để quẳng Thằng Lố về Giường hoặc Bát Cơm (như The Sims).
*   **[Lab 8: Lắp Ráp Nhện Bò Vách Đá (Procedural IK) ✨](./lab-procedural-spider-ik.md)**
    *   *Nhiệm vụ:* Không dùng Asset Anim. Bắn Laze Raycast xuống gầm địa hình gồ ghề. Ép bằng code Toán học `Lerp` nhấc 4 cẳng chân Nhện bám dính dốc.
