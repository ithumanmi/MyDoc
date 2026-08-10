# Chapter 2: Topic map & routing

## Core Idea
Resolve intent with the map **before** opening deep-dives; heuristic lines beat search-first.

## Frameworks Introduced
- **Intent → Path Heuristic**: Fixed question → branch → canonical path
  - When to use: Ambiguous “game” questions
  - How: Match phrase class; open map row; then hub README

## Key Concepts
- **Canonical**: Preferred path in map for a topic
- **Make cluster**: design, Unity, netcode, art-tech, production, challenges
- **Earn cluster**: career, indie/publisher, market research
- **Play cluster**: leisure, taste, backlog, fun-maxing/dopamine
- **Follow cluster**: culture radar, industry radar, weekly brief

## Mental Models
- Use “How do I build…?” → Make only.
- Use “Salary/publisher…?” → Earn only.
- Use “Everything about games?” → Games OS README, not domains root.

## Anti-patterns
- **Grep domains before map**: Wastes tokens; misroutes leisure to Unity.
- **Confuse play taste with genre design pillars**: Leisure ≠ `genre-deep-dives` KPI.

## Reference Tables
```text
"How do I build / design / implement?" → Make (domains/game-dev)
"Salary / freelance / publisher / $?"  → Earn (career game-dev)
"How do I play well / without burnout?" → Play
"What happened in games this week?"    → Follow
"Everything about games / Games OS?"   → guides/05-games-os/README.md
```

## Worked Example
Ask: “Balatro-like genre research for my prototype.”  
Tag as Make (design) → `domains/game-dev/game-design/` (+ market research if Earn sizing). Optional Play session marked **Make-research**, not leisure Next slot.

## Key Takeaways
1. Open `games-os-map.md` for path table.
2. Keep Make/Earn pointers cold-start accurate.
3. When both tech and career asked → both hubs; lead with Make for skills.

## Connects To
- **Ch 1**: Four branches
- **Ch 3**: Weekly time budgets per branch
- **Source**: `guides/05-games-os/games-os-map.md`, `links.md`
