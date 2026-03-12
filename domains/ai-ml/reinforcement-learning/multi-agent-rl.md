## 🤝 Multi-Agent Reinforcement Learning

> [← Back to RL Roadmap](./README.md)

MARL (Multi-Agent RL) cho môi trường nhiều agent tương tác (cooperative, competitive, mixed).

---

## 1. Settings

- **Cooperative:** tất cả agent cùng mục tiêu (VD: multi-robot coordination).
- **Competitive:** zero-sum (VD: game đối kháng).
- **Mixed:** vừa hợp tác vừa cạnh tranh.

Challenge: non-stationarity (policy agent khác thay đổi liên tục).

---

## 2. Centralized Training, Decentralized Execution (CTDE)

Ý tưởng: training dùng thông tin global (state, hành động agent khác), nhưng khi deploy mỗi agent chỉ quan sát local.

Ví dụ: MADDPG (Multi-Agent DDPG) — critic dùng thông tin toàn cục, actor chạy local.

---

## 3. Key Algorithms

| Thuật toán | Mô tả |
| --- | --- |
| **Independent Q-learning** | Mỗi agent tự học, treating agent khác như environment → dễ không ổn định. |
| **COMA** | Counterfactual multi-agent policy gradient với centralized critic. |
| **QMIX** | Value decomposition, tổng hợp Q_i để đảm bảo consistency. |
| **MADDPG** | Actor-critic cho continuous action, centralized critic. |
| **MAPPO** | PPO multi-agent với shared policy hoặc policy riêng. |

---

## 4. Communication & Coordination

- **Parameter sharing:** agents cùng kiến trúc/chung weights.
- **Attention / graph nets:** học message giữa agents.
- **Explicit communication channel:** gửi tín hiệu discrete/continuous.

---

## 5. Evaluation & Benchmarks

- **SMAC (StarCraft Multi-Agent Challenge)**
- **Multi-agent Mujoco / PettingZoo environments**
- **Google Research Football**

Metrics: win rate, episodic reward per agent, cooperation score.

---

## 6. Implementation Tips

- Normalize observation per agent.
- Buffer riêng cho từng agent hoặc shared buffer với tagging.
- Curriculum: bắt đầu ít agent → tăng dần.
- Giới hạn action space để tránh combinatorial explosion.

> 🔍 Tip: Dùng RLlib hoặc PyMARL để tận dụng hạ tầng multi-agent sẵn có (policy mapping, centralized value function).
