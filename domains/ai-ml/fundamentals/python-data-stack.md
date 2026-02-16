# 🐍 Python Data Stack: Ngôn ngữ của Khoa học Dữ liệu

> [← Back to AI/ML Roadmap](../README.md)

Làm AI mà không biết Python thì giống như làm thợ mộc mà không có búa.
Đây là bộ 3 thư viện quyền lực nhất: **NumPy, Pandas, Matplotlib**.

---

## 1. NumPy (Numerical Python)

Python thuần rất chậm khi xử lý số lượng lớn (Vòng lặp `for` siêu rùa).
NumPy được viết bằng C, chạy nhanh hơn Python gấp 100 lần nhờ **Vectorization** (Tính toán song song).

```python
import numpy as np

# Tạo vector
a = np.array([1, 2, 3])

# Phép tính trên toàn bộ mảng (không cần vòng lặp)
b = a * 2 
# Output: [2, 4, 6] -> Nhanh khủng khiếp!
```

*   **NDArray:** Mảng đa chiều hiệu quả bộ nhớ.
*   **Broadcasting:** Tự động mở rộng kích thước mảng nhỏ để tính toán với mảng lớn.

---

## 2. Pandas (Python Data Analysis)

Excel phiên bản Python. Xử lý dữ liệu dạng bảng (Tabular Data).

```python
import pandas as pd

# Đọc file CSV (hàng triệu dòng trong tích tắc)
df = pd.read_csv('data.csv')

# Xem 5 dòng đầu
print(df.head())

# Lọc dữ liệu: Lấy tất cả người > 20 tuổi
adults = df[df['age'] > 20]

# Thống kê mô tả
print(df.describe()) # Mean, Std, Min, Max...
```

*   **DataFrame:** Cấu trúc bảng 2 chiều (Dòng & Cột).
*   **Missing Data:** Xử lý dữ liệu bị thiếu (`NaN`) bằng `fillna()` hoặc `dropna()`.

---

## 3. Matplotlib & Seaborn (Visualization)

Một bức ảnh hơn ngàn lời nói. Vẽ biểu đồ để hiểu dữ liệu.

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Vẽ biểu đồ đường (Line Chart) - Xu hướng
plt.plot(x, y)

# Vẽ biểu đồ cột (Bar Chart) - So sánh
plt.bar(categories, values)

# Vẽ biểu đồ phân tán (Scatter Plot) - Tương quan
plt.scatter(height, weight)

# Seaborn: Đẹp hơn, dễ dùng hơn Matplotlib
sns.heatmap(correlation_matrix) # Bản đồ nhiệt
plt.show()
```

---

## 4. Scikit-learn (Machine Learning Library)

Thư viện chuẩn mực cho Classic ML.
Cung cấp sẵn tất cả thuật toán (Linear Regression, SVM, Random Forest) chỉ với vài dòng code.

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train) # Huấn luyện
predictions = model.predict(X_test) # Dự đoán
```
