# Quiz13_202404002 강지수
# 삼성주가 투자 리스크 분석

# 학번/이름 출력문
print("*****************")
print("202404002/강지수")
print("*****************")

import numpy as np

# 종단가
stock = np.array([68000, 68500, 69000, 70000, 69500, 69000, 68000, 67500, 67000, 66000, 66500, 67000, 68000, 68500, 69000])
# 누적최대값
cumMax= np.array([68000, 68500, 69000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000, 70000])

# 낙폭률 계산
decline_rate = (stock - cumMax) / cumMax

# 최대 낙폭 일
max_decline_day = np.argmin(decline_rate) + 1
# 최대 낙폭 률
max_decline_rate = np.min(decline_rate)

if max_decline_rate <= -0.2:
    risk_level = "위험" # 최대 낙폭이 20% 이상인 경우
elif -0.2 < max_decline_rate <= -0.1:
    risk_level = "주의" # 최대 낙폭이 10% 이상 20% 미만인 경우
else:
    risk_level = "안전" # 최대 낙폭이 10% 미만인 경우

# 투자 리스크 출력
print("<삼성 주가>")
print(stock)
print("<누적최대값>")
print(cumMax)
print("<낙폭률>")
print(decline_rate)

print(f"\n최대낙폭 일={max_decline_day}일")
print(f"\n최대낙폭 률={max_decline_rate:.2f}({risk_level})")
