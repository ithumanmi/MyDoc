# 🎨 Game Designer Roadmap: Zero → Professional

> [← Back to Home](../../README.md) | [Game Dev Roadmap](../../../domains/game-dev/README.md)

Hướng dẫn toàn diện để trở thành Game Designer - Người tạo ra trải nghiệm chơi, không chỉ code.

---

## 📋 Mục lục

1. [Game Designer vs Game Developer](#1-game-designer-vs-game-developer)
2. [Skills & Mindset](#2-skills--mindset)
3. [Learning Path (0-24 tháng)](#3-learning-path-0-24-tháng)
4. [Specializations](#4-specializations)
5. [Portfolio Building](#5-portfolio-building)
6. [Career Path & Salary](#6-career-path--salary)
7. [Getting Hired](#7-getting-hired)
8. [Resources](#8-resources)

---

## 1. Game Designer vs Game Developer

### Game Designer (Thiết kế trò chơi)

**Công việc chính:**
- Tạo ra **gameplay mechanics** (nhảy, bắn, thu thập...)
- Design **progression systems** (leveling, unlocks, skill trees)
- Balance **game economy** (currency, rewards, pricing)
- Write **Game Design Documents (GDD)**
- Prototype và iterate dựa trên playtesting

**Ví dụ cụ thể:**
- *"Jump height bao nhiêu để player cảm thấy responsive nhưng không broken?"*
- *"Enemy spawn rate như thế nào để challenging mà không frustrating?"*
- *"Weapon damage progression từ level 1-50?"*

---

### Game Developer (Lập trình game)

**Công việc chính:**
- **Implement** những gì Designer đã design
- Code movement, combat, AI, networking
- Optimize performance (60fps, memory usage)

**Ví dụ:**
- Designer: "Tôi muốn double jump mechanic"
- Developer: "OK, tôi sẽ code physics cho nó"

---

### Overlap & Collaboration

**Best Game Designers hiểu code cơ bản:**
- Communicate tốt hơn với developers
- Prototype nhanh mà không cần đợi dev
- Hiểu technical constraints (VD: "AI pathfinding tốn performance")

**Lời khuyên:**
- Nếu bạn **thích sáng tạo, storytelling, psychology** → Game Designer
- Nếu bạn **thích code, solve problems, optimization** → Game Developer

---

## 2. Skills & Mindset

### Hard Skills

**1. Design Thinking:**
- **Player psychology:** Tại sao người chơi thích "loot boxes"? (Variable rewards)
- **Flow theory:** Balance difficulty vs skill
- **Core loop:** What player does every second/minute/hour

**2. Systems Thinking:**
- Hiểu cách các mechanics tương tác với nhau
- VD: Trong RPG, *Damage system + Armor system + Healing system = Combat balance*

**3. Documentation:**
- Viết GDD rõ ràng (Developers phải hiểu được)
- Flowcharts (Miro, Lucidchart)
- Spreadsheets (Balancing, Economy)

**4. Tools (Basic):**
- **Unity/Unreal:** Để prototype
- **Excel/Sheets:** Math, balancing
- **Figma:** UI mockups
- **Twine/Ink:** Narrative branching

---

### Soft Skills

**1. Communication:**
- Explain design decisions to devs, artists, stakeholders
- Give/receive feedback constructively

**2. Playtesting & Iteration:**
- Observe players (Đừng nói gì, chỉ quan sát họ chơi)
- Identify pain points
- Iterate quickly

**3. Empathy:**
- Understand target audience (Casual vs Hardcore gamers)
- Design for accessibility (Colorblind mode, difficulty options)

---

## 3. Learning Path (0-24 tháng)

### Phase 1: Foundations (Month 1-3)

**Objective:** Hiểu "What is good game design?"

#### **A. Read Core Books**
- [ ] **The Art of Game Design: A Book of Lenses** (Jesse Schell) - *Must read #1*
- [ ] **Rules of Play** (Katie Salen) - Game design theory
- [ ] **Theory of Fun** (Raph Koster) - Why games are fun

#### **B. Analyze Games Critically**
Chơi 5-10 games từ genres khác nhau, viết analysis:
- **Core loop:** Player làm gì lặp đi lặp lại?
- **Progression:** Unlock gì khi level up?
- **Hooks:** Game giữ chân player như thế nào?

**Template:**
```
Game: Vampire Survivors
Genre: Roguelike, Auto-shooter
Core Loop: Move → Kill enemies → Collect XP → Level up → Choose upgrade
Hooks: 
- 30-minute runs (Perfect lunch break)
- Power fantasy (One-shot thousands of enemies)
- Build variety (100+ synergies)
```

#### **C. Learn Basic Unity**
- [ ] Unity Learn: *Creator Kit: Puzzle* (Drag-and-drop, no code)
- [ ] Basic scripting (C# fundamentals)
- Goal: Prototype simple ideas

---

### Phase 2: Practice & Build (Month 4-9)

**Objective:** Create portfolio pieces

#### **A. Write 3 Game Design Documents (GDD)**

**Template GDD:**
```markdown
# Game Title: [Name]

## High Concept (1 sentence pitch)
"Flappy Bird meets Dark Souls"

## Core Loop
Player does X every second
Player does Y every minute  
Player does Z every hour

## Mechanics
1. Jump (Space bar, hold for higher jump)
2. Dash (Shift, 3-second cooldown)
3. Collect coins (Increase score, unlock skins)

## Progression
- Level 1-5: Tutorial (Learn basic mechanics)
- Level 6-10: Difficulty spike (Introduce enemies)
- Level 11-20: Mastery (Complex patterns)

## Economy
- Coins earned: 10 per enemy
- Skins cost: 100-500 coins
- Power-ups: 50 coins (temporary)

## Target Audience
- Age: 13-25
- Platform: Mobile
- Session length: 5-10 minutes
```

**3 GDD Ideas (Diverse genres):**
1. Puzzle game (Mobile casual)
2. Action RPG (PC/Console)
3. Multiplayer competitive (Esports potential)

---

#### **B. Prototype 2-3 Mechanics**

Không cần graphics đẹp, chỉ cần playable.

**Example projects:**
1. **Grappling Hook Mechanic**
   - Player swings like Spider-Man
   - Focus: Feel (Arc, speed, momentum)
   
2. **Card-based Combat**
   - Draw cards, play combos
   - Focus: Strategy depth vs Simplicity

3. **Procedural Level Generation**
   - Infinite runner with random obstacles
   - Focus: Fair difficulty curve

**Tools:**
- Unity + C# (Or Bolt/PlayMaker visual scripting)
- Upload to Itch.io với video walkthrough

---

#### **C. Join 2 Game Jams**

**Why Game Jams:**
- Learn to scope (48 hours = ruthless prioritization)
- Team collaboration (Work với devs/artists)
- Portfolio pieces (Even failed jams = learning)

**Popular Jams:**
- **Ludum Dare** (3 times/year)
- **Global Game Jam** (January)
- **GMTK Jam** (Theme-based, July)

**Your role:** Designer (Write GDD, playtest, iterate)

---

### Phase 3: Specialize & Go Pro (Month 10-24)

**Objective:** Become hireable in 1 specific area

Pick **1-2 specializations** (See Section 4).

#### **A. Deep Dive**
- Read advanced books/courses
- Recreate famous game mechanics (VD: "Replicate Hades' boon system")
- Build 1 "flagship" portfolio piece

#### **B. Networking**
- Attend local game dev meetups (VN: VGDC, GameDev VN)
- Join Discord communities (r/gamedesign, IGDA)
- Twitter: Follow designers, share learnings

#### **C. Apply for Jobs**
- See Section 7 (Getting Hired)

---

## 4. Specializations

Game Design có nhiều nhánh. Chọn 1-2 để master:

### A. Level Designer

**Focus:** Design maps, missions, quests.

**Skills:**
- Spatial thinking (Architecture, pacing)
- Tools: Unity ProBuilder, Unreal Editor
- Understanding player flow (Where do eyes look? Where to guide?)

**Games to study:**
- *Half-Life 2* (Tutorial integration)
- *The Last of Us* (Environmental storytelling)
- *Celeste* (Difficulty curve)

**Portfolio:**
- 3-5 levels (Different moods: Tutorial, Action, Puzzle)
- Video walkthrough explaining design choices

**Job titles:**
- Level Designer
- Mission Designer (Open-world games)
- Quest Designer (RPGs)

---

### B. Systems Designer

**Focus:** Combat, progression, crafting, AI.

**Skills:**
- Math & spreadsheets (Damage formulas, XP curves)
- Balancing (Rock-paper-scissors dynamics)
- Scripting (To prototype systems)

**Games to study:**
- *Diablo 3* (Loot 2.0, difficulty scaling)
- *Dark Souls* (Combat depth)
- *Path of Exile* (Skill tree complexity)

**Portfolio:**
- Design docs với math breakdowns
- Spreadsheet showing balance (VD: "Weapon DPS progression L1-50")
- Prototype system playable

**Job titles:**
- Systems Designer
- Combat Designer
- Progression Designer

---

### C. Narrative Designer

**Focus:** Story, characters, dialogue, quests.

**Skills:**
- Writing (Dialogue, branching narratives)
- Tools: Twine, Ink, Articy Draft
- Understanding pacing (3-act structure)

**Games to study:**
- *The Witcher 3* (Quest design)
- *Disco Elysium* (Dialogue systems)
- *Life is Strange* (Choice consequences)

**Portfolio:**
- 1-2 branching narrative prototypes (Twine)
- Character backstories
- Quest design docs

**Job titles:**
- Narrative Designer
- Writer
- Quest Designer

---

### D. Economy Designer

**Focus:** F2P monetization, gacha rates, shop pricing.

**Skills:**
- Data analysis (A/B testing, KPIs)
- Psychology (Sunk cost, FOMO)
- Spreadsheets (Currency sinks vs faucets)

**Games to study:**
- *Genshin Impact* (Gacha, battle pass)
- *Clash of Clans* (Timers, gems)
- *Fortnite* (Battle Pass design)

**Portfolio:**
- Economy model spreadsheet (Show currency flow)
- Monetization design doc (Ethical F2P)
- Case study: "How I'd improve [Game X]'s economy"

**Job titles:**
- Economy Designer
- Monetization Designer
- LiveOps Designer

---

### E. UX/UI Designer (Game-focused)

**Focus:** Menus, HUD, onboarding, tutorials.

**Skills:**
- UI/UX principles (Clarity, consistency, feedback)
- Tools: Figma, Adobe XD
- Understanding accessibility

**Games to study:**
- *God of War 2018* (Minimal HUD)
- *Dead Space* (Diegetic UI)
- *Hearthstone* (Mobile-friendly UX)

**Portfolio:**
- Redesign existing game UI (Before/After mockups)
- Prototype in Unity
- Usability test results

**Job titles:**
- UI/UX Designer
- UX Designer (Games)

---

## 5. Portfolio Building

### Portfolio Structure

**Your Portfolio Website (Must-have):**

```
yourname.com/

Pages:
1. Home
   - Intro: "Game Designer specialized in [X]"
   - Featured projects (3 best)

2. Projects
   - Each project: 
     - Title, Genre, Role
     - Challenge, Solution, Result
     - GDD link, Prototype link, Video

3. About
   - Background, Passion for games
   - Skills, Tools

4. Contact
   - Email, LinkedIn, Twitter
```

**Tools:**
- **Wix/Squarespace** (No code)
- **Webflow** (More customization)
- **GitHub Pages + Jekyll** (Free, for developers)

---

### Sample Project Page

**Title:** "Rogue Dash - Roguelike Platformer"

**Role:** Solo Designer + Developer

**Challenge:**
*"How to create replayability in a platformer? Players usually beat it once and quit."*

**Solution:**
- Procedural level generation (Every run unique)
- Roguelike meta-progression (Unlock permanent abilities)
- Daily challenge leaderboard (Social competition)

**Result:**
- Playtesters averaged 3.5 hours (vs 1-hour typical platformer)
- 80% said they'd replay
- Itch.io: 500 downloads, 4.2/5 stars

**Links:**
- [Play on Itch.io](#)
- [GDD (PDF)](#)
- [Devlog (YouTube)](#)

---

## 6. Career Path & Salary

### Seniority Levels

| Level | Years | Responsibilities | VN Salary (2026) |
|-------|-------|-----------------|------------------|
| **Junior Designer** | 0-2 | Execute tasks, assist seniors | 8-15M VND/m |
| **Designer** | 2-4 | Own features, mentor juniors | 15-25M VND/m |
| **Senior Designer** | 4-7 | Lead systems, cross-team collaboration | 25-40M VND/m |
| **Lead Designer** | 7-10 | Vision, manage team, stakeholder communication | 40-60M VND/m |
| **Creative Director** | 10+ | Game vision, company strategy | 60M+ VND/m |

**Note:** AAA studios (VNG, Gameloft) trả cao hơn. Indie studios thấp hơn nhưng creative freedom lớn.

---

### Typical Day (Mid-Level Designer)

**9:00 AM:** Standup (What did yesterday, today, blockers)  
**9:30 AM:** Review playtesting feedback from QA  
**11:00 AM:** Iterate enemy AI behavior (Tweak aggro range in spreadsheet)  
**12:00 PM:** Lunch  
**1:00 PM:** Meeting với Art team về new weapon visuals  
**2:00 PM:** Write design doc for boss fight mechanics  
**4:00 PM:** Prototype in Unity (Test boss attack patterns)  
**5:00 PM:** Playtest session (Watch testers, take notes)  
**6:00 PM:** Wrap up, plan tomorrow

---

## 7. Getting Hired

### A. Resume for Designers

**Different from Developer resume:**

**KHÔNG cần:**
- GitHub (Unless you code)
- LeetCode skills

**CẦN:**
- **Portfolio link** (Top of resume)
- **Games played** (Shows passion + knowledge)
- **Relevant projects** (Focus on design decisions, not code)

**Sample:**
```
[Your Name]
Game Designer | Systems & Economy Specialist
Portfolio: yourname.com | Email | LinkedIn

SUMMARY
Game designer with 3 years experience in F2P mobile games. 
Specialized in economy design and player retention systems.

EXPERIENCE

Economy Designer | [Mobile Game Studio] | 2023-Present
• Designed battle pass system increasing revenue 25% ($500k ARR)
• Balanced in-game economy serving 1M+ DAU
• A/B tested gacha rates, improved conversion 15%

Game Designer (Contract) | [Indie Studio] | 2022-2023
• Designed core combat system for roguelike game
• Iterated through 50+ playtests, improved retention 2x
• Wrote 100-page GDD used by 5-person team

SKILLS
Design: Systems Design, Economy, Progression, Balancing
Tools: Unity, Excel, Miro, Figma, Twine
Specialties: F2P Monetization, Player Psychology

PROJECTS
[Project 1]: Roguelike Deckbuilder [Itch.io | GDD]
[Project 2]: Economy Redesign Case Study [PDF]

EDUCATION
BS Game Design | [University] | 2022
```

---

### B. Interview Process

**Round 1: Portfolio Review (30-60 phút)**
- Recruiter reviews portfolio
- Questions:
  - "Walk me through your favorite project"
  - "How did you handle negative playtest feedback?"

**Round 2: Design Exercise (Take-home)**
- Example tasks:
  - "Design a new hero for [Our Game]"
  - "How would you improve player retention in [Scenario]?"
  - "Balance this weapon set (Spreadsheet provided)"

**Time:** 3-6 hours (Respect your time, don't spend 20h)

**Round 3: Onsite (Virtual)**

**3a) Design Deep Dive (60 phút)**
- Present your take-home exercise
- Defend decisions
- They challenge you: "What if players abuse this mechanic?"

**3b) Game Critique (30 phút)**
- "What game did you recently play? What would you change?"
- Tests: Analytical thinking, Communication

**3c) Cultural Fit (30 phút)**
- STAR method (See behavioral interview guides)

---

### C. Common Interview Questions

**1. "Describe your design process."**

**Good answer:**
```
1. Research: Understand player pain points, competitor analysis
2. Ideation: Brainstorm 10+ solutions, narrow to 3
3. Prototype: Build quick & dirty version
4. Playtest: Observe 5-10 players, gather data
5. Iterate: Refine based on feedback
6. Ship: Handoff to dev with clear doc
7. Monitor: Track KPIs post-launch, iterate
```

**2. "How do you balance difficulty?"**

**Good answer:**
```
- Flow theory: Match challenge to player skill
- Playtesting: Observe where players get stuck
- Data: Track failure rates (>50% = too hard, <10% = too easy)
- Options: Difficulty settings, dynamic difficulty adjustment
- Example: In my platformer, I reduced spike damage 20% after 
  seeing 60% of playtesters quit at level 3
```

**3. "Tell me about a design that failed."**

**Good answer (STAR method):**
```
Situation: I designed a crafting system for survival game
Task: Players should feel rewarded for exploration
Action: I made rare materials spawn randomly (Low %)
Result: Playtesters hated RNG. Felt unfair.
Learning: I redesigned to fixed spawn locations (High effort, 
guaranteed reward). Satisfaction jumped 40%.
```

---

## 8. Resources

### Books (Must-Reads)

**Beginner:**
- **The Art of Game Design** (Jesse Schell)
- **Rules of Play** (Katie Salen)
- **A Theory of Fun** (Raph Koster)

**Advanced:**
- **Game Feel** (Steve Swink) - Juiciness
- **Level Up!** (Scott Rogers) - Practical tips
- **Designing Games** (Tynan Sylvester) - Rimworld creator

---

### Online Courses

**Free:**
- **Game Design Concepts** (Ian Schreiber) - MIT OpenCourseWare
- **Unity Learn** - Prototyping tracks

**Paid:**
- **Coursera: Game Design Specialization** (CalArts)
- **Udemy: Complete Game Design Course** (Discount often $15)

---

### Communities

**Discord:**
- GMTK Discord (10k+ designers)
- r/gamedesign Discord

**Forums:**
- Designer Notes (Soren Johnson's blog)
- Gamasutra/GameDeveloper.com

**Local (Vietnam):**
- VGDC (Vietnam Game Developers Community)
- GameDev VN (Facebook group)

---

### Podcasts

- **Game Maker's Notebook** (Interviews với designers)
- **Designer Notes** (Deep dives)
- **The Game Design Round Table**

---

## 🎯 Action Plan (Next 30 Days)

**Week 1:**
- [ ] Read *Art of Game Design* (Lenses 1-25)
- [ ] Analyze 2 games you love (Write critique)
- [ ] Setup portfolio website (Basic structure)

**Week 2:**
- [ ] Unity Learn: Creator Kit tutorial
- [ ] Write first GDD (Mobile puzzle game)
- [ ] Join r/gamedesign Discord

**Week 3:**
- [ ] Prototype 1 simple mechanic (Unity)
- [ ] Playtest with 3 friends (Record feedback)
- [ ] Iterate based on feedback

**Week 4:**
- [ ] Polish prototype
- [ ] Upload to Itch.io
- [ ] Write project case study for portfolio
- [ ] Register for next Game Jam

---

## 🎯 Kết luận

**Game Designer khác Game Developer:**
- **Developer:** Code mechanics
- **Designer:** Create experiences

**Success Formula:**
```
Play Many Games + Analyze Critically + Prototype Fast + 
Iterate Based on Feedback + Communicate Clearly = 
Great Game Designer
```

**Start today:**
1. Play a game for 30 minutes
2. Write 3 things you'd change (Design perspective)
3. Prototype 1 idea this weekend

**Good luck! 🎮**

---

## 📖 Related Guides

- [Game Dev Roadmap](../../domains/game-dev/README.md) - For programming side
- [Game Theory](./game-theory.md) - Strategic thinking
- [Systems Thinking](./systems-thinking-in-life.md) - Mental models
