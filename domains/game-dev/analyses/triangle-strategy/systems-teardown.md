---
title: "Triangle Strategy — Systems Teardown"
description: "Systems essay: Convictions/Scales meta, positional combat physics, decision axes, premium friction."
updated: "2026-08-10"
canonical: false
tags: [game-design, case-study, teardown, tactical-rpg, narrative]
audience: [intermediate, advanced]
related:
  - ./README.md
  - ./pitch.md
  - ./gdd.md
  - ./systems-economy.md
  - ../../game-design/templates/game-systems-teardown.md
  - ../honkai-star-rail/systems-teardown.md
sensitivity: public
---

# Triangle Strategy — Systems Teardown

> [← Pack](./README.md) · [Pitch](./pitch.md) · [GDD](./gdd.md)  
> Skill: `.cursor/skills/game-systems-teardown/` · Template: [game-systems-teardown.md](../../game-design/templates/game-systems-teardown.md)

## Agent SUMMARY

- Thesis: flip FE-style “virtuous warlord ownership” → **coalition politics (Scales)** + **positional combat skill** on HD-2D dioramas; Convictions hide-couple route & roster.
- Core battle chain: read terrain → move height → act → follow-up/weather exploit → Quietuses as emergency agency.
- Meta snowball: dialogue lean → Scales vote → branch → roster identity → NG+ for other vectors.
- Axes: Conviction lean vs short-term convenience · Position safety vs flank aggression · Quietuses spend vs hoard.
- Anti–power-creep: fixed premium campaign + map scripting + Serenoa-death fail (not GaaS cycles).
- Economy: soft shop/mock-battle sinks; monetization = upfront sale, not IAP wall.
- Transfer: hidden belief meters + public vote ritual; do not clone HD-2D alone and call it USP.

**Platform / model:** Console/PC · **Premium** HD-2D tactical RPG (Square Enix / Artdink) `(observed)`  
**Genre family:** Strategy RPG / grid tactics + branching political narrative  
**Sources:** Shipped design lộ thiên + design docs trong repo; số retention **không** bịa. Tags: `(observed)` · `(inferred)` · `(genre pattern)`

Theory: [advanced-core-loops.md](../../game-design/advanced-core-loops.md) · [metagame-design.md](../../game-design/metagame-design.md) · [player-psychology.md](../../game-design/player-psychology.md) · [narrative-toolkit.md](../../game-design/narrative-toolkit.md)

---

## 0. Thesis

Triangle Strategy không thắng bằng “FE nhưng HD-2D”. Nó **đảo quyền sở hữu quyết định**: bạn là lord trên bàn cờ, nhưng **công lý quốc gia bị tranh chấp trên Scales** (vote liên minh), trong khi skill expression combat nằm ở **hình học vị trí** (height / weather / flank) — và currency ẩn **Utility · Morality · Liberty** khâu hai nửa đó thành một máy. `(inferred)`

---

## 1. Loop physics & nhịp agency

**Core actions (trong trận):**  
`Read board (height · weather · threat) → Move to geometry advantage → Act (attack / ability / item / Wait) → Trigger follow-ups / terrain rules → Spend Quietuses if crisis → Objective check`

Không phải infection (số unit → tipping spectacle). HSR-style “knowledge snowball” gần hơn ở **campaign**, còn trong battle là **position snowball**: mỗi ô đúng làm turn sau rẻ hơn; mỗi ô sai → mất unit / mất Quietuses / fail Serenoa. `(inferred)`

| Feedback | Cơ chế |
| --- | --- |
| **Positive** | Cao độ / flank / weather match → forecast xanh → K.O. chuỗi → ít mang thương → giữ Quietuses → clear sạch `(observed)` |
| **Negative / brake** | Thấp địa / weather counter / overextend → chết unit → mất DPS trên bản đồ có timer hoặc boss phase; Serenoa chết = reset kỳ vọng `(observed)` |
| **Meta positive** | Conviction lean đúng vector → unlock cast / path fantasy → identity đội mạnh trên một ethics `(observed)` |
| **Meta brake** | Lean “convenient” lệch route; Scales vote không theo ý → branch bất ngờ; FOMO recruit `(observed)` |

| Phase | Agency | Hệ thống đang làm gì | Cảm xúc |
| --- | --- | --- | --- |
| **Early** | High micro (học forecast, height) | Tutorial board; conviction còn “mềm” | “Mỗi bước có số” |
| **Mid (tipping)** | Hybrid: battle puzzle + ethics commit | Scales trở thành load-bearing; roster bắt đầu khóa identity | “Không có nước sạch” |
| **Late** | Low surprise trên path đã chọn; High plan trong map scripted | Route committed; mock battles / NG+ mở sandbox mastery | Tragedy + “xem ending kia” |

**Platform fit:** Session battle dài phù hợp couch; HD-2D diorama bán “board game sống” — agency fatigue đến từ **dialogue density**, không từ thumb-skill. `(inferred)`

---

## 2. Systems map

| Layer | Loop / modes | Job |
| --- | --- | --- |
| **Core** | Grid battle + Quietuses + terrain weather | Skill expression & failure risk |
| **Meta** | Convictions · Scales · Character stories · Encampment/shop · NG+ | Branch + roster + light vertical power |
| **Live** | Không GaaS — Mental Mock Battles / difficulty / edition QoL | Diversify session length **without** FOMO calendar `(observed)` |

Conviction là **bridge system**: narrative choice → meta currency → combat roster options. `(observed)`

---

## 3. Decision axes

### Axis 1 — Conviction lean vs Short-term convenience

| | Commit ethics vector (U/M/L) | Convenient chapter pick |
| --- | --- | --- |
| Được | Recruit/path coherence; ending identity | Tối ưu scene hiện tại / cast tạm thời |
| Mất | Khóa nhân vật / ending khác | Meter “lợn cợn”; Scales khó đoán |
| Khi nào | Mid-run khi đã chọn fantasy | Early không rõ meter `(inferred)` |

Ternary thật (3 axes) — trục thiết kế là **commit vs hedge**, không phải good vs evil. `(observed)`

### Axis 2 — Positional patience vs Flank aggression

| | Hold / morph board slowly | Push flank & tempo |
| --- | --- | --- |
| Được | An toàn Serenoa; chuẩn bị weather swing | Burst kill priority targets |
| Mất | Timer / reinforce enemy / boredom | Overextend → wipe |
| Khi nào | Defend objectives, rough weather | Soft maps, advantage height already `(inferred)` |

### Axis 3 — Quietuses spend vs Hoard

| | Burn Quietuses now | Hoard for boss / crisis |
| --- | --- | --- |
| Được | Stabilizes bad RNG / bad spawn | Peak agency ở phase khó |
| Mất | Empty toolkit late | Unit loss early → harder board |
| Khi nào | Protect key units / Serenoa | Known multi-phase battles `(observed)` |

Đây là “Bite vs Eat” của TS: Quietuses = **agency dự trữ** đổi **ổn định tức thì**.

---

## 4. Escalation & anti–power-creep

| Tier / gate | Vai trò | Trả lời power người chơi |
| --- | --- | --- |
| Tutorial boards | Dạy height/forecast | Không chặn |
| Chapter elites / scripted spawns | Ép đọc map, không chỉ grind level | Soft gate: underlevel đau `(observed)` |
| Conviction / Scales locks | Horizontal content gate | Power ≠ mở mọi unit |
| Boss / defend / multi-phase | Peak Quietuses & positioning | Hard skill check |
| Mental Mock Battles | Optional mastery / farm | Bounded optional sink `(observed)` |
| Difficulty modes | Audience widen | Không thay ethics machine `(assumed)` |

**Anti–power-creep lever:** Campaign **fixed** (premium) — không season power creep. Escalation = **map scripting + fail state Serenoa** + **route exclusivity**, không phải HP inflation theo patch. Vertical power tồn tại (level/gear) nhưng bị **board geometry** và **cast identity** giới hạn trần hiệu quả. `(inferred)`

So sánh GaaS: HSR dùng cycle buff chống one-team forever ([HSR teardown](../honkai-star-rail/systems-teardown.md)); TS dùng **branch exclusivity + NG+** cho cùng việc “ép breadth” theo nghĩa narrative. `(inferred)`

---

## 5. Economy & monetization friction

| | Chi tiết |
| --- | --- |
| **Sources** | Battle spoils, chapter rewards, mock battles, exploration pickups `(observed)` |
| **Sinks** | Shop / smith gear, optional upgrades, mock-battle mastery loops `(observed)` |
| **Grinding wall** | Có nhưng **optional** — story gates chủ yếu bằng chapter/skill/route, không bằng stamina IAP `(genre pattern)` + `(observed)` |
| **Premium friction** | Giá full game (+ edition); thời gian = dialogue + retry battles — friction **attention**, không wallet mid-run `(observed)` |
| **Fair-feel** | No pity/gacha; “unfair” cảm xúc đến từ Scales vote & hidden conviction, không từ loot RNG banner `(inferred)` |

Ethics: conflict nằm ở **narrative coercion** (đồng minh vote) chứ không ở dark-pattern shop. `(inferred)`

---

## 6. UI/UX & psychology

| Topic | Phân tích |
| --- | --- |
| **FTUE** | Forecast + height teach agency sớm; Scales ceremony dạy “bạn không độc quyền công lý” `(observed)` |
| **Friction** | Wall of political dialogue; conviction black-box → wiki reliance `(observed)` |
| **Hierarchy dưới mật độ** | Diorama đẹp vs tile ownership — camera/tilt và icon weather/height là survival kit `(inferred)` |
| **Agency vs fatigue** | Battle = high agency; story stretches = low control, high emotion — intentional whiplash `(inferred)` |
| **Psychology** | Loss aversion trên recruit lock; sunk cost route; autonomy tension khi Scales outvote player (liên quan SDT / agency trong [player-psychology.md](../../game-design/player-psychology.md)) `(inferred)` |

---

## 7. Transfer (mang đi game khác)

| Pattern portable | Đừng copy mù |
| --- | --- |
| **Hidden belief meters** gắn recruit/ending | Meter không surface → frustration thuần |
| **Public vote ritual** (Scales) cắt “player = god” | Vote giả (luôn theo player) = theatrical waste |
| **Geometry-first combat** (height/weather) | Stat inflation bỏ qua board = hệ chết |
| **Emergency resource** (Quietuses) tạo axis spend/hoard | Resource quá nhiều = hết quyết định |
| **NG+ as breadth machine** cho premium narrative | Ép NG+ nếu ending 1 nghèo trải nghiệm |

**Title-specific:** HD-2D production language; Norzelia salt/iron politics; Square catalog marketing — không phải USP hệ thống thuần.

---

## 8. Open questions / verify

- [ ] Phân bổ % session: dialogue vs battle theo chapter mid/late.
- [ ] Tương quan conviction variance (độ “thuần” vector) vs clear rate chapter khó.
- [ ] Quietuses spend curve: % players empty trước final phase.
- [ ] % players start second route / NG+ trong 30 ngày sau ending `(no invented %)`.
- [ ] Perception study: Scales “công bằng” vs “mất kiểm soát” theo personality.
- [ ] So teardown với Tactics Ogre Reborn / FFT trên axis “politics ownership”.

---

## Theory footer

| Topic | Path |
| --- | --- |
| Core/meta | [advanced-core-loops.md](../../game-design/advanced-core-loops.md) |
| Meta collection / branch | [metagame-design.md](../../game-design/metagame-design.md) |
| Psychology | [player-psychology.md](../../game-design/player-psychology.md) |
| Narrative structure | [narrative-toolkit.md](../../game-design/narrative-toolkit.md) |
| Pack siblings | [pitch.md](./pitch.md) · [gdd.md](./gdd.md) · [systems-economy.md](./systems-economy.md) |
| GaaS contrast | [honkai-star-rail systems-teardown](../honkai-star-rail/systems-teardown.md) |
