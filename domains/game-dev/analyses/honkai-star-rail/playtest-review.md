---
title: "Honkai: Star Rail — Playtest / review (deep study)"
description: "Deep study protocol: Break/SP FTUE, Auto contract, orthogonal endgame exams; scores TBD."
updated: "2026-08-10"
canonical: false
tags: [playtest, gaas, deep, analysis-pack]
audience: [intermediate, advanced]
related:
  - ./README.md
  - ./gdd.md
  - ./systems-teardown.md
  - ../../game-design/playtest-framework.md
  - ../../game-design/checklist-game-review.md
sensitivity: public
---

# Honkai: Star Rail — Playtest / review (deep study)

> [← Pack](./README.md) · Mode: `playtest-review`  
> Protocol for **inspired GaaS TB** or structured review of HSR itself. Scores blank until a real session.

| Field | Value |
| --- | --- |
| Build | HSR live / your slice |
| Facilitator | … |
| N / persona | New Hoyoverse · Returning · Optimizer |
| Linked GDD | [gdd.md](./gdd.md) §FTUE · §Combat · §LiveOps |

---

## 1. Research questions (priority order)

1. **RQ1:** Players treat Break as a *phase*, not a minor bonus?  
2. **RQ2:** Players can explain shared SP (Skill costs / Basic refunds) unprompted?  
3. **RQ3:** After seeing MoC vs PF vs AS descriptions, players invent *different* team needs?  
4. **RQ4:** When do they enable Auto — before or after understanding RQ1–2?  
5. **RQ5:** Banner skip feels psychologically OK if mid exams clearable?

**Success (study thresholds — tune, don’t fake results):** ≥8/10 verbalize RQ1+RQ2; Auto enable after first elite Break for ≥70% of newcomers `(proposed)`.

---

## 2. Protocols

### P0 — FTUE combat (45–60m) — new players

| Block | Time | Tasks | Observe |
| --- | --- | --- | --- |
| Onboarding | 10m | First fights | Weakness icon use |
| SP starve | 10m | Fight designed with hungry Skills | Basic usage talk-aloud |
| Break elite | 15m | Elite high Toughness | Target order |
| Ult + Technique | 10m | Energy cycle | Burst timing |
| Debrief | 10m | Pillars quiz | Exact wording |

### P1 — Daily economy day (async 1 day)

Empty Power once; journal: traces vs relics choice; cap hit Y/N.

### P2 — Endgame literacy (60m) — mid accounts

| Block | Time | Observe |
| --- | --- | --- |
| Read MoC buffs only | 10m | Plan before pull urge |
| Attempt mid MoC floor | 20m | Team swaps |
| PF scoring explanation | 15m | AoE recognition |
| AS Break focus | 15m | Element matching talk |

### P3 — Expert review checklist session (stakeholders)

Use scoring table §5 without players — design/prod/QA only.

---

## 3. Telemetry pack (instrument a clone)

| Event | Properties | Insight |
| --- | --- | --- |
| `combat.break.first` | time_from_ftue | RQ1 |
| `combat.sp.empty` | fight_id | SP teaching |
| `auto.enable` | content_type | Auto contract |
| `power.cap_hit` | hour_local | Loop health |
| `exam.attempt` | mode=moc\|pf\|as | Breadth |
| `banner.skip_confirm` | patch_id | Skip dignity |
| `relic.enhance.rollback_emotion` proxy | session rage quit | Near-miss |

---

## 4. Survey (≤10)

| # | Item | Scale |
| --- | --- | --- |
| 1 | Understood Toughness Break as a damage window | 1–5 |
| 2 | Understood Skill Points are shared | 1–5 |
| 3 | Auto felt OK for farming | 1–5 |
| 4 | MoC / PF / AS feel like different exams | 1–5 |
| 5 | Skipping a banner feels acceptable | 1–5 |
| 6 | Relic grinding feels fair | 1–5 |
| 7 | Story length vs daily loop balance | 1–5 |
| 8 | Want to continue tomorrow | 1–5 |
| Open A | Most confusing UI | text |
| Open B | Most memorable combat moment | text |

---

## 5. Build review scores (fill when reviewing)

| Area | Score 1–5 / N/A | Note |
| --- | --- | --- |
| General feel | TBD | |
| Core gameplay (Break/SP) | TBD | |
| Art & UI | TBD | |
| Flow & balance | TBD | Equilibrium pacing |
| Progression | TBD | Trace vs relic |
| Misc (stability, access) | TBD | |
| Live Ops | TBD | Cycle FOMO |
| Competitor (vs GI / other TB gacha) | TBD | |
| Business / monetization feel | TBD | Pity honesty |

---

## 6. Insight → action template

| Tag | Insight | Sev | Action | Owner | GDD section |
| --- | --- | --- | --- | --- | --- |
| Loop | … | S0–S3 | … | … | Combat FTUE |
| Economy | … | | | | Power priority |
| UX | … | | | | HUD |
| LiveOps | … | | | | Exam triad |

---

[playtest-framework.md](../../game-design/playtest-framework.md) · [checklist-game-review.md](../../game-design/checklist-game-review.md) · [systems-teardown.md](./systems-teardown.md)
