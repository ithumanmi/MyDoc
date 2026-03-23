---
title: "Unity Testing Architecture & Automation"
description: "Chiến lược Unit/Edit/PlayMode tests, golden recording, CI matrix cho dự án Unity 2026."
tags:
  - testing
  - automation
  - unity
updated: 2026-03-23
---

# 🧪 Unity Testing Architecture & Automation

> **Goal:** Thiết lập pipeline test tự động cho gameplay/system Unity, đảm bảo regression được bắt sớm và chạy được trong CI headless.
> **Deliverables:** Test plan (unit/edit/play), golden recording suite, CI pipeline matrix.
> **Success Criteria:**
> - ≥70% gameplay logic chạy được Unit/Edit mode tests.
> - PlayMode smoke suite < 10 phút.
> - Golden recording cho mechanic quan trọng.
> - CI báo đỏ nếu asset missing, perf regression.

## 1. Test Pyramid cho Unity

| Layer | Scope | Tools |
|-------|-------|-------|
| Unit | Pure C# logic (combat calc, economy) | NUnit, `Playmode=false` |
| Edit Mode | ScriptableObject, editor tooling, serialization | Unity Test Runner (EditMode) |
| Play Mode | Integration of systems (movement, UI, netcode) | PlayMode tests/headless |
| Golden Recording | Input replay + visual diff | Custom harness + snapshots |

### Tips
- Extract logic khỏi MonoBehaviour (use `Context` classes) để dễ unit test.
- Use dependency injection (Zenject) để swap stub/mock.

## 2. PlayMode Architecture

### 2.1 Scene Harness
- Create `Tests/PlayMode/Scenes/TestHarness.unity` bao gồm systems cần test.
- Use `TestPlayer` prefab (input driver) + `TestCamera` lock.

### 2.2 Input Simulation
- Use `InputTestFixture` (Input System) hoặc Custom `IInputProvider`.
- Record sequences (JSON) → feed to tests.

### 2.3 Assertions
- `Assert.That(player.transform.position, Is.EqualTo(expected).Within(0.1f))`
- Use `WaitForSecondsRealtime` thay vì `yield return null` trong tests.
- Validate UI text via `TMP_Text.text`.

## 3. Golden Recording

### 3.1 Purpose
- Capture deterministic input + output (position, HP, UI) để detect regression (animation, physics, netcode).

### 3.2 Implementation steps
1. **Record Mode:** log input + key state per frame → JSON.
2. **Replay Mode:** feed input, capture metrics (position, animation state).
3. **Compare:** use tolerance (float) + hash screenshot.

### 3.3 Tooling
- Use `RecorderController` + `RenderTexture` snapshot.
- Save baseline in `Assets/Tests/GoldenRecordings/`.
- Build diff reporter (HTML) to review mismatches.

## 4. CI Pipeline

### 4.1 Matrix
| Job | Platform | Tests |
|-----|----------|-------|
| Unit | Windows/Linux | `-runTests -testPlatform editmode` |
| PlayMode Smoke | Windows | `-runTests -testPlatform playmode -testResults` |
| Golden | Windows (GPU) | Custom CLI run, upload snapshots |
| Performance | Windows | Run `PerformanceTests.dll`, output JSON |

### 4.2 Command example
```
Unity.exe -batchmode -projectPath . -runTests -testPlatform playmode \
 -testResults ./TestResults/playmode.xml -logFile ./Logs/playmode.log
```

### 4.3 Fail conditions
- Any test fail.
- Golden diff > threshold.
- Performance metrics deviates > 10%.

## 5. Load & Netcode Testing
- Use `Headless` build to spawn multiple clients (Docker Compose) hitting local server.
- Use `Unity.Multiplayer.PlaymodeTests` or custom harness to spawn 8 bots.
- Capture metrics: RTT, packet loss, CPU.

## 6. Tooling & Packages
- `com.unity.test-framework` latest.
- `com.unity.testtools.graphics` for screenshot comparison.
- `Unity Performance Testing` package for perf KPIs.

## 7. Checklist
- [ ] Unit tests cover combat calculator, inventory transactions.
- [ ] Edit mode tests validate ScriptableObject schema.
- [ ] PlayMode tests cover movement, UI flow, quest progression.
- [ ] Golden recording baseline captured + validated.
- [ ] CI pipeline configured, artifacts stored (XML, screenshots).
- [ ] Telemetry from tests (fps, memory) uploaded to metrics sheet.

## 🔗 References
- [Testing Hub](./README.md)
- [Unity Impact Metrics](../production/metrics/unity-impact-metrics.md)