# 스타벅스 월별 통계

import matplotlib.pyplot as plt

# 월 데이터 (1월부터 11월까지)
months = range(1, 12)
# 스타벅스 데이터
revenue = [150, 160, 155, 165, 170, 180, 175, 185, 190, 200, 210] # 월별 매출 (단위: 억 원)
beverages_sold = [120, 130, 125, 135, 140, 145, 150, 155, 160, 165, 170] # 월별 음료 판매량 (단위: 만 잔)
new_customers = [5000, 5200, 5100, 5300, 5500, 5600, 5700, 5900, 6000, 6200, 6500] # 월별 신규 고객 수

fig, axs = plt.subplots(1, 3) # 1 x 3 subplot 생성
fig.set_size_inches(15, 5) # 그래프 크기 설정 (가로 15, 세로 5)

# 첫 번쨰 그래프: 월별 매출
axs[0].plot(months, revenue, morker = 'D', color = '#aed953') # 'D' 마커 사용, 연한 초록색
axs[0].set_title('Monthly Revenue (Billion KRW)') # 그래프 제목 설정
axs[0].set_xlabel('Months') # x축 라벨 설정
axs[0].set_ylabel('Revenue (B KRW)') # y축 라벨 설정
axs[0].grid(True) # 격자선 표시

# 두 번쨔 그래프: 월별 음료 판매량
axs[1].plot(months, beverages_sold, morker = '+', color = 'b') # '+' 마커 사용, 파란색
axs[1].set_title('Monthly Revenue Sold (10k cups)') # 그래프 제목 설정
axs[1].set_xlabel('Months', fontsize = 12) # x축 라벨 설정
axs[1].set_ylabel('Beverages Sold (10k)') # y축 라벨 설정
axs[1].grid(True) # 격자선 표시

# 세 번째 그래프: 월별 신규 고객 수
axs[2].plot(months, new_customers, morker = '1', color = '#d95753') # '1' 마커 사용, 빨간색
axs[2].set_title('Monthly New Customers') # 그래프 제목 설정
axs[2].set_xlabel('Months') # x축 라벨 설정
axs[2].set_ylabel('New Customers') # y축 라벨 설정

# 그래프 출력
plt.show()





