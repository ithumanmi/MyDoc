# Mode: full-pack (game analysis folder)

**Job:** When analyzing (or greenlighting) **one game**, create a **folder hub** with all design models in one place.  
**Not:** One unread mega-file; not Games OS play-taste notes.

## Output layout (required)

```text
domains/game-dev/analyses/<kebab-slug>/
  README.md                 ← fill from game-analysis-pack-readme.md
  pitch.md                  ← game-pitch-one-pager.md
  gdd.md                    ← game-gdd.md
  systems-economy.md        ← game-systems-map-economy.md
  systems-teardown.md       ← game-systems-teardown.md (+ skill game-systems-teardown)
  playtest-review.md        ← game-playtest-review.md
  postmortem.md             ← game-postmortem.md
```

Also add a row to `domains/game-dev/analyses/README.md`.

## Workflow

1. Confirm **slug** (e.g. `triangle-strategy`, `honkai-star-rail`) + whether shipped study vs own project.
2. Create folder + hub README with status matrix (all six listed).
3. Fill in this order (dependencies):
   1. `pitch.md` — thesis & pillars
   2. `gdd.md` — expand pillars → systems index (link economy + teardown)
   3. `systems-teardown.md` — loop physics, axes, escalation (load skill `game-systems-teardown`)
   4. `systems-economy.md` — sources/sinks aligned with teardown economy section
   5. `playtest-review.md` — protocol/checklist (TBD scores OK if not run)
   6. `postmortem.md` — study stub or real retro
4. Cross-link every file back to `./README.md` and siblings.
5. Update hub status: `filled` · `stub` · `TBD`.

## Quality bar

| Do | Don’t |
| --- | --- |
| One slug = one pack forever | Split same title across `pitches/` + `case-studies/` without redirect |
| Teardown remains systems essay quality | Paste store description into teardown |
| Economy numbers labeled `(assumed)` | Invent ARPU / D7 |
| Playtest/postmortem honest stubs | Fake “team said…” |

## Triggers (examples)

- “Phân tích game X đầy đủ”
- “full-pack / dossier / tất cả models cho X”
- “Tạo bộ doc design cho X như Triangle Strategy”
