---
title: "Ragdoll Systems"
description: "Active ragdoll, partial ragdoll, blending with animation."
tags:
  - physics
  - unity
  - ragdoll
updated: 2026-03-11
---

# 🪆 Ragdoll Systems

## 1) Goals
- Ragdoll chuyển mượt từ anim → physics, không glitch/đơ.
- Active/partial ragdoll cho hit-react, stun, death đa dạng.

## 2) Setup
- Rigidbody trên từng bone (chest, arms, legs); Capsule collider phù hợp orientation.
- Joints: ConfigurableJoint với limit (swing/twist) gần giải phẫu; drive spring/damper để ổn định.
- Mass distribution: tổng mass trùng nhân vật; center of mass gần pelvis.

## 3) Active Ragdoll
- Điều khiển joint drive để đuổi theo pose animation (target rotation = anim bone).
- Weight blend: 0 = full anim, 1 = full ragdoll; dùng curve theo lực va chạm/hit severity.
- Stabilizer: add torque nhỏ vào pelvis để đứng dậy hoặc giữ hướng.

## 4) Partial Ragdoll
- Chỉ bật physics cho vùng (ví dụ tay bị bắn) bằng cách set joint drive = mềm, còn lại cứng.
- Hit reaction: blend additive anim + partial ragdoll cho natural slump.
- Death: full ragdoll sau khi play anim “hit” 0.3–0.5s rồi release.

## 5) Recovery
- Snapshot pose khi trigger ragdoll; khi phục hồi, lerp transform bone từ ragdoll → anim pose, sau đó bật kinematic.
- Align pelvis/root với navmesh/ground trước khi trao quyền cho Animator.

## 6) Perf & Debug
- Disable ragdoll rigidbody khi off-screen hoặc sau thời gian (sleep & set kinematic).
- Gizmo joint limit để debug stretch.
- Layer collision: ragdoll layer va chạm tối thiểu (ground, props lớn) để tránh kẹt nhỏ.

## 7) Ví dụ C# (Active/Partial Ragdoll)

```csharp
public class ActiveRagdoll : MonoBehaviour
{
    [SerializeField] Animator animator;
    [SerializeField] Rigidbody[] ragdollBodies;
    [SerializeField] ConfigurableJoint[] joints;
    [SerializeField] float maxBlend = 1f;
    [SerializeField] AnimationCurve hitBlendCurve;
    float _blend;
    float _blendVelocity;

    void Awake()
    {
        SetRagdoll(false);
    }

    public void TriggerHit(float force, Vector3 point)
    {
        float targetBlend = Mathf.Clamp01(force / 1000f);
        StartCoroutine(BlendRoutine(targetBlend));
        foreach (var body in ragdollBodies)
        {
            body.AddExplosionForce(force, point, 1f);
        }
    }

    IEnumerator BlendRoutine(float target)
    {
        float time = 0f;
        float duration = 0.4f;
        while (time < duration)
        {
            time += Time.deltaTime;
            _blend = hitBlendCurve.Evaluate(time / duration) * target;
            UpdateJointDrive();
            yield return null;
        }
    }

    void UpdateJointDrive()
    {
        foreach (var joint in joints)
        {
            var drive = joint.slerpDrive;
            drive.positionSpring = Mathf.Lerp(1000f, 50f, _blend);
            drive.positionDamper = Mathf.Lerp(100f, 5f, _blend);
            joint.slerpDrive = drive;
        }
        animator.enabled = _blend < 0.95f;
    }

    public void SetRagdoll(bool enabled)
    {
        foreach (var body in ragdollBodies)
        {
            body.isKinematic = !enabled;
            body.detectCollisions = enabled;
        }
        animator.enabled = !enabled;
    }
}
```

- `TriggerHit` chuyển dần joint drive mềm hơn theo lực va chạm.
- `BlendRoutine` điều chỉnh spring/damper → active ragdoll partial.
- Khi `_blend` gần 1, Animator tắt, ragdoll hoàn toàn.
- Có thể mở rộng để snapshot pose (pelvis/root) trước khi bật ragdoll.

## ✅ Apply it
- [ ] Thiết lập mass/joint limit đúng giải phẫu; collider capsule chuẩn.
- [ ] Active ragdoll: joint drive theo anim pose, blend weight dựa lực/hit.
- [ ] Partial ragdoll cho hit-react; full ragdoll khi death với blend mượt.
- [ ] Recovery: snapshot pose, align root, chuyển về anim sạch.
- [ ] Perf: sleep/disable ragdoll khi off-screen, layer collision tối giản.