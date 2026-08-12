---
title: "Infect Them All — Systems teardown (gold)"
description: "Gold systems essay: Health Decay, Bite vs Eat, tipping phases, density UX."
updated: "2026-08-10"
canonical: false
tags: [teardown, gold, infection, analysis-pack]
audience: [intermediate, advanced]
related:
  - ./README.md
  - ../_quality-bar.md
  - ../honkai-star-rail/systems-teardown.md
sensitivity: public
---

# Infect Them All — Systems Teardown

> [← Pack](./README.md) · [Quality bar](../_quality-bar.md)  
> **Gold reference** cho density — Magic Cube series (Zombies / Vampires / sequels). Claims tagged.

## Agent SUMMARY

- Thesis: infection snowball powered by **Health Decay** + binary **Bite→Infect vs Bite→Eat**.
- Core: move → latch bite → choose growth vs heal → minions cascade → clear.
- Phases: high micro early → tipping mid → late spectacle (horde works).
- Axes: Infect vs Eat · Aggressive dive vs bait with minions · Upgrade speed vs tank.
- Escalation: enemy weaponization + stage scripts; anti-creep = player still dies to decay/gunfire if starve bites.
- Economy: stage gold → stat upgrades; light IAP era friction.
- Transfer: any growth fantasy needs costly alternative to growth (Heal tax).

**Platform:** Mobile arcade · **Genre:** Infection growth  
**Sources:** App Store features + contemporaneous reviews `(observed)`; design inference tagged.

---

## 0. Thesis

Infect Them All **đảo survivor fantasy**: bạn không chạy khỏi đám đông — bạn **là vector**. Máy cảm xúc là tipping từ “cắn từng người” sang “xem army tự lan,” dưới luật **máu chảy liên tục**. `(inferred)`

---

## 1. Loop physics & agency

**Core:**  
`Navigate densitiy → Collide latch → Bite channel → Release as Infect OR finish as Eat → Minions expand / HP restore → Objective clear`

| Feedback | |
| --- | --- |
| **+** | Infect → more agents → faster clear → safer paths `(observed)` |
| **−** | Eating removes convert; decay forces bites; armed humans punish greed `(observed)` |

| Phase | Agency | System | Feel |
| --- | --- | --- | --- |
| Early | High micro | Few minions; teach Eat/Infect | Tense surgical bites |
| Mid tipping | Hybrid | Chain conversions start | “It’s working” |
| Late | Low micro / spectacle | Horde clears while you steer edges | Power trip / camera chaos |

Mobile: short stages; thumb stick / tilt; release action on bite is the skill beat. `(observed)`

---

## 2. Systems map

| Layer | Modes | Job |
| --- | --- | --- |
| Core | Stage clear infection | Growth physics |
| Meta | Gold upgrades, unlock characters | Vertical readiness |
| “Live” | Campaign · Infinite/Tower · Survival · Blitz | Session length knobs `(observed)` — not GaaS seasons |

---

## 3. Decision axes

### Axis 1 — Infect vs Eat (canonical)

| | Infect (release) | Eat (consume) |
| --- | --- | --- |
| Được | +1 fighter; snowball | Large heal; remove threat slot |
| Mất | Little/no heal; risk mid-bite | Lose convert; slow growth |
| Khi nào | Healthy + crowd left | Critical HP / hard target heal value `(observed)` |

### Axis 2 — Dive boss vs Sacrifice minions

| | Dive as player | Use minions as meatshield |
| --- | --- | --- |
| Được | Control bite timing | Preserve player HP |
| Mất | Die to focus fire | Lose army tempo |
| Khi nào | Need heal eat | Gun lines / soldiers `(inferred)` |

### Axis 3 — Meta: Speed vs Survivability upgrades

| | Speed/eat rate | HP/armor |
| --- | --- | --- |
| Được | Faster tipping | Forgive mistakes |
| Mất | Squishy | Slow snowball |
| Khi nào | Blitz modes | Survival / late campaign `(assumed)` |

---

## 4. Escalation & brakes

| Tier | Role |
| --- | --- |
| Civilians | Tutorial converts |
| Armed / specials | Punish brainless zerg |
| Bosses | Spike requiring specials/minions `(observed)` |
| Mode timers (Blitz) | Compress decisions |
| Infinite/Tower | Soft endless escalate |

**Anti–power-creep:** Upgrades help but **decay + guns** vẫn kill if starve Infect economy; modes change pressure type not only HP sponges. `(inferred)`

---

## 5. Economy & monetization

See [systems-economy.md](./systems-economy.md). Soft gold from stages → permanent upgrades; series sold as paid / light IAP era apps `(observed)`. Friction = skill walls + upgrade grind, not stamina banner FOMO.

---

## 6. UX & psychology

| | |
| --- | --- |
| FTUE | Collide→bite→release readable in seconds `(observed)` |
| Density | Green/tint infected; risk of clutter late — performance boasts 150–200 units `(observed)` |
| Psychology | Variable reward of tipping; loss aversion when over-eat at low HP; competence fantasy when army autopilots ([player-psychology.md](../../game-design/player-psychology.md)) |

---

## 7. Transfer

| Take | Don’t |
| --- | --- |
| Growth action needs **costly alternative** (Eat) | Free growth + free heal |
| Design an explicit **tipping phase** | Flat difficulty forever |
| Modes remix same core | New game every mode |
| Readable infection state | Identical sprites for infected |

Contrast GaaS puzzle: [HSR teardown](../honkai-star-rail/systems-teardown.md) — knowledge snowball, not unit-count tipping.

---

## 8. Open / verify

- [ ] Exact HP decay rate curve per character  
- [ ] Bite latch timing windows per enemy class  
- [ ] IAP SKU map per sequels  
- [ ] Compare Infectonator on same axes  

---

Theory: [advanced-core-loops.md](../../game-design/advanced-core-loops.md) · [_quality-bar.md](../_quality-bar.md)
