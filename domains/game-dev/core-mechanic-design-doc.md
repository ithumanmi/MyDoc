## 🎯 Core Mechanic Game Design Doc (GDD) – Template & Ví dụ

> “Core mechanic định hình 80% cảm giác chơi.” – Hãy viết Game Design Doc (GDD) để mọi người trong team đều hiểu rõ cơ chế cốt lõi, cách vận hành và KPI cần đạt.

### 1. Overview & Player Fantasy
- **Fantasy:** Người chơi muốn cảm thấy như thế nào? (Ví dụ: “Samurai tốc độ ánh sáng”)
- **Core Promise:** Một câu mô tả ngắn (15 chữ) về trải nghiệm.
- **Target Platform / Genre:** PC roguelike / Mobile action v.v.

### 2. Core Loop & Flow
| Step | Mô tả hành động | Feedback chính |
|:----|:----------------|:---------------|
| 1 | Player quan sát thế trận | Telemetry + Highlight mục tiêu |
| 2 | Kích hoạt core mechanic (Dash/Grapple/etc.) | Camera tilt, particle burst |
| 3 | Reward/Fail state | Slow-mo kill / Screen desaturate |

```
Core Loop Diagram (Pseudo):
Sense → Decide → Execute → Reward → Reset
```

### 3. Ruleset & System Detail
- **Input:** Button mapping, gesture, cooldown.
- **Constraints:** Stamina cost, limited charges, energy regen.
- **Fail States:** Hit wall (stun 1s), miss target (lose combo).
- **Synergy:** Tương tác với mechanic khác (Combo với parry, chain kill).

### 4. Feedback & Juice Checklist
- **Visual:** Trail, motion blur, screen shake.
- **Audio:** Whoosh pitch, impact sound layer.
- **Haptic:** Rumble intensity.
- **UX:** Crosshair color change, target lock indicator.

### 5. Balancing & Difficulty Curve
- **Tuning table:**
  | Level | Speed multiplier | Cooldown | Enemy reaction |
  |:------|:----------------|:---------|:---------------|
  | Early game | 1.0x | 3s | Slow telegraph |
  | Mid game | 1.25x | 2s | Faster react |
  | Late game | 1.5x | 1.5s | Instant counter |
- **Metrics:** Success rate target (70% mid game), time-to-master (~30 phút).
- **Dynamic Difficulty hooks:** Auto-aim assist, slowdown window.

### 6. KPI & Telemetry
- **Usage Rate:** % thời gian mechanic được kích hoạt.
- **Kill Contribution:** % enemy kill nhờ mechanic.
- **Fail Reason Breakdown:** Miss target, stamina cạn, camera issue.
- **Heatmap:** Vị trí người chơi dùng mechanic nhiều nhất.

### 7. Playtest Checklist
- [ ] Người chơi hiểu cơ chế trong < 1 phút?
- [ ] Họ mô tả được fantasy sau khi chơi?
- [ ] Camera có gây say khi spam mechanic?
- [ ] Người chơi có lạm dụng mechanic (breaking balance)?
- [ ] Log telemetry đúng sự kiện?

### 8. Ví dụ: “Aether Dash Grapple”
- **Fantasy:** Ninja lướt qua không gian, bám trụ vào boss và kết liễu trong 1 đòn.
- **Input:** Hold RT để charge dash, release + aim bằng right stick; nhấn X khi icon xuất hiện để grapple.
- **Rules:**
  - Dash tiêu hao 25 năng lượng, cooldown 2s.
  - Grapple chỉ khả dụng khi enemy bị stagger < 30% HP.
  - Nếu miss, player mở lưng 0.5s.
- **Feedback:**
  - Dash: Cyan trail + distortion shader.
  - Grapple success: Time dilation 0.3s + “Shatter” SFX.
  - Fail: Screen tint đỏ + audio low pass.
- **Balancing:**
  - Early: Auto-aim cone 30°. Late: 10°.
  - Boss phản ứng: Shield nếu người chơi dash 3 lần liên tục.
- **Metrics cần theo dõi:**
  - Average dash per minute.
  - Success rate grapple khi boss còn >50% HP (goal <5%).
  - Player comfort survey: camera motion sickness score.

### 9. Tài nguyên tham khảo
- [Game Feel – Steve Swink]
- [Juice It or Lose It – GDC Talk]
- [domains/game-dev/ai/behavior-tree/core-concepts.md]
- [domains/game-dev/unity-deep-dive/architecture-patterns.md]

> **Tip:** Luôn cập nhật GDD sau mỗi vòng playtest. Core mechanic tốt phải vừa “ngầu” (fantasy) vừa có số liệu chứng minh (telemetry).