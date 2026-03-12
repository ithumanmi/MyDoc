## 🧪 Reinforcement Learning Labs & Playbook

> [← Back to AI/ML Roadmap](../README.md)

Chuỗi bài thực hành giúp đưa RL vào production và kết nối với các bài toán thực tế.

---

## Lab 1 — CartPole to PPO (Fundamentals)

| Item | Nội dung |
| --- | --- |
| Goal | Chuyển từ DQN cơ bản sang PPO, giải CartPole, MountainCar. |
| Steps | 1) Train DQN (experience replay) 2) Implement PPO từ CleanRL 3) So sánh learning curve |
| Deliverables | Notebook + chart episodic reward + checklist hyperparameters |

Checklist:
- [ ] Log bằng TensorBoard/Weights & Biases
- [ ] Sweep epsilon vs entropy coefficient
- [ ] Export policy `.pth`

---

## Lab 2 — Continuous Control với SAC

| Item | Nội dung |
| --- | --- |
| Goal | Huấn luyện SAC trên MuJoCo (HalfCheetah, Ant). |
| Steps | 1) Setup mujoco-py 2) Tune replay buffer size, batch size 3) Evaluate deterministic vs stochastic policy |
| Deliverables | Training script + evaluation video GIF + metrics report |

Checklist:
- [ ] Dùng automatic entropy tuning
- [ ] Log critic loss & temperature α
- [ ] Implement checkpoint resume

---

## Lab 3 — Multi-Agent RL (RLlib)

| Item | Nội dung |
| --- | --- |
| Environment | PettingZoo (Pistonball, MPE) |
| Goal | Train multi-agent PPO với Ray RLlib |
| Steps | 1) Define multi-agent config 2) Add centralized critic 3) Evaluate cooperative metrics |
| Deliverables | Config YAML + training logs + ablation report |

Checklist:
- [ ] Parameter sharing vs independent policies
- [ ] Curriculum training
- [ ] Visualization bằng PettingZoo animation

---

## Lab 4 — Offline RL for Recommendation

| Item | Nội dung |
| --- | --- |
| Dataset | Recsys log (bandit feedback) |
| Goal | Train CQL hoặc CRR để học chính sách mới từ batch data |
| Steps | 1) Preprocess logged data (state, action, reward) 2) Train offline RL 3) Counterfactual evaluation (IPS/DR) |
| Deliverables | Notebook + evaluation metrics + deployment plan |

Checklist:
- [ ] Validate support coverage (action overlap)
- [ ] Add constraint để tránh out-of-distribution action
- [ ] Kết hợp simulated A/B trước khi production

---

## Lab 5 — Model-Based RL (MBPO/Dreamer)

| Item | Nội dung |
| --- | --- |
| Goal | Huấn luyện agent model-based dùng ensemble dynamics (MBPO) và latent world model (Dreamer). |
| Steps | 1) Thu thập rollout thật 2) Train dynamics ensemble 3) Sinh short rollouts feed vào SAC 4) (Optional) Huấn luyện DreamerV3 trên environment hình ảnh |
| Deliverables | Notebook + report prediction error + config YAML cho dynamics model |

Checklist:
- [ ] Tune rollout horizon (1-5 bước) để tránh model bias
- [ ] Log uncertainty của ensemble (variance)
- [ ] Benchmark Dreamer vs MBPO về sample efficiency

## Lab 6 — RLHF Mini Pipeline

| Item | Nội dung |
| --- | --- |
| Goal | Xây dựng pipeline preference → reward model → PPO fine-tuning LLM nhỏ |
| Steps | 1) Thu thập cặp câu trả lời 2) Train reward model (pairwise loss) 3) PPO training với TRL 4) Đánh giá human-in-the-loop |
| Deliverables | Dataset JSONL + training scripts + evaluation rubric |

Checklist:
- [ ] Monitor KL divergence
- [ ] Kết hợp rejection sampling
- [ ] Viết guideline cho annotator

> 🚀 Tip: Chuẩn hóa folder structure theo [CV Repo Template](../computer-vision/cv-repo-template.md) để dễ tracking thí nghiệm RL.
