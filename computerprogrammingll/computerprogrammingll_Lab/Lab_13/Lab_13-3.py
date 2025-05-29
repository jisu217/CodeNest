# 영화 관람자수 예측
import numpy as np

# 데이터: 왓챠 '보고 싶어요' 수(x)와 총 관객 수(y)
x = np.random.uniform(5000, 20000, size=30).astype(int)
# 총 관객 수 (명): watched_counts를 기반으로 normal 분포 추가
y = (x * np.random.uniform(400, 600, size=30) + np.random.normal(0, 500000, size=30)).astype(int)

# 선형 회귀: 기울기(m)와 절편(b) 계산
x_mean = np.mean(x)
y_mean = np.mean(y)

numerator = ((x-x_mean) * (y-y_mean)).sum()
denominator = ((x - x_mean) ** 2).sum()
a = numerator / denominator
b = y_mean - a * x_mean

print(f"기울기 (a): {a:.2f}")
print(f"절편 (b): {b:.2f}")

x = int(input("궁금한 개봉예정 보고싶어요 수:"))
# 예측값 계산
predicted_audience = a * x + b
print(f"예측 관객 수는 {predicted_audience:.2f}명 입니다.")