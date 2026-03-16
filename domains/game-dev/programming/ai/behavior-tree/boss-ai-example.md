# 👹 Boss AI Example: The Dark Knight

> [← Back to Behavior Tree Fundamentals](./core-concepts.md)

Hãy áp dụng hệ thống vừa viết để tạo một con Boss "Dark Knight" với 3 Phase chiến đấu.

---

## 1. Thiết kế Blackboard (Bộ nhớ của Boss)

Blackboard chứa dữ liệu dùng chung cho cả cây.

```csharp
public class Blackboard {
    public Transform player;
    public float hp;
    public float enrageThreshold = 50f; // 50% máu
    public bool isStunned;
}
```

---

## 2. Cấu trúc Cây (Tree Structure)

*   **Root (Selector)**
    *   **Phase 3: Desperate (Sequence)**
        *   Cond: `HP < 20%`
        *   Action: `SpinAttack` (Xoay kiếm liên tục)
    *   **Phase 2: Enrage (Sequence)**
        *   Cond: `HP < 50%`
        *   **Selector (Combat Logic)**
            *   Seq: `SummonMinions` (Nếu chưa gọi)
            *   Seq: `JumpAttack` (Nhảy bổ vào player)
    *   **Phase 1: Normal (Sequence)**
        *   Cond: `SeePlayer?`
        *   **Selector**
            *   Seq: `Distance < 2m` -> `MeleeAttack`
            *   Seq: `Distance > 2m` -> `Chase`
    *   **Idle (Sequence)**
        *   Action: `Patrol` (Đi tuần quanh phòng)

---

## 3. Implement Custom Nodes

### **A. Condition: HP Check**
```csharp
public class CheckHP : Node {
    public float threshold;
    public override NodeState Evaluate() {
        if (blackboard.hp < threshold) return NodeState.Success;
        return NodeState.Failure;
    }
}
```

### **B. Action: Summon Minions**
```csharp
public class TaskSummon : Node {
    bool hasSummoned = false;
    public override NodeState Evaluate() {
        if (hasSummoned) return NodeState.Failure; // Đã gọi rồi thì thôi
        
        animator.Play("Summon");
        SpawnMinions();
        hasSummoned = true;
        return NodeState.Success;
    }
}
```

---

## 4. Tinh chỉnh (Tuning)

AI hay không nằm ở việc tinh chỉnh các tham số:
*   **Cooldown:** Thêm Decorator `Cooldown` vào `JumpAttack` để Boss không nhảy liên tục (trông rất ngáo).
*   **Random:** Dùng Selector `RandomSelector` để Boss lúc thì chém trái, lúc thì chém phải (khó đoán).
*   **Telegraphing:** Trước khi đánh mạnh, Boss cần có animation "gồng" (Warning) để người chơi kịp né.
