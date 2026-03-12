## 📊 Q-Learning & Deep Q-Networks

> [← Back to RL Roadmap](./README.md)

Từ Q-table truyền thống đến DQN, Double DQN và Rainbow.

---

## 1. Q-Learning Basics

Bellman update:

\[ Q_{t+1}(s,a) = Q_t(s,a) + \alpha (r + \gamma \max_{a'} Q_t(s',a') - Q_t(s,a)) \]

Algorithm:

```python
for episode in episodes:
    s = env.reset()
    while not done:
        a = epsilon_greedy(Q, s)
        s', r, done, _ = env.step(a)
        Q[s,a] += alpha * (r + gamma * max(Q[s']) - Q[s,a])
        s = s'
```

> Ưu điểm: đơn giản, áp dụng tốt khi state/action space nhỏ.

---

## 2. Deep Q-Network (DQN)

Nhược điểm Q-table → DQN dùng neural network xấp xỉ \(Q(s,a)\).

Key components:

1. **Experience Replay:** buffer lưu transition (s,a,r,s').
2. **Target Network:** cập nhật chậm để ổn định.
3. **ε-greedy:** exploration.

Loss:

\[ L(\theta) = \mathbb{E}[(r + \gamma \max_{a'} Q_{\theta^-}(s',a') - Q_{\theta}(s,a))^2] \]

---

## 3. Double & Dueling DQN

| Biến thể | Ý tưởng |
| --- | --- |
| **Double DQN** | Tách action selection và evaluation để giảm overestimation. |
| **Dueling DQN** | Mạng tách Value stream & Advantage stream → học tốt hơn khi action không ảnh hưởng nhiều. |

Rainbow = DQN + Double + Dueling + Prioritized Replay + Noisy Nets + C51 + N-step.

---

## 4. Implementation Snippet (PyTorch)

```python
q_net = QNetwork().to(device)
target_net = QNetwork().to(device)
target_net.load_state_dict(q_net.state_dict())
optimizer = torch.optim.Adam(q_net.parameters(), lr=1e-3)

def compute_td_loss(batch):
    states, actions, rewards, next_states, dones = batch
    q_values = q_net(states).gather(1, actions)
    next_q = target_net(next_states).max(1)[0].detach()
    target = rewards + gamma * (1 - dones) * next_q
    loss = F.mse_loss(q_values.squeeze(), target)
    optimizer.zero_grad(); loss.backward(); optimizer.step()
```

> Cập nhật target network mỗi `target_update` steps.

---

## 5. Best Practices

- Normalize / scale observations.
- Gradient clipping để tránh exploding updates.
- Monitor TD error, replay buffer size, ε decay.
- Multi-step returns (n-step) cải thiện learning speed.

---

## 6. When to use

- Environment discrete action space.
- Game (Atari), grid-world, tabular problems.
- Có thể kết hợp với curiosity module cho sparse reward.

> 🎯 Tip: Khi state/action lớn, cân nhắc chuyển sang Actor-Critic (PPO/SAC).
