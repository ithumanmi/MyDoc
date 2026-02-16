# 🎯 Game Theory for Engineers: Applied Guide

> [← Back to Game Theory Basics](./game-theory.md) | [Systems Thinking](../../chapters/09-systems-thinking.md) | [Home](../../README.md)

Ứng dụng thực tế của Game Theory vào Career, System Design, và Team Dynamics trong ngành Tech.

---

## 📋 Mục lục

1. [Tại sao Engineers cần Game Theory?](#1-tại-sao-engineers-cần-game-theory)
2. [Salary Negotiation](#2-salary-negotiation-đàm-phán-lương)
3. [System Design as Game Theory](#3-system-design-as-game-theory)
4. [Team Dynamics & Conflict Resolution](#4-team-dynamics--conflict-resolution)
5. [Career Decisions](#5-career-decisions-quyết-định-nghề-nghiệp)
6. [Interview Strategy](#6-interview-strategy)
7. [Open Source & Community](#7-open-source--community)
8. [Practical Exercises](#8-practical-exercises)

---

## 1. Tại sao Engineers cần Game Theory?

### Game Theory ≠ Manipulation

**Hiểu lầm phổ biến:**
> *"Game Theory là về cách lừa người khác để thắng."*

**Sự thật:**
> *"Game Theory là về **hiểu tương tác** để tìm win-win solutions và tránh lose-lose outcomes."*

---

### Kỹ năng cốt lõi

Game Theory giúp Engineers:

1. **Negotiate better:** Salary, deadlines, scope.
2. **Design robust systems:** Anticipate failure modes.
3. **Collaborate effectively:** Understand team incentives.
4. **Make career decisions:** Startup vs Big Tech, skill investment.

---

## 2. Salary Negotiation (Đàm phán lương)

### 2.1. The Negotiation Game

**Players:**
- **Bạn:** Maximize salary + benefits.
- **Employer:** Minimize cost, maximize value.

**Strategies:**
- **Accept:** Nhận offer ngay.
- **Counter:** Đề xuất mức cao hơn.
- **Walk away:** Từ chối offer.

**Information:**
- **Asymmetric:** Employer biết budget, bạn không.
- **Your goal:** Giảm information gap.

---

### 2.2. Key Concepts

#### **A. BATNA (Best Alternative To Negotiated Agreement)**

**Định nghĩa:** Lựa chọn tốt nhất nếu không đạt thỏa thuận.

**Ví dụ:**
```
Offer A: $1500 (Current offer)
BATNA: Offer B: $1200 (Backup offer)
→ You can walk away if A < $1200
```

**Power:**
- **Strong BATNA** (Nhiều offers) → Negotiate aggressive.
- **Weak BATNA** (Không có backup) → Phải cẩn thận.

**Tactic:** Luôn tạo BATNA (Apply nhiều công ty).

---

#### **B. Anchoring Effect**

**Định nghĩa:** Số đầu tiên "neo" toàn bộ negotiation.

**Ví dụ:**
```
Scenario 1: Employer anchor
- Employer: "Budget is $1000"
- You: "I expect $1500" → Settle at $1200

Scenario 2: You anchor
- You: "I expect $2000"
- Employer: "We can do $1500" → Settle at $1700
```

**Rule:** Ai anchor trước có lợi → **Bạn nên anchor trước** (nếu có research).

**Optimal Anchor:** Market rate + 10-20%.

---

#### **C. Reservation Price**

**Định nghĩa:** Mức thấp nhất bạn chấp nhận.

**Example:**
```
Your target: $1500
Reservation price: $1200 (Below this → Walk away)
```

**Never reveal reservation price!** Employer sẽ offer đúng mức đó.

---

### 2.3. Real-world Scenarios

#### **Scenario 1: First Job Offer**

**Situation:**
- Offer: $800/month (Junior Backend Dev, Vietnam).
- Market rate: $600-$1000.
- No other offers.

**Payoff Matrix:**
```
                Employer
            Accept | Reject
You    ─────────────┼────────
Accept │   800, -800│    -
Counter│ 900?, -900?│ 0, 0 (No deal)
        │  or 0, 0  │
```

**Strategy:**
1. **Research:** Glassdoor, Levels.fyi → $800 is high.
2. **Counter:** "I appreciate the offer. Based on my skills (Node.js, TypeScript, AWS), I was expecting $900. Can we meet at $850?"
3. **Justify:** Không counter vô căn cứ → Đưa evidence (Skills, market rate).

**Likely outcome:** $800-$850 (Employer rarely reject over $50).

---

#### **Scenario 2: Multiple Offers**

**Situation:**
- Offer A: $1500/month (Big Corp, boring work).
- Offer B: $1200/month (Startup, exciting work, equity).

**Game:** Sử dụng A để negotiate B.

**Script:**
```
Email to B:
"Hi [Recruiter], I'm very excited about [Startup]. However, 
I have another offer at $1500. I prefer your company, but 
the compensation gap is significant. Can we discuss?"
```

**Possible outcomes:**
1. B raises to $1400 + equity → You win.
2. B keeps $1200 → You choose based on priorities.
3. A hears you're negotiating → May sweeten deal.

**Key:** Frame as "I want to join you" not "I'm using you".

---

#### **Scenario 3: Internal Promotion**

**Situation:**
- Current: $1000/month.
- Promoted to Senior → Expect $1500.
- Manager offers $1200.

**Mistake:** Accept vì "đã được promote".

**Strategy:**
1. **Research:** Senior rate is $1400-$1600.
2. **Counter:** "I'm grateful for the promotion. However, market rate for Senior Backend in Hanoi is $1500. Given my contributions (List achievements), can we match that?"
3. **BATNA:** Nếu refuse → Apply external (Leverage outside offers).

---

### 2.4. Advanced Tactics

#### **A. The Flinch**

Khi Employer đưa số → **Flinch** (Giật mình, im lặng 3 giây).

**Psychology:** Employer nghĩ "Offer quá thấp" → May raise spontaneously.

---

#### **B. Split the Difference**

```
You: $2000
Employer: $1500
Employer: "Let's split at $1750?"
You: "Hmm, how about $1850?" (Split again)
```

**Note:** Chỉ split nếu outcome acceptable.

---

#### **C. Non-salary Negotiations**

Nếu salary stuck → Negotiate:
- **Signing bonus:** $1000 one-time.
- **Remote work:** 2 days/week.
- **Learning budget:** $500/year for courses.
- **Early review:** 6 months instead of 1 year.

---

### 2.5. Common Mistakes

❌ **Mistake 1:** Accept first offer.
- Employer expect bạn counter → Offer thường có "padding".

❌ **Mistake 2:** Reveal current salary.
- "I'm making $800" → Employer anchor to $900 (not market rate $1500).
- **Response:** "I prefer to focus on market value for this role."

❌ **Mistake 3:** Bluff without BATNA.
- "I have another offer at $2000" (Lie) → Employer: "Take it."

❌ **Mistake 4:** Negotiate too hard.
- Employer rescinds offer → You lose everything.
- **Balance:** Assertive but respectful.

---

## 3. System Design as Game Theory

### 3.1. Load Balancing Game

**Game:**
- **Players:** N servers (S1, S2, ..., SN).
- **Requests:** 1000 req/s incoming.
- **Objective:** Distribute requests fairly.

**Selfish Strategy:**
```
If Server = Overloaded:
    Reject request (Save CPU)
Else:
    Accept request
```

**Nash Equilibrium (Without coordination):**
- All servers reject when slightly loaded → System crash.

**Solution: Load Balancer = "Game Master"**

**Algorithms:**

#### **A. Round Robin**
```
Request 1 → S1
Request 2 → S2
Request 3 → S3
Request 4 → S1 (repeat)
```

**Game Theory:** Enforce **fairness** (No server can "cheat").

---

#### **B. Least Connections**
```typescript
function getServer(servers: Server[]): Server {
  return servers.reduce((min, server) => 
    server.connections < min.connections ? server : min
  );
}
```

**Nash Equilibrium:** All servers have ~equal connections.

---

#### **C. Consistent Hashing**

**Game:** Cache servers compete for "hot" keys.

**Problem:** 
```
Key "user:123" always → Server A → A overloaded.
```

**Solution:** Distribute keys uniformly (Consistent hashing with virtual nodes).

---

### 3.2. Database Replication: Consensus Game

**Game:**
- **Players:** Master, Slave1, Slave2.
- **Challenge:** Agree on "current state" despite network partitions.

**Byzantine Generals Problem:**
- Generals (Nodes) want to attack together.
- Some generals may be traitors (Faulty nodes).
- **Goal:** Honest nodes agree on "Attack" or "Retreat".

**Solution: Raft Algorithm**

**Game Theory Applied:**
1. **Leader Election:** Nodes vote → Majority wins.
2. **Log Replication:** Leader sends logs → Followers ACK → Commit when majority ACK.

**Nash Equilibrium:** Follow the leader (Deviating = Inconsistency).

---

### 3.3. API Rate Limiting: Tragedy of the Commons

**Game:**
- **Players:** N clients using API.
- **Resource:** Server capacity (1000 req/s).
- **Selfish Strategy:** Each client sends max requests.

**Payoff:**
```
If Total Requests < 1000:
    All clients get fast response
Else:
    Server crashes → All clients get 0
```

**Nash Equilibrium (No rate limit):** 
- All clients spam → Server crash (Tragedy of the Commons).

**Solution: Rate Limiter**

**Implementation (Token Bucket):**
```typescript
class RateLimiter {
  private tokens: Map<string, number> = new Map();
  private limit = 100; // req/minute
  
  isAllowed(clientId: string): boolean {
    const now = Date.now();
    const clientTokens = this.tokens.get(clientId) || this.limit;
    
    if (clientTokens > 0) {
      this.tokens.set(clientId, clientTokens - 1);
      return true;
    }
    return false; // Reject
  }
  
  refill() {
    // Every minute, refill tokens
    setInterval(() => {
      this.tokens.forEach((_, clientId) => {
        this.tokens.set(clientId, this.limit);
      });
    }, 60000);
  }
}
```

**Game Theory:** Rate limiter = "Regulation" preventing tragedy.

---

### 3.4. Microservices: Prisoner's Dilemma

**Game:**
- **Service A** calls **Service B**.
- **Strategies:**
  - **Cooperate:** Respond quickly, handle errors gracefully.
  - **Defect:** Timeout, throw errors, don't retry.

**Payoff Matrix:**
```
              Service B
          Cooperate | Defect
Service A ──────────┼────────
Cooperate│  Good    │ A crashes
Defect   │ B crashes│ Both crash
```

**Nash Equilibrium (Without safeguards):** Both defect → Both crash (Cascade failure).

**Solution: Circuit Breaker**

```typescript
enum State { CLOSED, OPEN, HALF_OPEN }

class CircuitBreaker {
  private state = State.CLOSED;
  private failures = 0;
  private threshold = 5;
  
  async call(fn: Function) {
    if (this.state === State.OPEN) {
      throw new Error('Circuit OPEN - Service unavailable');
    }
    
    try {
      const result = await fn();
      this.onSuccess();
      return result;
    } catch (error) {
      this.onFailure();
      throw error;
    }
  }
  
  private onFailure() {
    this.failures++;
    if (this.failures >= this.threshold) {
      this.state = State.OPEN; // Stop calling Service B
      setTimeout(() => {
        this.state = State.HALF_OPEN; // Try again
      }, 30000);
    }
  }
  
  private onSuccess() {
    this.failures = 0;
    this.state = State.CLOSED;
  }
}
```

**Game Theory:** Break the Prisoner's Dilemma by "not playing" when opponent defects.

---

### 3.5. Caching Strategy: Evolutionary Game

**Game:**
- **Players:** Cache entries competing for limited space.
- **Strategies:** LRU, LFU, FIFO.

**LRU (Least Recently Used) = Evolutionary Stable Strategy:**
```
If Entry = Not accessed recently:
    Evict (Make room for new)
Else:
    Keep
```

**Why ESS?**
- If all entries follow LRU → No entry benefits from changing strategy.
- Hot data stays, cold data evicted → Optimal for most workloads.

---

## 4. Team Dynamics & Conflict Resolution

### 4.1. Code Review Conflicts

**Game:**
- **Players:** Junior Dev (Author) vs Senior Dev (Reviewer).
- **Strategies:**
  - Junior: Fix immediately, Argue back, Ignore.
  - Senior: Approve, Request changes, Reject harshly.

**Payoff Matrix:**
```
                Senior Reviewer
            Approve | Harsh Reject
Junior Dev ─────────┼──────────────
Fix Fast  │  2, 2   │   1, -1
Argue Back│  0, -1  │  -2, -2
```

**Nash Equilibrium:** Junior fixes fast, Senior approves → Win-win (2, 2).

**Toxic Equilibrium:** Junior argues, Senior rejects harshly → Both suffer (-2, -2).

---

**Best Practices (Mechanism Design):**

**For Junior:**
- "Thanks for the feedback. I'll update the PR."
- Ask questions if unclear: "Why is this approach better?"

**For Senior:**
- "Good work overall. Suggest changing X because Y."
- Approve with non-blocking comments.

**Result:** Cooperation becomes dominant strategy.

---

### 4.2. Feature Ownership: Chicken Game

**Scenario:**
- 2 developers, 1 complex feature (Authentication refactor).
- Both avoid it (Prefer easy features).

**Game:**
```
              Dev B
          Take it | Avoid
Dev A  ───────────┼───────
Take it│  -2, -2  │ -5, 0  (A does hard work)
Avoid  │   0, -5  │  0, 0  (Feature not done)
```

**Nash Equilibria:** (Take, Avoid) or (Avoid, Take).

**Problem:** Who "swerves" first?

**Solution (Mechanism Design):**
1. **Manager assigns:** Remove the game.
2. **Rotate ownership:** Fair over time (Repeated game).
3. **Incentivize:** Bonus for tackling hard features.

---

### 4.3. Meeting Participation: Free Rider Problem

**Game:**
- 5 engineers in meeting.
- **Strategies:** Contribute ideas vs Stay silent.

**Payoff:**
```
If Everyone contributes:
    Meeting productive (Value = 10)
    
If You stay silent, others contribute:
    You save energy (Value = 5 for you, 8 for team)
    
If Everyone silent:
    Meeting waste (Value = 0)
```

**Dominant Strategy:** Stay silent (Free ride on others' contributions).

**Nash Equilibrium:** Everyone silent → Meeting useless.

**Solutions:**

1. **Round-robin:** "Each person share 1 idea."
2. **Pre-meeting homework:** Everyone prepares → Sunk cost → More likely to share.
3. **Small groups:** Harder to hide in 3-person meeting.

---

### 4.4. On-call Rotation: Repeated Prisoner's Dilemma

**Game:**
- You and colleague rotate on-call weekly.
- **Strategies:** Help when asked vs Ignore.

**Payoff Matrix (Single round):**
```
                Colleague
            Help | Ignore
You    ──────────┼────────
Help   │  1, 1   │ -2, 2
Ignore │  2, -2  │  0, 0
```

**Single-shot Nash Equilibrium:** Both ignore (0, 0).

**BUT: This is a repeated game!**

**Tit-for-Tat Strategy:**
```
Round 1: Cooperate (Help)
Round N: Do what opponent did in Round N-1
```

**Result:**
- You help → Colleague helps back → Both help consistently (1, 1) every round.
- Colleague defects → You defect next round → They learn cooperation is better.

**Lesson:** Build reputation for cooperation in repeated interactions.

---

### 4.5. Promotion Competition: Non-zero-sum

**Common belief (Wrong):**
> *"Promotion is zero-sum: If you get promoted, I don't."*

**Reality:**
- If team performs well → Multiple promotions possible.
- **Cooperate** > Sabotage colleagues.

**Payoff:**
```
                Colleague
            Cooperate | Sabotage
You    ───────────────┼──────────
Cooperate│ Both promoted│ You lose
Sabotage │ You lose     │ Both lose
```

**Insight:** In most companies, helping colleagues → Better team results → You also benefit.

---

## 5. Career Decisions (Quyết định nghề nghiệp)

### 5.1. Startup vs Big Tech

**Payoff Matrix (Simplified):**
```
                   Success | Failure
Startup (Equity) │ $500k   │ $0 (Company dies)
Big Tech (Salary)│ $200k   │ $200k (Stable)
```

**Expected Value:**
```
Startup: 10% * $500k + 90% * $0 = $50k
Big Tech: 100% * $200k = $200k
```

**Rational choice:** Big Tech (Higher expected value).

**BUT: Consider non-monetary factors:**
- Learning: Startup = Wear many hats.
- Lifestyle: Big Tech = Better WLB.
- Risk tolerance: Young → Can afford risk.

**Mixed Strategy:** 
- 20s: Try startup (Low risk, high learning).
- 30s: Big Tech (Stability for family).

---

### 5.2. Skill Investment Game

**Scenario:**
- Limited time (10 hours/week).
- **Options:** Learn AI/ML vs System Design vs Cloud (AWS).

**Game Theory:**
- **Herding:** Everyone learns AI → Market saturated → Lower value.
- **Contrarian:** Learn undervalued skill (System Design) → Higher value.

**Strategy:**
1. **Research demand:** Job postings trend.
2. **First-mover advantage:** Learn emerging tech early (Blockchain in 2015, AI in 2018).
3. **Diversify:** 60% core skill, 40% emerging.

---

### 5.3. Job Hopping Frequency

**Game:**
- **Stay 6 months → Hop:** Bad reputation (Job hopper).
- **Stay 5 years:** Miss salary growth (Switching = 20-30% raise).

**Optimal Strategy (Empirical data):**
- **Junior (0-3 YOE):** 1.5-2 years per job.
- **Mid (3-7 YOE):** 2-3 years.
- **Senior (7+ YOE):** 3-5 years.

**Game Theory:** Build reputation for stability (Repeated game) → Better offers.

---

## 6. Interview Strategy

### 6.1. Salary Expectation Question

**Interviewer:** *"What's your salary expectation?"*

**Strategies:**

#### **Strategy A: Dodge (Optimal)**
```
"I'm flexible and prefer to focus on fit first. 
What's the budget for this role?"
```

**Game Theory:** Make employer anchor first.

---

#### **Strategy B: High Anchor**
```
"Based on my experience with [Skills], I'm targeting $X."
(X = Market rate + 20%)
```

**Risk:** May be filtered out if way above budget.

---

#### **Strategy C: Range**
```
"I'm looking at $1500-$2000, depending on total compensation."
```

**Problem:** Employer hears $1500 (low end).

**Better:** "$1800-$2000, flexible for equity/benefits."

---

### 6.2. Multiple Interview Rounds

**Game:** You vs Other candidates.

**Strategies:**
- **Overperform early:** Make strong first impression.
- **Ask smart questions:** Show genuine interest.
- **Follow-up:** Thank-you email (80% don't do this).

**Nash Equilibrium:** All candidates prepare hard → You must differentiate.

**Differentiators:**
- Portfolio (GitHub with clean projects).
- Contributions (Blog posts, Stack Overflow).
- Referrals (Warm intro > Cold apply).

---

## 7. Open Source & Community

### 7.1. Public Goods Game

**Game:**
- **Players:** Developers worldwide.
- **Strategies:** Contribute code vs Use only.

**Payoff:**
```
If All contribute:
    Rich ecosystem (Value = 10 for all)
    
If You don't contribute, others do:
    You save time (Value = 5), others get 8
    
If No one contributes:
    No tools (Value = 0)
```

**Dominant Strategy:** Free ride (Don't contribute).

**Reality:** Many still contribute! Why?

**Reasons (Beyond Game Theory):**
1. **Reputation:** GitHub profile → Job offers.
2. **Learning:** Contribute → Deep understanding.
3. **Reciprocity:** "I benefited, give back."
4. **Intrinsic motivation:** Enjoy coding.

**Lesson:** Humans ≠ Perfectly selfish (Behavioral Economics).

---

### 7.2. License Wars

**Game:** GPL (Copyleft) vs MIT (Permissive).

**GPL Strategy:**
- "You must open-source derivative works."
- **Payoff:** Prevents corporations from closing code.

**MIT Strategy:**
- "Do whatever you want."
- **Payoff:** Wider adoption (Corporations prefer).

**Trade-off:**
- GPL: Protects openness, limits adoption.
- MIT: Maximizes adoption, risk of corporate capture.

---

## 8. Practical Exercises

### Exercise 1: Salary Negotiation Simulation

**Scenario:**
- Offer: $1200/month (Backend Developer, Ho Chi Minh City).
- Market: $1000-$1500.
- You: 1 YOE, Node.js, PostgreSQL, Docker.
- No other offers.

**Task:**
1. What's your BATNA?
2. Draft counter-offer email.
3. Justify the counter.

**Sample Answer:**
```
BATNA: Stay at current job ($1000) or keep applying.

Email:
"Thank you for the offer. I'm excited about [Company]. 
However, based on market research (Levels.fyi shows $1400 median) 
and my experience with Node.js microservices and Docker deployments, 
I was expecting $1400. Can we meet at $1350?"
```

---

### Exercise 2: Load Balancer Game

**Scenario:**
- 3 servers: S1, S2, S3.
- Capacity: 100 req/s each.
- Incoming: 250 req/s.

**Task:**
1. Design algorithm to distribute.
2. What happens if S2 crashes?
3. Modify algorithm for fault tolerance.

**Sample Answer:**
```typescript
// Weighted Round Robin
const servers = [
  { id: 'S1', weight: 5, connections: 0 },
  { id: 'S2', weight: 3, connections: 0 },
  { id: 'S3', weight: 2, connections: 0 }
];

function getServer() {
  const server = servers.reduce((max, s) => 
    (s.weight - s.connections) > (max.weight - max.connections) ? s : max
  );
  server.connections++;
  return server;
}

// If S2 crashes: Health check + Remove from pool
```

---

### Exercise 3: Code Review Conflict

**Scenario:**
- Junior wrote nested ternary operators (Hard to read).
- Senior requests refactor.
- Junior: "It works, why change?"

**Task:** As Senior, draft response.

**Sample Answer:**
```
"Hey [Name], great work on the feature! The logic is correct, 
but nested ternaries can be tricky to debug. Here's a refactor 
using if-else that's easier to read:

[Code example]

This makes it easier for future maintainers (including yourself 
in 6 months 😄). Let me know if you have questions!"
```

---

## 🎯 Kết luận

### Key Takeaways

**1. Negotiation:**
- Always counter (Politely).
- Research + Anchor high.
- Create BATNA.

**2. System Design:**
- Distributed systems = Multiplayer games.
- Design incentives (Rate limiters, Circuit breakers).
- Anticipate selfish behavior.

**3. Team Dynamics:**
- Cooperation > Competition (Repeated games).
- Build reputation.
- Mechanism design for better equilibria.

**4. Career:**
- Think long-term (Repeated games).
- Diversify skills.
- Network = Create BATNAs.

---

### Final Thought

> *"Game Theory không dạy bạn 'thắng' trong mọi tình huống. Nó dạy bạn **hiểu** tương tác để tìm win-win, tránh lose-lose, và đưa ra quyết định rational dựa trên incentives."*

**Practice:** Nhìn mọi interaction qua lens Game Theory → Bạn sẽ đưa ra better decisions! 🚀

---

## 📚 Further Reading

- [Game Theory Basics](./game-theory.md) - Foundation concepts
- [Systems Thinking](../../chapters/09-systems-thinking.md) - Big picture view
- [Becoming Top 1%](./becoming-top-1-percent.md) - Career strategy
- [Personal Brand](../../chapters/08-personal-brand.md) - Reputation building
