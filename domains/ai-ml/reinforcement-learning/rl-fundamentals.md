## 🧭 Reinforcement Learning Fundamentals

> [← Back to RL Roadmap](./README.md)

Hiểu rõ thành phần của bài toán RL, Bellman equations, taxonomy thuật toán và workflow huấn luyện thực tế.

---

## 1. Markov Decision Process

| Thành phần | Mô tả |
| --- | --- |
| **State (S)** | Mô tả tình trạng hiện tại của môi trường. |
| **Action (A)** | Tập hành động agent có thể thực hiện. |
| **Transition (P)** | Xác suất chuyển \(P(s'|s,a)\). |
| **Reward (R)** | Phần thưởng nhận được sau action. |
| **Discount (γ)** | Trọng số reward tương lai (0 < γ ≤ 1). |

Bellman expectation:

\[ V^{\pi}(s) = \mathbb{E}_{a \sim \pi}[R(s,a) + \gamma V^{\pi}(s')] \]

> Goal: học policy \(\pi(a|s)\) tối đa hoá expected return.

---

## 2. Value & Policy Functions

- **State-value:** \(V^{\pi}(s)\).
- **Action-value:** \(Q^{\pi}(s,a)\).
- **Advantage:** \(A^{\pi}(s,a) = Q^{\pi}(s,a) - V^{\pi}(s)\).

Bellman optimality (cho policy tối ưu):

\[ Q^{*}(s,a) = \mathbb{E}[R + \gamma \max_{a'} Q^{*}(s',a')] \]

---

## 3. Taxonomy

* **Value-based:** Q-learning, SARSA, DQN.
* **Policy-based:** REINFORCE, PPO.
* **Actor-Critic:** A2C/A3C, SAC.
* **Model-based:** Dyna-Q, MuZero, MBPO.
* **Offline/Batch RL:** BCQ, CQL, IQL.

---

## 4. Exploration vs Exploitation

- ε-greedy, Boltzmann exploration, UCB.
- Intrinsic motivation (ICM, RND) cho sparse reward.
- Curriculum learning: tăng độ khó môi trường dần.

---

## 5. Training Workflow

1. **Environment:** Gymnasium, Isaac Gym, MetaWorld.
2. **Agent:** định nghĩa policy/value network (MLP/CNN/Transformer).
3. **Experience:** rollout, replay buffer (value-based) hoặc trajectory buffer (policy-based).
4. **Optimization:** tính loss (TD error, policy gradient) + regularization (entropy, KL).
5. **Evaluation:** deterministic rollout, log reward, success rate.
6. **Deployment:** xuất policy weights, wrap API/simulator integration.

Monitoring metrics:

- Episode reward, moving average.
- KL divergence (PPO), entropy.
- Critic/TD loss, value function drift.

---

## 6. Tooling & Frameworks

- **Stable-Baselines3**: DQN/PPO/SAC ready-to-run.
- **RLlib (Ray)**: distributed training, multi-agent.
- **CleanRL**: single-file reference implementation.
- **Weights & Biases / MLflow**: log metrics, videos.

---

## 7. RLHF Snapshot

1. Thu thập preference data (cặp response tốt/xấu).
2. Train reward model (RM).
3. Fine-tune policy với PPO + KL penalty so với model gốc.
4. Đánh giá (auto eval + human eval) → iterate.

> 🧠 Tip: Đảm bảo logging state/action/reward đầy đủ để debug và audit khi RL chạy trên sản phẩm thực.
