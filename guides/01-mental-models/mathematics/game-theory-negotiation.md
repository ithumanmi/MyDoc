# ♟️ Game Theory (Lý thuyết Trò chơi)

## 1. Cân bằng Nash (Nash Equilibrium) - Định nghĩa hình thức
Trong một trò chơi với $n$ người chơi, một bộ chiến lược $(s_1^*, s_2^*, ..., s_n^*)$ được gọi là Cân bằng Nash nếu không người chơi nào có thể đạt được kết quả tốt hơn bằng cách đơn phương thay đổi chiến lược của mình, trong khi các người chơi khác giữ nguyên chiến lược.

### Công thức:
$$U_i(s_i^*, s_{-i}^*) \geq U_i(s_i, s_{-i}^*)$$
Với mọi $s_i \in S_i$ (tập chiến lược của người chơi $i$).
*   $U_i$: Hàm lợi ích (Utility function) của người chơi $i$.
*   $s_i^*$: Chiến lược tối ưu của người chơi $i$.
*   $s_{-i}^*$: Chiến lược tối ưu của tất cả những người chơi còn lại.

**Ý nghĩa:** Trạng thái "ổn định" của hệ thống. Không ai hối tiếc về quyết định của mình khi biết quyết định của người khác. Một trò chơi có thể có một, nhiều, hoặc không có Cân bằng Nash (chiến lược thuần túy).

## 2. Thế tiến thoái lưỡng nan của tù nhân (Prisoner's Dilemma)
Ví dụ kinh điển về việc lợi ích cá nhân mâu thuẫn với lợi ích tập thể.

### Ma trận lợi ích (Payoff Matrix):
Giả sử A và B bị bắt.
*   **Hợp tác (Im lặng):** Mỗi người tù 1 năm.
*   **Phản bội (Khai):** Kẻ khai được thả (0 năm), kẻ im lặng tù 10 năm.
*   **Cả hai Phản bội:** Mỗi người tù 5 năm.

| | B Hợp tác (Im lặng) | B Phản bội (Khai) |
| :--- | :--- | :--- |
| **A Hợp tác** | A: -1, B: -1 (Tốt nhất cho cả hai) | A: -10, B: 0 |
| **A Phản bội** | A: 0, B: -10 | **A: -5, B: -5** (Cân bằng Nash) |

### Phân tích:
*   Nếu B im lặng -> A nên Khai (0 > -1).
*   Nếu B khai -> A nên Khai (-5 > -10).
*   **Chiến lược áp đảo (Dominant Strategy):** Dù B làm gì, A luôn có lợi hơn khi Khai. Tương tự với B.
*   **Kết quả:** Cả hai cùng Khai (-5, -5), dù lựa chọn Im lặng (-1, -1) tốt hơn cho cả hai (Pareto Optimal).
*   **Bài học:** Sự hợp lý của cá nhân dẫn đến sự phi lý của tập thể. Cần luật chơi/hợp đồng để ép buộc hợp tác.

## 3. Trò chơi Tổng bằng không (Zero-sum)
Lợi ích của người này là mất mát của người kia.
$$\sum_{i=1}^{n} U_i(s) = 0$$
*   **Ví dụ:** Cờ vua, Poker, Tranh giành thị phần trong thị trường bão hòa.
*   **Minimax Theorem:** Trong zero-sum game, chiến lược tối ưu là tối thiểu hóa khả năng thắng tối đa của đối thủ (Minimize the Maximum loss).

## 4. Trò chơi lặp lại (Iterated Games) & Sự tiến hóa của hợp tác
Trong trò chơi Prisoner's Dilemma chơi 1 lần, phản bội là tối ưu. Nhưng nếu chơi vô hạn lần, **Hợp tác** có thể xuất hiện.

### Chiến lược Tit-for-Tat (Ăn miếng trả miếng):
1.  Ván 1: Hợp tác.
2.  Ván n: Làm y hệt những gì đối thủ làm ở ván n-1.
*   **Tính chất toán học:**
    *   **Nice:** Không bao giờ phản bội trước.
    *   **Retaliatory:** Phản đòn ngay lập tức.
    *   **Forgiving:** Sẵn sàng quay lại hợp tác.
*   **Kết quả:** Trong mô phỏng máy tính của Robert Axelrod, Tit-for-Tat đánh bại các chiến lược phức tạp khác.

## 5. Chiến lược Hỗn hợp (Mixed Strategy)
Đôi khi chiến lược tốt nhất là... ngẫu nhiên.
Trong trò Oẳn tù tì (Rock-Paper-Scissors), nếu bạn ra Búa 100%, bạn thua.
Cân bằng Nash là chọn mỗi phương án với xác suất $P = 1/3$.
*   **Ứng dụng:** Trong cạnh tranh/thể thao, phải làm mình trở nên khó đoán (Unpredictable) để đối thủ không bắt bài.

## 6. Điểm Schelling (Focal Point)
Trong các trò chơi phối hợp (Coordination Game) mà không được giao tiếp, người chơi thường chọn giải pháp "nổi bật" nhất.
*   **Bài toán:** Hai người hẹn gặp ở New York nhưng quên chốt địa điểm/thời gian.
*   **Giải pháp:** Đa số chọn "Quảng trường Thời đại" vào lúc "12 giờ trưa".
*   **Marketing:** Thương hiệu là một điểm Schelling. Khi không biết chọn gì, khách hàng chọn cái nổi bật nhất.

---

## 🛠️ Ứng dụng Thực chiến (Life Applications)

### 1. Trò chơi "Gà đế" (Game of Chicken) & Đàm phán
Hai xe lao vào nhau. Ai bẻ lái trước là "Gà" (hèn). Nếu không ai bẻ lái, cả hai cùng chết.
*   **Chiến lược thắng:** Làm cho đối thủ tin rằng mình **mất khả năng kiểm soát** hoặc **hoàn toàn điên rồ**.
*   **Đàm phán:** "Đây là giá cuối cùng, sếp tôi không cho phép giảm nữa" (Tự trói tay mình - Binding commitment). Khi bạn không còn quyền lựa chọn, đối thủ buộc phải nhượng bộ nếu không muốn đàm phán đổ vỡ.

### 2. Bi kịch của cái chung (Tragedy of the Commons)
Tài nguyên chung (bếp văn phòng, công viên, môi trường) luôn bị khai thác quá mức vì lợi ích cá nhân mâu thuẫn với lợi ích tập thể.
*   **Ví dụ:** Bếp văn phòng bẩn thỉu vì ai cũng nghĩ "mình chỉ để một cái ly bẩn thôi mà".
*   **Giải pháp Game Theory:** Tư hữu hóa (Privatization) hoặc áp đặt quy định thưởng phạt nghiêm khắc (Regulation) để thay đổi Payoff Matrix (làm cho việc xả rác có "giá" đắt hơn).

### 3. Burn the Boats (Đốt thuyền)
Tướng quân Cortez khi đến vùng đất mới đã đốt hết thuyền để binh sĩ chỉ còn 1 đường sống: Chiến thắng hoặc Chết.
*   **Cơ chế:** Loại bỏ lựa chọn rút lui (Retreat option) để thay đổi tâm lý và cam kết của bản thân (và quân lính).
*   **Đời sống:** Nộp đơn nghỉ việc trước khi tìm được việc mới (rủi ro cao) đôi khi là động lực duy nhất để bạn khởi nghiệp thành công.
