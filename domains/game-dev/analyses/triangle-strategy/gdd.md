---
title: "Triangle Strategy — GDD (reconstructed thin bible)"
description: "Thin living GDD from shipped HD-2D SRPG: Convictions, Scales, combat pillars, progression."
updated: "2026-08-10"
canonical: false
tags: [game-design, gdd, tactical-rpg, case-study]
audience: [intermediate, advanced]
related:
  - ./README.md
  - ./pitch.md
  - ./systems-economy.md
  - ./systems-teardown.md
  - ../../game-design/templates/game-gdd.md
sensitivity: public
---

# Triangle Strategy — GDD / design bible

> [← Pack](./README.md) · [Pitch](./pitch.md) · Skill: `.cursor/skills/game-design-docs/` · Mode: `gdd`  
> **Thin GDD tái dựng** từ title đã ship — dùng học spec / reference, không phải tài liệu nội bộ Square.  
> Tags: `(locked)` = khớp ship đã quan sát · `(proposed)` = suy ra cho bài tập · `(TBD)` = cần verify patch/edition · `(assumed)`

| Field | Value |
| --- | --- |
| Title | Triangle Strategy |
| Genre / platforms | Tactical RPG (grid) · HD-2D · Switch originally → multiplat / enhanced `(locked)` |
| Team / owners | Square Enix · Artdink (shipped) — doc owner: Docs study |
| Doc status | Reconstructed reference `(proposed)` as teaching GDD |
| Linked pitch | [pitch.md](./pitch.md) |
| Linked economy sheet | [systems-economy.md](./systems-economy.md) |

---

## 1. Vision & pillars

- **Vision:** Một chiến tranh liên minh nơi **lời nói trên hội đồng và nước cờ trên bàn** cùng quyết định số phận quốc gia; người chơi cảm thấy mỗi “đúng” đều có giá. `(assumed)`
- **Pillars (≤3):**
  1. **No clean war** — không có đường đạo đức xanh lá.
  2. **Position is the skill** — height / weather / flank / Quietuses > thuần stat.
  3. **Belief routes roster** — Utility / Morality / Liberty định hình cast & ending.
- **Anti‑goals:** Open world filler; gacha LiveOps; auto-battler skip fantasy; dating-sim support làm xương sống. `(locked)` as product stance

---

## 2. Player fantasy & target

- **Fantasy:** Lord trẻ nhà Wolffort — strategist + moral agent trong bàn cờ sống (HD-2D diorama). `(locked)`
- **Target player:** SRPG veterans & story-RPG players chịu dialogue dài; chấp nhận permadeath-lite / difficulty options. `(assumed)`
- **Session model:** Chapter beat = story nodes + optional prep + 1 major battle; ~45–90 phút/session `(assumed)`

---

## 3. Loops — Core / Meta / Live

| Layer | Chain | Win / fail / exit |
| --- | --- | --- |
| **Core** (battle) | `Select unit → Move on height grid → Act (attack/ability/item/Wait) → Resolve terrain/weather/follow-up → Turn order` | Win: map objective (rout / boss / defend…). Fail: Serenoa K.O. or objective fail → Game Over / retry. Exit: victory → spoils + story. `(locked)` |
| **Meta** (campaign) | `Chapter story → Convictions lean (dialogue/choices) → Scales of Conviction → Branch → Battle → Character stories / Mental Mock Battles → Encampment upgrade` | Win path: reach ending for conviction vector. Soft fail: locked characters / harder later fights. Exit: credits / NG+. `(locked)` |
| **Live** | N/A GaaS — optional post-ship: Mental Mock Battles, NG+, difficulty, edition QoL | No season pass cadence `(locked)` |

---

## 4. Systems index

| System | Purpose | Owner (study) | Detail doc | Status |
| --- | --- | --- | --- | --- |
| Convictions (U/M/L) | Ẩn điểm niềm tin → route, recruit, ending | Design | § Combat/Meta modules below | `(locked)` |
| Scales of Conviction | Vote công khai; Serenoa không độc quyền | Narrative + Design | § Narrative | `(locked)` |
| Grid combat | Skill expression chính | Combat design | § Optional: Combat | `(locked)` |
| Quietuses | Meta battle spend (TP-like) | Combat | Combat module | `(locked)` |
| Character stories | Horizontal cast depth | Narrative | — | `(locked)` |
| Encampment / shops / kudos | Prep & light economy | Systems | economy sheet `(TBD)` | `(locked)` |
| Mental Mock Battles | Optional challenge / grind sink | Combat | — | `(locked)` |
| NG+ / New Game+ | Replay routes, carry select progress | Meta | — | `(locked)` |
| Difficulty modes | Widen audience | Combat/Prod | — | `(locked)` |

---

## 5. Progression & content

- **Horizontal unlocks:** Characters via story + conviction thresholds; Quietuses; character story battles; mock battles maps. `(locked)`
- **Vertical power:** Levels, weapon skills, promotion-style upgrades, equipment, accessories; kudos-related rewards. `(locked)` / verify exact names per edition `(TBD)`
- **Soft gates:** Underleveled for chapter bosses; missing Quietuses; suboptimal conviction for recruit. `(assumed)`
- **Hard walls:** Story branch locks; Serenoa death = fail; some paths exclusive. `(locked)`
- **Content buckets:** Main chapters · Character stories · Mock battles · Multiple endings · Optional rematch/challenge. `(locked)`

---

## 6. UX / controls / FTUE

- **Input map (typical SRPG):** Cursor move · Confirm · Cancel · Turn menu · Camera rotate/tilt · Range preview · Unit list. `(assumed)` standard
- **First ~30 minutes (beat sheet):** World tone (Norzelia salt/iron tension) → introduce Serenoa & lords → tutorial combat (move/height) → early dialogue choices seeding Convictions → first meaningful political stakes. `(assumed)` exact chapter numbering varies by edition
- **HUD priorities:** Turn order · height readability · attack forecast · weather icon · objective text — combat UI phải thắng “pretty diorama clutter”. `(assumed)`

---

## 7. Narrative (structure only)

- **Spine:** Ba thế lực / lợi ích xung quanh **muối & sắt** → Wolffort bị kéo vào chiến tranh liên minh → Choices định nghĩa “công lý” nào được ưu tiên. `(locked)`
- **Branch tech:** Conviction scores (hidden) + **Scales of Conviction** (on-stage vote with ally opinions). `(locked)`
- **Cast roles:** Protagonist house + rival lords + specialty units as ideology magnets. `(locked)`
- **Tone:** Political tragedy / drama, not shonen tournament. `(assumed)`
- Details / scene bible → external lore wikis · theory: [narrative-toolkit.md](../../game-design/narrative-toolkit.md)

---

## 8. A/V direction (constraints)

- **HD-2D:** Painted backgrounds + 3D-ish sprites; battles are **readable dioramas** — VFX cannot hide tile ownership / height. `(locked)`
- **Tone ↔ systems:** Solemn UI, council ceremony SFX for Scales = mark “this choice is load-bearing”. `(assumed)`
- **Readability constraints:** Weather/height must have persistent icons; elevation ramps clear from camera. `(proposed)` as design rule extracted from play

---

## 9. Tech & live constraints

- **Class:** Offline single-player campaign; no mandatory netcode. `(locked)`
- **Platform:** Console/PC; performance budget for HD-2D battles with many actors. `(assumed)`
- **LiveOps:** None as core loop. Post-launch = patches, difficulty, port/enhanced edition content. `(locked)`
- See [live-ops-design.md](../../game-design/live-ops-design.md) only as contrast (what we refuse).

---

## 10. Milestones

*(Reconstructed production gates for study — not real SE milestones.)*

| Gate | Entry criteria | Exit / ship criteria |
| --- | --- | --- |
| Vertical slice | Pillars locked; 1 Scales scene + 1 signature height/weather map | Players articulate “politics + position” without marketing text `(proposed)` |
| Alpha | Full chapter loop; conviction → recruit demo; battle feature complete | Can finish vertical path without debug `(proposed)` |
| Content complete | All branches / endings scripted; cast join conditions | Route QA matrix green `(proposed)` |
| Ship / enhanced | Difficulty polish; mock battles; QoL | Premium release criteria `(locked)` as product type |

---

## 11. Open questions & changelog

| Date | Decision | Owner |
| --- | --- | --- |
| 2026-08-10 | Create reconstructed thin GDD from pitch + shipped design | Docs agent |
| 2026-08-10 | Defer full economy sheet to mode `systems-economy` | Docs agent |

**Open / verify `(TBD)`:**

- [ ] Exact conviction point sources (every dialogue weight).
- [ ] Quietuses TP economy numbers per difficulty.
- [ ] Full recruit threshold table per character.
- [ ] Edition delta (original vs Multiplayer? / Deluxe / PC) feature list.
- [ ] Mental Mock Battle as intentional grind sink vs optional mastery — write economy sheet.

---

## Optional module A — Combat (thin)

| Rule | Spec |
| --- | --- |
| Turn structure | Unit-at-a-time on grid; move + act `(locked)` |
| Spacing | Height advantages / disadvantages for attacks; flanking `(locked)` |
| Environment | Weather alters abilities/accuracy/range (fire, ice, wind, rain, etc.) `(locked)` |
| Follow-ups | Adjacent ally follow-up attacks when conditions met `(locked)` |
| Defeat | Enemy K.O.; Serenoa K.O. = battle fail `(locked)` |
| Quietuses | Limited powerful out-of-band actions (heal/revive/damage/buff class) — spend resource across battle/campaign prep `(locked)` / exact currency name verify `(TBD)` |
| Difficulty | Adjusts enemy pressure / assists — does not remove conviction ethics `(assumed)` |

**Edge cases:** Trap tiles, elevation-only paths, defend timers, multi-phase bosses — chapter-scripted `(locked)` as design space.

---

## Optional module B — Convictions & Scales

| Element | Behavior |
| --- | --- |
| Three axes | Utility · Morality · Liberty — hidden accumulators `(locked)` |
| Sources | Dialogue choices, free roam interactions, battle conduct `(locked)` / weights `(TBD)` |
| Scales | Party members vote; persuasion attempts may shift votes; outcome branches story `(locked)` |
| Roster coupling | High affinity on axes unlocks specialists; opposite path may lock `(locked)` |
| Endings | Vector of convictions → ending family `(locked)` |

**Design rule:** Player should feel agency *and* consequence of coalition politics — not pure puppet master. `(assumed)` pillar tie-in

---

## Optional module C — Prep / light economy

| Sink / source | Role |
| --- | --- |
| Battles / spoils | Soft currency & materials |
| Shop / smith | Vertical gear |
| Encampment facilities | Quality-of-life & progression taps |
| Mock battles | Optional power/mastery sink |

→ See pack sheet [systems-economy.md](./systems-economy.md).

---

## Theory footer

[advanced-core-loops.md](../../game-design/advanced-core-loops.md) · [metagame-design.md](../../game-design/metagame-design.md) · [narrative-toolkit.md](../../game-design/narrative-toolkit.md) · [level-design-flow.md](../../game-design/level-design-flow.md) · Template [game-gdd.md](../../game-design/templates/game-gdd.md)  
Pack: [pitch.md](./pitch.md) · [systems-teardown.md](./systems-teardown.md) · [systems-economy.md](./systems-economy.md) · [playtest-review.md](./playtest-review.md)
