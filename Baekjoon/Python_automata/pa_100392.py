total_score = 0

# 학생 점수 5번 입력
for i in range(5):
    score = int(input())  # 점수 입력
    if score < 40:        # 40점 미만이면
        score = 40       # 40점으로 바꿈
    total_score += score  # 점수 더하기

# 평균 계산
average_score = total_score // 5

# 평균 출력
print(average_score)


