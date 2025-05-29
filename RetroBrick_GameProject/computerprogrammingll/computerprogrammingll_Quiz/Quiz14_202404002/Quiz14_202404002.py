# Quiz14_202404002 강지수
# 음악 주파수와 공부의 관계 그래프

# 학번/이름 출력문
print("*****************")
print("202404002/강지수")
print("*****************")

import numpy as np
import matplotlib.pyplot as plt

# 파일 읽기
scores = np.loadtxt('/res/data.csv', delimiter=",")
# 음악 주파수 데이터
# Music_Frequency = range(250, 2000)
Music_Frequency = np.linspace(250, 2000, num=100)

fig, axs = plt.subplots(1, 2) # 1 x 2 subplot 생성
fig.set_size_inches(20, 10) # 그래프 크기 설정 (가로 15, 세로 5)

# 첫 번째 그래프
axs[0].plot(Music_Frequency, scores[:, 0], marker='o', color = '#CC33FF')
axs[0].plot(Music_Frequency, scores[:, 1], color = 'blue', linestyle="--")
axs[0].set_title('Study Focus(%) vs Heart Rate(BPM) by Music Frequency(Hz)')
axs[0].set_xlabel('Music Frequency(Hz)')
axs[0].set_ylabel('Value')
axs[0].grid(True) # 격자선 표시

# 두 번쨰 그래프
axs[1].plot(Music_Frequency, scores[:, 2], color = 'green', linestyle="-.")
axs[1].plot(Music_Frequency, scores[:, 0], marker='o', color = '#CC33FF')
axs[1].set_title('Study Focus Level(%) vs Memory Test Score by Music Frequency(Hz)')
axs[1].set_xlabel('Music Frequency(Hz)')

plt.show()