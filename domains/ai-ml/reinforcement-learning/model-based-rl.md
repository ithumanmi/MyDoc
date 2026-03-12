## 🧱 Model-Based Reinforcement Learning

> [← Back to RL Section](./README.md)

Tận dụng mô hình động lực (dynamics model) để planning, data efficiency và tổng hợp dữ liệu ảo.

---

## 1. Kiến trúc tổng quan

```
Environment -> Data Buffer -> Model Learning -> Planning / Policy Learning -> Deployment
```

*   **Model Learning:** học \(p(s_{t+1}|s_t, a_t)\) và \(r(s_t, a_t)\).
*   **Planning:** MPC, shooting method, cross-entropy method (CEM).
*   **Policy Learning:** sử dụng model để sinh rollouts ảo cho policy/value update.

---

## 2. Thuật toán tiêu biểu

| Algorithm | Ý tưởng | Ghi chú |
| --- | --- | --- |
| Dyna-Q | Kết hợp trải nghiệm thật & model-generated | Tabular/linear |
| PILCO | Gaussian Processes làm dynamics model | Data efficiency cao |
| MBPO | Ensemble dynamics + short rollouts cho SAC | Giảm model bias |
| DreamerV3 | World model (recurrent latent) + latent actor-critic | Scalable, image-based |
| MuZero | Học model trong latent space (no explicit dynamics) | Planning bằng MCTS |

---

## 3. MBPO Workflow (ví dụ)

1. Collect real transitions vào replay buffer.
2. Train ensemble dynamics models (probabilistic NN).
3. Generate short-horizon rollouts từ model để augment buffer.
4. Train policy (SAC) trên buffer kết hợp real + imagination data.
5. Update model định kỳ, giới hạn rollout length để tránh drift.

Pseudo-code snippet:

```python
for epoch in range(E):
    real_batch = replay.sample_real()
    model.train(real_batch)

    for _ in range(model_rollouts):
        start_states = replay.sample_states()
        imag_transitions = model.rollout(start_states, horizon=H)
        replay.add_model_data(imag_transitions)

    for _ in range(policy_updates):
        batch = replay.sample_combined()
        sac.update(batch)
```

---

## 4. Planning với MPC + CEM

1. Sample nhiều chuỗi action ngẫu nhiên.
2. Dùng dynamics model dự đoán reward tổng.
3. Chọn top-k sequence, fit distribution (mean/covariance).
4. Lặp vài vòng rồi thực thi action đầu tiên.

```python
def cem_plan(state, model):
    mean, var = init_distribution()
    for _ in range(N_iters):
        actions = sample_actions(mean, var)
        returns = evaluate(model, state, actions)
        elites = select_top(actions, returns, elite_frac=0.1)
        mean, var = fit_gaussian(elites)
    return mean[0]
```

---

## 5. Best Practices

* Ensemble models + uncertainty penalty để giảm overfitting.
* Ngăn rollout quá dài → dùng horizon 1-5 bước (MBPO) hoặc latent imagination (Dreamer).
* Kiểm tra model overfitting bằng validation loss trên hold-out transitions.
* Logging: prediction error, policy reward, model usage ratio.

---

## 6. Resources

* [MBPO Paper](https://arxiv.org/abs/1906.08253)
* [DreamerV3](https://arxiv.org/abs/2301.04104)
* [MuZero](https://arxiv.org/abs/1911.08265)

> 🧠 Tip: Dùng model-based RL để giảm chi phí simulator (robotics, energy) và kết hợp với offline RL để bootstrap chính sách.
