# 성적 분석
import numpy as np

# 파일 읽기
scores = np.loadtxt(',//res//scores.csv', delimiter=',')
# 데이터를 구분하는 **구분자(Separator)**,
# 데이터를 다룰 때, 텍스트 파일에서 값들이 어떻게 구분되는지 지정해주는 역할
scores = np.array(scores, int)

# 과목
Subject = "수학", "국어", "영어"

print("[전체 데이터")
print(scores)

print("\n[학년별 평균")
print(scores.mean(1))

# mean(): 배열의 평균값을 계산
# axis=0: 열 방향_과목별 평균
# axis=1: 행 방향_학년별 평균
# mean(1) = axis=1

print("\n[과목별 통계")
for i in range(3) :
    print(Subject[i], end ='')

# scores.mean(axis=0)[i] = 과목별 평균을 계산한 결과 중에서 i번째 값을 가져옴

    avg = scores.mean(axis=0)[i]
    print(f"\t평균:{avg:.2f}", end= '')

    std = scores.std(axis=0)[i]
    print(f"\t표준편차:{std:.2f}", end= '')

    data = scores[:, i] # 과목 전체 행
    maxIDX = np.argmax(data)
    minIDX = np.argmin(data)

    print(f"\t최고점수:{data[maxIDX]}", end= '')
    print(f"\t최저점수:{data[minIDX]}")
