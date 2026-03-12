## 🎯 Policy Gradient & Actor-Critic

> [← Back to RL Roadmap](./README.md)

Từ REINFORCE cơ bản tới PPO hiện đại.

---

## 1. Policy Gradient Objective

Goal: maximize expected return \(J(\theta) = \mathbb{E}_{\pi_{\theta}}[\sum_t \gamma^t r_t]\).

Gradient estimator (REINFORCE):

\[ \nabla_{\theta} J(\theta) = \mathbb{E}[\nabla_{\theta} \log \pi_{\theta}(a_t|s_t) R_t] \]

Vấn đề: variance cao.

---

## 2. Baseline & Advantage

Sử dụng baseline (value function) giảm variance:

\[ \nabla J = \mathbb{E}[\nabla \log \pi (a_t|s_t) (R_t - b(s_t))] \]

Advantage: \(A_t = Q(s_t,a_t) - V(s_t)\) → Generalized Advantage Estimation (GAE) cân bằng bias-variance.

---

## 3. Actor-Critic (A2C/A3C)

* **Actor:** policy network cập nhật bằng policy gradient.
* **Critic:** value network ước lượng V(s).
* **Loss:**
  * Policy loss: \(-\log \pi(a|s) A_t\)
  * Value loss: \((R_t - V(s))^2\)
  * Entropy bonus: khuyến khích exploration.

`A2C`: synchronous; `A3C`: asynchronous workers.

---

## 4. PPO (Proximal Policy Optimization)

Clipped objective giữ update an toàn:

\[ L^{CLIP}(\theta) = \mathbb{E}[\min(r_t(\theta) A_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) A_t)] \]

Trong đó \(r_t(\theta) = \frac{\pi_{\theta}(a_t|s_t)}{\pi_{\theta_{old}}(a_t|s_t)}\).

Workflow:

1. Collect rollout (T timesteps) với policy hiện tại.
2. Tính advantages (GAE) và returns.
3. Optimize nhiều epochs trên mini-batch.
4. KL penalty/clip để tránh update quá xa.

---

## 5. Implementation Notes

- Normalize advantages.
- Shuffle mini-batch cho mỗi epoch.
- Monitor KL, entropy, value loss.
- Dùng `ppo_clip=0.1-0.3`, `gae_lambda=0.95`, `entropy_coef=0.01` (tùy bài toán).

```python
ratio = (new_log_probs - old_log_probs).exp()
clip_adv = torch.clamp(ratio, 1-eps, 1+eps) * advantages
loss = -(torch.min(ratio * advantages, clip_adv)).mean()
loss += value_coef * (returns - value_preds).pow(2).mean()
loss -= entropy_coef * entropy.mean()
```

---

## 6. When to use

- Continuous action spaces (robotics, control).
- Policy cần stochastic (exploration) hoặc constraints.
- Tương thích với distributed rollout (vectorized envs).

> 🧠 Tip: Sử dụng Stable-Baselines3 PPO/A2C để prototyping nhanh, sau đó tinh chỉnh hyperparameter bằng Optuna/W&B Sweeps.
