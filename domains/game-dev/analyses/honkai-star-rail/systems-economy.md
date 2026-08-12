---
title: "Honkai: Star Rail — Systems map / economy (deep)"
description: "Deep GaaS economy: Power, jade faucets, pity structure, relics, endgame triad sinks/sources."
updated: "2026-08-10"
canonical: false
tags: [economy, gaas, deep, analysis-pack]
audience: [intermediate, advanced]
related:
  - ./README.md
  - ./systems-teardown.md
  - ./gdd.md
  - ../../case-studies/genshin-gacha-economy.md
sensitivity: public
---

# Honkai: Star Rail — Systems map / economy (deep)

> [← Pack](./README.md) · [Teardown](./systems-teardown.md) · Mode: `systems-economy`  
> **Structural models only.** Exact regen minutes, pity counts, jade totals: verify in live client / cited community sheets. Never invent ARPU/D7.

| Field | Value |
| --- | --- |
| Project | Honkai: Star Rail |
| Status | deep reconstructed |
| Sister pity patterns | [genshin-gacha-economy.md](../../case-studies/genshin-gacha-economy.md) |

---

## 0. Economy thesis

Hai khan hiếm chính: **thời gian (Trailblaze Power)** và **cơ hội banner (jade/tickets)**.  
Fantasy tiền tệ phục vụ: (1) mở cast theo Path/element, (2) đẩy vertical để vượt exam, (3) spectacle Ult/cinema. Monetization nén thời gian & ceiling — không khóa chapter tường minh. `(inferred)`

---

## 1. Systems ↔ economy map

| Layer | Earn | Spend |
| --- | --- | --- |
| Core combat | — | — (no soft shop mid-fight) |
| Story / explore / ach. | Jade, mats, LC | One-shot |
| Power nodes (Calyx, Cavern, Echo…) | XP, trace mats, relics, boss mats | Power |
| SU family | Planar relics, mats, lore | Time / Immersifiers etc. `(TBD names)` |
| Endgame MoC/PF/AS | Recurring jade | Skill + roster opportunity cost |
| Events / BP | Jade, mats, cosmetics | Calendar attention |
| Banners | Characters / LC | Jade/tickets |
| Cash shop | Jade, packs, BP+, refills | Money |

```text
Attention
   ├─ Daily Power empty → deterministic vertical (traces) OR RNG vertical (relics)
   ├─ Cycle exams → jade pulse → banner decisions
   └─ Version FOMO → skip vs pull → coverage vs ceiling
```

---

## 2. Currency taxonomy

| Currency / resource | Class | Persist | Notes |
| --- | --- | --- | --- |
| Trailblaze Power | Stamina faucet | Regen + overflow rules `(TBD exact)` | Cap pressure |
| Reserved / condensed Power items | Battery | Inventory | Smooth vacation |
| Character EXP / ascension mats | Soft | Yes | Planet-themed sinks |
| Trace mats + credits | Soft | Yes | Deterministic power |
| Relics + enhancement fodder | Soft RNG | Yes | Infinite |
| Light Cones | Gear / gacha | Yes | Vertical + fantasy |
| Stellar Jade | Soft+Hard hybrid | Yes | Convert → tickets |
| Special / limited passes | Tickets | Yes | Banner-specific |
| Undying Starlight / leftover shops | Pity leftover | Yes | Soft pity shop class `(TBD live names)` |
| Nameless Honor currencies | BP | Season | Free vs paid track |
| Event tokens | Temporary | Expire | FOMO shops |

---

## 3. Faucet classes (cadence)

| Faucet | Cadence | Design job | Risk if overtuned |
| --- | --- | --- | --- |
| Power regen | Continuous | Daily habit | Forced refill feel |
| Dailies / Assignment | Daily | Login glue | Chore toxicity |
| Story / companion | One-shot | Onboarding oxygen | Frontload whales only if unbalanced |
| Events | Patch | Jade spike + theme | Must-play fatigue |
| MoC / PF / AS | ~6-week phases `(observed docs)` | Skill-gated recurring jade | Anxiety / third-team tax with Starward |
| Echo weekly | Weekly | Boss sink | Easy clear trivializes |
| Top-up / packs | Cash | Revenue | Trust loss if exams require |
| BP paid | Season | Midspend | Pay lag behind FOMO |

---

## 4. Source → sink matrix

| Source | Into | Primary sinks | Failure mode |
| --- | --- | --- | --- |
| Power | Mats/relics | Traces, sets | Cap waste / burnout |
| Story jade | Tickets | Limited banners | Early pity then poverty |
| Exam stars/scores | Jade | Pull plans | Skill lockout feels P2W if too sharp |
| Events | Jade/mats/selectors | Builds / skips | Calendar stress |
| Relic drops | Combat power | Re-farm | Near-miss addiction `(genre pattern)` |
| Cash | Jade/refills | Instant ceiling | Social distrust |

---

## 5. Progression economics

### Soft walls

Equilibrium scaling → must spend Power. Trace bottlenecks on new DPS. Wrong element for AS boss.

### Hard-feeling walls

Missing limited for comfort clears (still often clear mid with invest). Relic CV chase for 0-cycle culture.

### Recommended F2P Power priority `(assumed study heuristic)`

1. Ascension + traces for **two exam cores** (MoC)  
2. Minimum PF AoE core  
3. Break-capable AS options  
4. Then relic main stats → subs  

---

## 6. Gacha / pity (structure — verify numbers live)

Hoyoverse-class pattern (detail & history in [GI sister](../../case-studies/genshin-gacha-economy.md)):

| Mechanism | Job |
| --- | --- |
| Soft pity ramp | Reduce late dry spell rage |
| Hard pity | Hard floor on rarity |
| Featured lose → next guarantee | Softens 50/50 cruelty |
| Separate LC banner rules | Monetize ceiling |
| Selector / shop / anniversary | Skip dignity / catch-up |

**Do not paste unverified pull % here.** Document only after citing patch/UI.

### Spend axes

| Decision | Prefer when |
| --- | --- |
| New character | Missing cover for ≥2 modes |
| Signature LC | Already clearing; chase ceiling |
| Eidolons | Whale / favorite |
| Skip patch | Team already clears jade thresholds |

---

## 7. Anti-inflation & brakes

- Power soft cap  
- Weekly Echo materials  
- Exam rotation changes optimal spend  
- Relic set lock-in opportunity cost  
- Pity leftover shops convert waste → slow guarantee  

Inflation risk: too much free jade → every limited owned → lose horizontal tension. Brake = new modes (Starward) + vertical relic + power creep discourse managed by older unit mid-clear viability. `(inferred)`

---

## 8. Monetization friction map

| Moment | F2P path | Paid path | Ethics heat |
| --- | --- | --- | --- |
| Limited debut | Save / skip | Top-up | High FOMO |
| BP | Free track | Paid | Medium |
| Power vacation | Wait / battery items | Refill | Low–med |
| Relic | Time | Same RNG | Time-as-pay |
| Exam jade | Skill/build | Faster gearing | Med if thresholds fair |
| Starward extras | Optional ignore | More teams ready | Med — must stay optional |

**Red lines (inspired projects):** Don’t hard-lock story chapters; don’t make base exam jade require latest E2; publish pity. `(proposed)`

---

## 9. Telemetry for a clone

| Metric | Question it answers |
| --- | --- |
| PowerCapWasteRate | Is daily loop healthy? |
| TraceCompleteBeforeRelic | Are players sequencing right? |
| ExamJadeCapture% | Skill vs gear gate honesty |
| BannerSkipWithoutRageQuit | Skip dignity |
| ModeSpecializeRatio | Are PF/MoC/AS actually orthogonal? |
| AutoShareByContent | Auto contract integrity |

---

## 10. Spreadsheet todos

- [ ] Cite dated public F2P jade/patch sheet  
- [ ] EV model: days-to-usable 4pc main stats  
- [ ] Coverage matrix: element × Path × mode  
- [ ] Starward incremental jade vs team cost  

---

[economy-systems.md](../../game-design/economy-systems.md) · [game-economics-monetization.md](../../game-design/game-economics-monetization.md) · [live-ops-design.md](../../game-design/live-ops-design.md) · [balancing-methodology.md](../../game-design/balancing-methodology.md)
