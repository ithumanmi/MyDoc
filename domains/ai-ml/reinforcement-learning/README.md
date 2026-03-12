## 🕹️ Reinforcement Learning Roadmap

> [← Back to AI/ML](../README.md)

Lộ trình RL từ cơ bản (MDP) tới các kỹ thuật nâng cao (policy gradient, multi-agent, RLHF).

---

### 1. Fundamentals & Workflow
*   **[RL Fundamentals](./rl-fundamentals.md):** MDP, value/policy functions, Bellman equations và workflow train PPO/DQN.
*   **[Model-Based RL](./model-based-rl.md):** Học dynamics model, planning (MPC/CEM), MBPO, Dreamer, MuZero.

### 2. Algorithms
*   **[Q-Learning & DQN](./q-learning.md):** Q-table, Deep Q-Network, Double/ Dueling DQN, Rainbow.
*   **[Policy Gradient & Actor-Critic](./policy-gradient.md):** REINFORCE, A2C/A3C, PPO, GAE, entropy regularization.
*   **[Multi-Agent RL](./multi-agent-rl.md):** Cooperative vs competitive, centralized training decentralized execution (CTDE).

### 3. Applications & Labs
*   **[RL Applications](./rl-applications.md):** Game AI, robotics control, recommendation, RLHF cho LLM.
*   **[RL Labs & Playbook](./rl-labs.md):** Chuỗi project CartPole → PPO, SAC, multi-agent với RLlib.
*   **[RL Repo Template](./rl-repo-template.md):** Cấu trúc repo chuẩn (configs, training scripts, deployment, monitoring).

> 📌 Tip: Bắt đầu với môi trường Gymnasium đơn giản, log reward/episode bằng W&B, sau đó mở rộng sang simulator phức tạp.
