---
title: "Rollback Netcode"
description: "GGPO principles, input delay vs rollback, implementation notes cho fighting game."
tags:
  - multiplayer
  - networking
updated: 2026-03-11
---

# 🔁 Rollback Netcode (GGPO)

## 1) Khái Niệm
- **Deterministic simulation**: game phải chạy giống nhau giữa các client với cùng input.
- **Input delay**: Trễ cố định (2-4 frame) trước khi apply input để gom gói.
- **Rollback**: Khi nhận input trễ, tua lại state quá khứ → simulate lại → fast-forward.

## 2) Pipeline
1. Mỗi frame client gửi input (buttons, direction) + frame ID.
2. Giả định input của đối thủ (thường là lặp lại input trước đó).
3. Simulate frame local.
4. Khi nhận input thật → so sánh, nếu khác → rollback N frame (copy snapshot) → replay.

## 3) Snapshot & Determinism
- Serialize state nhẹ (position, velocity, timers).
- Dùng fixed timestep, tránh RNG không sync.
- Snapshot pool (ring buffer) lưu ~10-20 frame.

## 4) Config
- **Rollback window**: 6-10 frame (100-166ms ở 60fps).
- **Input delay**: dynamic theo ping (min 1 frame).
- **Prediction**: reuse last input, advanced: training ML.

## 5) Pseudocode

```csharp
void SimulateFrame(int frame)
{
    var myInput = localInputs[frame];
    var remoteInput = remoteInputs.GetOrPredict(frame);
    GameStep(myInput, remoteInput);
}

void OnRemoteInput(int frame, InputPacket pkt)
{
    remoteInputs[frame] = pkt;
    if (frame < currentFrame)
    {
        RollbackTo(frame);
        for (int f = frame; f < currentFrame; f++)
        {
            RestoreSnapshot(f);
            SimulateFrame(f);
        }
    }
}
```

## 6) Tools
- GGPO SDK (C/C++), Fightcade open source.
- Rollback libs: Rollback.NET, Quantum (Photon) hỗ trợ.
- Debug: visualiser hiển thị frame ID, rollback count.

## 7) QA Checklist
- [ ] Deterministic build (no floating RNG, no physics drift).
- [ ] Snapshot size < 2KB (để gửi nhanh).
- [ ] Stress test 200ms ping, packet loss 5%.
- [ ] Logging rollback frequency để tweak window.

## ✅ Apply it
- [ ] Chuyển gameplay sang deterministic fixed update.
- [ ] Implement snapshot serialize/deserialize.
- [ ] Tích hợp prediction + rollback loop.
- [ ] Telemetry: rollback count, input delay per match.
- [ ] Expose netcode options cho player (delay vs rollback).