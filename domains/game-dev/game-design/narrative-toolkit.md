---
title: "Narrative Toolkit"
description: "Story bible, quest structure và branching dialogue cho dự án indie/hybrid casual."
tags:
  - game-design
  - narrative
updated: 2026-03-11
---

# 📖 Narrative Toolkit

> Narrative không chỉ là lời thoại – nó phải hỗ trợ core loop và economy.

## 1. Story Bible Snapshot
- World premise, tone, key conflicts.
- Character sheet (goal, flaw, arc) bảng 3 cột.
- Theme + pillars (friendship, sacrifice...).

## 2. Quest & Arc Structure
```
Setup → Conflict → Choice → Payoff
```
- Main arc vs side quest với ID, owner, dependency.

## 3. Branching Dialogue
- Tool: Ink/Fungus/Yarn Spinner.
- Rule: mỗi branch quay về core loop reward.
- Telemetry tag: `DialogueChoice`, `AffinityChange`.

## 4. Integration Gameplay
- Narrative gating progression.
- Narrative-driven economy (NPC shop, story currency).
- Cinematic tiering (S/A/B) để quản lý resource.

## 5. Localization
- Export CSV/Sheet, include speaker/context.
- Placeholder tag {playerName}.
- QA checklist: banned words, text fit.

## 6. KPI
- Story completion %.
- Choice diversity.
- Sentiment score.
- Churn tại narrative beat.

## 7. Checklist
- [ ] Story bible versioned.
- [ ] Quest có owner, dependency.
- [ ] Dialogue telemetry ID.
- [ ] Localization pipeline OK.
- [ ] KPI xuất hiện trên dashboard.

## 8. Links
- [Core Loop Mastery](./core-loop-mastery.md)
- [Economy Systems](./economy-systems.md)
- [Playtest Framework](./playtest-framework.md)