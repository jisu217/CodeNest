import time

t1 = time.time() # 현재 시간을 실수형으로 가져옴
sum = 0
maxNum = 10000000
for i in range(1, maxNum):
    sum += i
t2 = time.time() # 현재 시간을 실수형으로 가져옴
print(f"1부터 {maxNum} 까지의 합을 구하는데 걸리는 시간: {t2 - t1}초")