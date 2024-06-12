from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 데이터셋 로드
diabetes = load_diabetes()

# BMI와 혈당 데이터 추출
X = diabetes.data[:, 2].reshape(-1, 1)
y = diabetes.target.reshape(-1, 1)

# 선형회귀 모델 학습
model = LinearRegression()
model.fit(X, y)

# 회귀선 그리기
y_pred = model.predict(X)
plt.scatter(X, y, alpha=0.5)
plt.plot(X, y_pred, color='red')
plt.title('BMI vs. Sugar')
plt.xlabel('BMI')
plt.ylabel('Sugar')
plt.show()
