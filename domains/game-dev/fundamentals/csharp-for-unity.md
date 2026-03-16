---
title: "C# for Unity"
description: "Ôn tập nhanh C# hiện đại và pattern thường gặp khi viết gameplay code."
tags:
  - csharp
  - unity
  - fundamentals
updated: 2026-03-16
---

# ⚙️ C# for Unity - Rapid Refresher

> **Use case:** Dành cho lập trình viên chuyển từ JS/Python sang Unity hoặc designer muốn script nhẹ. Mọi ví dụ đều tương thích Unity 2021-2023 LTS.

## 1. Language Basics You Must Know
- **Value vs Reference type:** `struct` (Value) phù hợp data nhỏ, `class` dùng cho entity phức tạp.
- **Properties:** dùng getter/setter để expose stat an toàn.
  ```csharp
  public class CharacterStats : MonoBehaviour
  {
      [SerializeField] private int baseHp = 100;
      public int CurrentHp { get; private set; }

      void Awake() => CurrentHp = baseHp;
      public void ApplyDamage(int dmg) => CurrentHp = Mathf.Max(0, CurrentHp - dmg);
  }
  ```
- **Events & Delegates:** dùng `Action`, `Func`, `event` để decouple UI ↔ gameplay.
  ```csharp
  public static class GameEvents
  {
      public static event Action<int> OnScoreChanged;
      public static void RaiseScore(int score) => OnScoreChanged?.Invoke(score);
  }
  ```

## 2. Unity-friendly Patterns
- **Dependency Injection light:** truyền reference qua inspector hoặc constructor khi dùng `ScriptableObject`.
- **ScriptableObject Architecture:** dùng để lưu config, event channel, database.
- **State Pattern:** `IState` interface + `StateMachine` giúp nhân vật clear logic.
- **Object Pooling:** tránh `Instantiate/Destroy` liên tục.

## 3. Collections & Jobs
- `List<T>`, `Dictionary<TKey, TValue>` → đừng lạm dụng `FindObjectOfType`.
- `Span<T>` không có trong Unity runtime, stick với array pooling nếu cần.
- `Unity.Collections` + `Burst` khi bước sang DOTS hoặc jobs.

## 4. Async Patterns
- `Coroutines`: `StartCoroutine` cho timer, sequence.
- `async/await` (C# 7.3+) có thể dùng trong editor tool hoặc networking; tránh gọi `await` trong `Update`.
- `UniTask`/`Addressables` async API giúp load asset không block main thread.

## 5. Testing Mindset
- Extract logic vào `plain C# class` để viết NUnit tests.
- Dùng `Assembly Definition` để chia module + giảm thời gian compile.

## 🔗 Further Learning
- [Unity Learn – C# Survival Guide](https://learn.unity.com/course/complete-c-c-survival-guide)
- [Game Programming Patterns](https://gameprogrammingpatterns.com/) (Áp dụng trực tiếp vào C#).
- [Odin Inspector / Zenject Docs] – nếu team dùng tool này.

> **Next step:** Quay lại [Unity Fundamentals](./unity-fundamentals.md) và chọn sprint luyện tập 14 ngày.