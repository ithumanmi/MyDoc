# 🎲 Lý thuyết trò chơi (Game Theory): Hướng dẫn toàn diện

> [← Back to Systems Thinking](../../chapters/09-systems-thinking.md) | [Home](../README.md)

Khoa học về ra quyết định chiến lược khi kết quả phụ thuộc vào hành động của nhiều người.

---

## 📋 Mục lục

1. [Game Theory là gì?](#1-game-theory-là-gì)
2. [Các khái niệm cốt lõi](#2-các-khái-niệm-cốt-lõi)
3. [Các loại trò chơi](#3-các-loại-trò-chơi)
4. [Chiến lược & Nash Equilibrium](#4-chiến-lược--nash-equilibrium)
5. [Các game kinh điển](#5-các-game-kinh-điển)
6. [Ứng dụng thực tế](#6-ứng-dụng-thực-tế)
7. [Game Theory trong đời sống](#7-game-theory-trong-đời-sống)
8. [Resources](#8-resources)

---

## 1. Game Theory là gì?

### Định nghĩa

**Game Theory** (Lý thuyết trò chơi) là ngành toán học nghiên cứu **tương tác chiến lược** giữa các "người chơi" (players) có mục tiêu riêng.

> *"Mathematics of strategic decision-making when your outcome depends on what others do, and they know you know that."*

---

### Tại sao quan trọng?

Game Theory giải thích:
- **Tại sao** các công ty cạnh tranh hạ giá đến khi cả 2 đều lỗ?
- **Tại sao** các quốc gia vũ trang dù không muốn chiến tranh?
- **Tại sao** bạn và đối tác khó tin tưởng nhau dù cùng có lợi?

**Insight:** Rational individual choices ≠ Optimal collective outcome.

---

### Lịch sử

- **1944:** John von Neumann & Oskar Morgenstern xuất bản *"Theory of Games and Economic Behavior"*.
- **1950:** John Nash phát triển **Nash Equilibrium** (Nobel Prize 1994).
- **Ngày nay:** Ứng dụng trong Economics, Politics, Biology, AI, Blockchain.

---

## 2. Các khái niệm cốt lõi

### 2.1. Players (Người chơi)

Các cá nhân/tổ chức tham gia game, mỗi player có:
- **Objective (Mục tiêu):** Maximize profit, minimize loss.
- **Rationality (Tính lý trí):** Chọn chiến lược tối ưu dựa trên thông tin.

**Ví dụ:** Viettel vs Mobifone (2 players cạnh tranh thị trường di động).

---

### 2.2. Strategies (Chiến lược)

Tập hợp các hành động có thể:
- **Pure Strategy:** Chọn 1 action cố định (VD: Luôn hợp tác).
- **Mixed Strategy:** Chọn ngẫu nhiên theo xác suất (VD: 70% hợp tác, 30% phản bội).

---

### 2.3. Payoffs (Lợi ích)

Kết quả nhận được từ combo chiến lược của tất cả players.

**Payoff Matrix (2 players):**
```
                Player B
            Strategy 1 | Strategy 2
Player A  ─────────────┼────────────
Strategy 1 │   (a, b)   │   (c, d)
Strategy 2 │   (e, f)   │   (g, h)
```

- `(a, b)`: Player A nhận `a`, Player B nhận `b`.

---

### 2.4. Information (Thông tin)

**Perfect Information:** Biết tất cả nước đi trước đó (Cờ vua).  
**Imperfect Information:** Không biết hết (Poker - không thấy bài người khác).

---

## 3. Các loại trò chơi

### 3.1. Cooperative vs Non-cooperative

**Cooperative Game:**
- Players có thể thỏa thuận ràng buộc (contracts).
- **Ví dụ:** 2 công ty merge thành 1.

**Non-cooperative Game:**
- Mỗi người tự quyết định, không có contract.
- **Ví dụ:** Đấu giá, cạnh tranh thị trường.

---

### 3.2. Zero-sum vs Non-zero-sum

**Zero-sum Game:**
- Tổng lợi ích của tất cả players = 0.
- Thắng của người này = Thua của người kia.
- **Ví dụ:** Poker (Tiền bạn thắng = Tiền tôi thua).

**Non-zero-sum Game:**
- Có thể cùng thắng hoặc cùng thua.
- **Ví dụ:** Prisoner's Dilemma (Cả 2 hợp tác → Cùng ít thua).

---

### 3.3. Sequential vs Simultaneous

**Sequential Game:**
- Players lần lượt đi, biết nước đi trước.
- **Ví dụ:** Cờ vua, Checkers.
- **Tool:** Game Tree, Backward Induction.

**Simultaneous Game:**
- Players chọn đồng thời, không biết lựa chọn của nhau.
- **Ví dụ:** Rock-Paper-Scissors, Prisoner's Dilemma.
- **Tool:** Payoff Matrix.

---

## 4. Chiến lược & Nash Equilibrium

### 4.1. Dominant Strategy

**Định nghĩa:** Chiến lược tốt nhất **bất kể** người khác làm gì.

**Ví dụ: Prisoner's Dilemma**
```
                Tù nhân B
            Im lặng | Khai báo
Tù nhân A ─────────┼──────────
Im lặng   │ -1, -1  │ -10, 0
Khai báo  │  0, -10 │  -5, -5
```

**Phân tích cho Tù nhân A:**
- Nếu B im lặng → A khai (0 > -1).
- Nếu B khai → A khai (-5 > -10).
- **Dominant Strategy cho A:** Khai báo.

Tương tự cho B → **Cả 2 đều khai** dù hợp tác tốt hơn.

---

### 4.2. Nash Equilibrium

**Định nghĩa:** Trạng thái mà **không ai muốn thay đổi** chiến lược nếu người khác giữ nguyên.

**Công thức:**
> Strategy profile (s₁*, s₂*) is Nash Equilibrium if:
> - s₁* is best response to s₂*
> - s₂* is best response to s₁*

**Ví dụ: Battle of the Sexes**
```
Cặp đôi muốn đi chơi cùng nhau nhưng sở thích khác:

               Vợ
          Opera | Football
Chồng  ────────┼──────────
Opera  │  2, 1  │  0, 0
Football│ 0, 0  │  1, 2
```

**Nash Equilibria:** 
1. Cả 2 đi Opera (2, 1).
2. Cả 2 đi Football (1, 2).

**Insight:** Có 2 equilibria → Cần **coordination** (thỏa thuận trước).

---

### 4.3. Tìm Nash Equilibrium

**Bước 1:** Vẽ Payoff Matrix.  
**Bước 2:** Với mỗi player, tìm best response cho từng chiến lược của đối thủ.  
**Bước 3:** Cell nào cả 2 đều là best response = Nash Equilibrium.

**Ví dụ: Matching Pennies**
```
           Player B
         Heads | Tails
Player A ──────┼──────
Heads   │ 1, -1│ -1, 1
Tails   │ -1, 1│  1, -1
```

**Kết quả:** **Không có** Pure Strategy Nash Equilibrium.  
**Mixed Strategy Equilibrium:** Mỗi người chọn 50% Heads, 50% Tails.

---

## 5. Các game kinh điển

### 5.1. Prisoner's Dilemma (Tiến thoái lưỡng nan)

**Setup:**
2 tội phạm bị bắt, thẩm vấn riêng:
- Cả 2 im lặng → Mỗi người 1 năm tù.
- 1 khai, 1 im → Người khai tự do, người im 10 năm.
- Cả 2 khai → Mỗi người 5 năm.

**Nash Equilibrium:** Cả 2 khai (-5, -5).  
**Pareto Optimal:** Cả 2 im (-1, -1).

**Bài học:** Individual rationality → Collective irrationality.

---

### 5.2. Chicken Game (Trò chơi con gà)

**Setup:**
2 xe ô tô lao vào nhau:
- **Swerve (Tránh):** Nhút nhát.
- **Straight (Lao thẳng):** Dũng cảm.

```
              Player B
          Swerve | Straight
Player A ────────┼──────────
Swerve  │  0, 0  │ -1, 1
Straight│  1, -1 │ -10, -10
```

**Nash Equilibria:** (Swerve, Straight) hoặc (Straight, Swerve).  
**Insight:** Ai cam kết "Straight" trước sẽ thắng (Commitment strategy).

**Ứng dụng:** Đàm phán quốc tế (ai nhượng bộ trước?).

---

### 5.3. Stag Hunt (Săn nai)

**Setup:**
2 thợ săn:
- Cùng săn **Nai** → Mỗi người 5 kg thịt (phải hợp tác).
- Săn **Thỏ** → 2 kg thịt (làm 1 mình được).

```
             Hunter B
          Stag | Hare
Hunter A ──────┼──────
Stag    │ 5, 5 │ 0, 2
Hare    │ 2, 0 │ 2, 2
```

**Nash Equilibria:** (Stag, Stag) hoặc (Hare, Hare).  
**Insight:** Cả 2 equilibria, nhưng (Stag, Stag) tốt hơn → Cần **trust**.

---

### 5.4. Tragedy of the Commons (Bi kịch của cái chung)

**Setup:**
10 người cùng dùng 1 cánh đồng chung:
- Mỗi người có 10 con cừu, đồng chịu tối đa 100 con.
- Nếu ai cũng thả 10 con → OK (100 con).
- Nếu 1 người thả 20 con → Người đó lời, đồng vẫn OK.
- Nếu ai cũng thả 20 con → Đồng chết (200 > 100).

**Nash Equilibrium:** Ai cũng thả 20 con → Đồng chết.  
**Bài học:** Không ai có incentive để giảm → Cần **regulation**.

**Real-world:** Overfishing, Climate change, Traffic congestion.

---

### 5.5. Ultimatum Game

**Setup:**
- Player A chia $100.
- Player B chọn Accept/Reject.
- Nếu Reject → Cả 2 nhận $0.

**Rational Prediction:**
- A offer $1, giữ $99.
- B Accept (vì $1 > $0).

**Reality:**
- Offers < $30 thường bị Reject.
- **Lý do:** Fairness, Punishment (B sẵn sàng mất tiền để trừng phạt A).

**Bài học:** People aren't perfectly rational (Behavioral Economics).

---

## 6. Ứng dụng thực tế

### 6.1. Kinh tế & Kinh doanh

#### **A. Price Competition (Cạnh tranh giá)**

**Ví dụ: Grab vs Gojek**
```
             Gojek
          Giá thấp | Giá cao
Grab   ─────────────┼──────────
Giá thấp│  -2, -2  │   5, -1
Giá cao │  -1, 5   │   2, 2
```

**Nash Equilibrium:** Cả 2 giá thấp → Cả 2 lỗ (Price war).  
**Giải pháp:** Collude (Thỏa thuận ngầm giữ giá) → Bất hợp pháp (Anti-trust law).

---

#### **B. Auctions (Đấu giá)**

**First-price Auction:**
- Bid cao nhất thắng, trả đúng giá bid.
- **Strategy:** Bid thấp hơn valuation (để lời).

**Second-price Auction (Vickrey):**
- Bid cao nhất thắng, trả giá của bid thứ 2.
- **Dominant Strategy:** Bid đúng valuation của bạn.
- **Ứng dụng:** Google Ads, eBay.

---

### 6.2. Chính trị & Quan hệ quốc tế

#### **A. Arms Race (Cuộc đua vũ trang)**

**Cold War: Mỹ vs Liên Xô**
```
              USSR
          Arm | Disarm
USA   ────────┼────────
Arm   │ -3, -3│  2, -5
Disarm│ -5, 2 │  0, 0
```

**Nash Equilibrium:** Cả 2 Arm (-3, -3).  
**Pareto Optimal:** Cả 2 Disarm (0, 0).

**Giải pháp:** Arms control treaties (INF, START).

---

#### **B. Voting (Bầu cử)**

**Strategic Voting:**
- Bạn thích A > B > C.
- Nhưng A không thắng được → Vote cho B để chặn C.

**Arrow's Impossibility Theorem:** Không có voting system hoàn hảo.

---

### 6.3. Sinh học & Tiến hóa

#### **Hawk-Dove Game**

Động vật tranh giành thức ăn:
- **Hawk:** Đánh nhau (thắng: +50, thua: -100).
- **Dove:** Tránh (chia đều: +25).

```
           Opponent
         Hawk | Dove
You  ─────────┼──────
Hawk │ -25, -25│ 50, 0
Dove │  0, 50  │ 25, 25
```

**Evolutionary Stable Strategy (ESS):** Mixed population (vài Hawk, nhiều Dove).

---

### 6.4. Công nghệ & AI

#### **A. Blockchain & Consensus**

**Byzantine Generals Problem:**
- N generals muốn tấn công cùng lúc.
- Một số generals có thể là traitor.
- **Game Theory:** Thiết kế incentive để honesty là dominant strategy.
- **Giải pháp:** Proof of Work (Bitcoin), Proof of Stake (Ethereum).

---

#### **B. Network Effects**

**Platform Competition:**
- Facebook vs Google+ → User ở nơi có nhiều user khác.
- **Nash Equilibrium:** Tất cả ở 1 platform → Winner-takes-all.

---

## 7. Game Theory trong đời sống

### 7.1. Đàm phán lương (Salary Negotiation)

**Setup:**
- Bạn: Muốn $2000.
- Employer: Muốn trả $1500.

**Strategies:**
- **Lowball:** Bạn đưa offer $1600 → Employer accept ngay.
- **Highball:** Bạn đưa $2500 → Employer counter $1800.

**Insight:** Ai anchor trước (đưa số đầu tiên) sẽ có lợi.

---

### 7.2. Traffic (Giao thông)

**Game:** Ai cũng muốn lấn làn để đi nhanh hơn.

**Nash Equilibrium:** Ai cũng lấn làn → Kẹt xe (tệ cho tất cả).  
**Solution:** Traffic rules + Enforcement.

---

### 7.3. Group Projects (Dự án nhóm)

**Free Rider Problem:**
- 4 người làm nhóm.
- Nếu ai cũng làm → Điểm A.
- Nếu 1 người lười, 3 người làm → 1 người lười cũng được A.

**Nash Equilibrium:** Ai cũng lười → Điểm F.  
**Solution:** Peer review, individual contribution tracking.

---

### 7.4. Dating & Relationships

**Commitment Problem:**
- A muốn commitment, B muốn freedom.
- **Nash Equilibrium:** Breakup hoặc 1 người nhượng bộ.

**Insight:** Phải tìm equilibrium cùng có lợi (win-win).

---

## 8. Resources

### **Books (Dễ đọc → Khó)**

1. **"The Art of Strategy"** - Avinash Dixit & Barry Nalebuff  
   *Game Theory cho mọi người, nhiều ví dụ đời thường.*

2. **"Thinking Strategically"** - Avinash Dixit  
   *Classic, dễ hiểu.*

3. **"Game Theory: An Introduction"** - Steven Tadelis  
   *Textbook chuẩn cho học sinh.*

4. **"A Beautiful Mind"** - Sylvia Nasar  
   *Tiểu sử John Nash (Nobel Prize winner).*

---

### **Online Courses**

- **Coursera:** *Game Theory* (Stanford - Matthew Jackson, Yoav Shoham).
- **Khan Academy:** Game Theory basics (Free).
- **Yale Open Course:** *Game Theory* (Ben Polak).

---

### **Videos**

- **Primer (YouTube):** Animated explanations (Prisoner's Dilemma, Evolution).
- **Veritasium:** Game Theory in real life.
- **3Blue1Brown:** Mathematical intuition.

---

### **Games to Play**

- **The Evolution of Trust** (ncase.me/trust) - Interactive Prisoner's Dilemma.
- **Diplomacy** - Board game về negotiation.

---

## 🎯 Kết luận

**Game Theory không phải về "thắng":**
- Mà về **hiểu** tương tác chiến lược.
- Dự đoán hành vi của người khác.
- Thiết kế incentive để đạt outcome mong muốn.

**Key Takeaways:**
1. **Rational ≠ Optimal:** Individual rationality → Collective suboptimal (Prisoner's Dilemma).
2. **Equilibrium ≠ Best:** Nash Equilibrium không phải luôn là kết quả tốt nhất.
3. **Context Matters:** Repeated games cho phép cooperation (Tit-for-tat strategy).
4. **Humans ≠ Robots:** Behavioral economics (fairness, emotions) ảnh hưởng quyết định.

**Áp dụng:**
- **Business:** Pricing, Auctions, Negotiations.
- **Life:** Relationships, Career decisions.
- **Tech:** Blockchain, AI alignment, Mechanism design.

**"In the game of life, understanding the rules is the first step to winning."** 🎲
