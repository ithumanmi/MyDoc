## 📁 RL Repo Template — Research to Production

> [← Back to RL Section](./README.md)

Chuẩn hóa cấu trúc dự án RL: từ simulator, training scripts, logging đến deployment/inference.

---

## 1. Directory Structure

```
rl-project/
├── data/
│   ├── raw/
│   ├── processed/
│   └── offline_buffers/
├── envs/
│   ├── custom_env.py
│   └── wrappers/
├── configs/
│   ├── train_cartpole.yaml
│   ├── sac_mujoco.yaml
│   └── dreamer_world.yaml
├── notebooks/
│   └── exploration.ipynb
├── src/
│   ├── agents/
│   │   ├── dqn.py
│   │   ├── ppo.py
│   │   └── sac.py
│   ├── models/   # dynamics model, reward model
│   ├── buffers/
│   ├── trainers/
│   └── utils/
├── scripts/
│   ├── train.py
│   ├── evaluate.py
│   ├── rollout.py
│   └── export_policy.py
├── deployments/
│   ├── docker/
│   │   └── Dockerfile
│   └── inference/
│       └── fastapi_server.py
├── monitoring/
│   ├── wandb_config.yaml
│   └── prometheus/
├── Makefile
├── requirements.txt
└── README.md
```

---

## 2. Config Schema (OmegaConf/YAML)

```yaml
env:
  id: CartPole-v1
  max_steps: 500
agent:
  name: ppo
  policy_hidden: [64, 64]
  value_hidden: [64, 64]
train:
  total_timesteps: 200000
  rollout_workers: 4
  gae_lambda: 0.95
  clip_range: 0.2
  entropy_coef: 0.01
eval:
  episodes: 10
log:
  project: rl-cartpole
  checkpoint_dir: outputs/checkpoints
```

Use Hydra/OmegaConf để override: `python scripts/train.py agent=ppo env=cartpole train.total_timesteps=500000`.

---

## 3. Makefile Targets

```makefile
init:
	python -m venv .venv && .venv\Scripts\pip install -r requirements.txt

train:
	python scripts/train.py +experiment=$(EXP)

eval:
	python scripts/evaluate.py checkpoint=$(CKPT)

rollout:
	python scripts/rollout.py checkpoint=$(CKPT) episodes=5

docker-build:
	docker build -t rl-agent:latest deployments/docker
```

---

## 4. Training Script Skeleton

```python
import hydra
from omegaconf import DictConfig
from rl_project.src.trainers.ppo_trainer import PPOTrainer
from rl_project.src.envs import make_env

@hydra.main(config_path="../configs", config_name="train_cartpole")
def main(cfg: DictConfig):
    env = make_env(cfg.env.id)
    trainer = PPOTrainer(cfg, env)
    trainer.train()
    trainer.save()

if __name__ == "__main__":
    main()
```

---

## 5. Logging & Experiment Tracking

* **Weights & Biases / MLflow:** log episodic reward, success rate, losses.
* **TensorBoard:** scalar, histogram (action distribution), videos.
* **Monitoring folder:** lưu Prometheus exporters (latency inference) khi deploy.

---

## 6. Deployment Blueprint

*   **FastAPI server:** load policy, nhận observation qua REST/WebSocket.
*   **gRPC streaming:** cho robotics / game engine.
*   **Batch evaluation:** script rollout offline logs để regression test.

Example FastAPI snippet:

```python
from fastapi import FastAPI
from rl_project.src.inference import PolicyServer

app = FastAPI()
server = PolicyServer("outputs/checkpoints/best.pth")

@app.post("/act")
def act(obs: list[float]):
    action = server.predict(obs)
    return {"action": action}
```

---

## 7. Data Management

*   `offline_buffers/` lưu replay buffer (npz, hdf5) – dùng cho offline RL.
*   Versioning dataset bằng DVC hoặc LakeFS.
*   Metadata JSONL: environment version, reward shaping, seed.

---

## 8. Templates & References

*   [CleanRL](https://github.com/vwxyzjn/cleanrl) — single-file reference.
*   [RLlib Template](https://docs.ray.io/en/latest/rllib/rllib-training.html) — distributed config.
*   [Dreamer Repo](https://github.com/danijar/dreamerv3) — world model structure.

> 📌 Tip: Đồng bộ cấu trúc này với [CV Repo Template](../computer-vision/cv-repo-template.md) để team ML dùng chung tooling (Makefile, pre-commit, logger).
