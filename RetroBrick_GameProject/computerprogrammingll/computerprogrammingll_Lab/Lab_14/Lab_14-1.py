# 2024년도 월별 PC방 게임 점유율

import matplotlib.pyplot as plt

# Monthly data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']
# Monthly percentage data for each game
lol = [40.46, 41.20, 42.00, 42.50, 43.00, 43.50, 44.00, 44.50, 45.00, 45.50, 46.00]
valorant = [8.03, 8.50, 8.70, 9.00, 9.20, 9.50, 9.70, 10.00, 10.20, 10.50, 10.70]
fifa_online = [10.01, 9.80, 9.60, 9.50, 9.40, 9.30, 9.20, 9.10, 9.00, 8.90, 8.80]

# plot the data
plt.figure(figsize=(10, 6)) # 그래프 10 x 6 인치 크기의 Figure
plt.plot(months, lol, morker = 'o', label = 'League of Legends')
plt.plot(months, valorant, morker = 'o', label = 'Valorant')
plt.plot(months, fifa_online, morker = 'o', label = 'FIFA Online')

# 제목과 축 라벨
plt.title('Monthly PC Bang Game Rankings (Top 3 game, 2024)', fontsize = 14)
plt.xlabel('Months', fontsize = 12)
plt.xlabel('Market Share (%)', fontsize = 12)

# 범례
plt.legend(loc='best') # 데이터를 방해하지 않는 가장 적합한 위치에 범례를 배치하므로 범례를 그래프에 추가할 때 가장 편리한 옵션
plt.grid(True) # 배경에 격자무늬 추가

# Show the plot
plt.show()
