# Quiz04_202404002 강지수
# 점수 계산

# 학번/이름 출력문
print("*****************")
print("202404002/강지수")
print("*****************")

# 사용자로부터 과목 개수를 입력 받는 코드
subject_count = int(input("과목 수 입력:"))

if subject_count > 0 :
   total_score = 0 # 총 점수를 저장할 변수
   average = 0 # 평균 점수를 저장할 변수

   # 과목 개수 만큼 점수를 입력받는 코드
   for n in range(subject_count):
       while True:
             score = int(input("점수 입력:"))

             # 0~100 이외의 값 입력받을 시 "!!!잘못입력!!!" 출력 후 재입력
             if 0 <= score <= 100 :
                total_score += score
                break
             else :
                  print("!!!잘못입력!!!")
# 평균 = 총점수/개수
average = total_score / subject_count
print(f"{subject_count}개 과목의 평균={average:.2f}")

# 퀴즈 풀면서 공부한 내용
# subject != 0 : 아닌 subject > 0 :
# score = 0: 사용자 입력 시 바로 덮어씌워지므로 초기화 X
# total_score = 0, average = 0: 점수의 합계를 저장하고 반복문이 끝난 후에도 값을 유지해 평균을 계산하는 데 사용되므로 초기화 O
# while True: 점수를 잘못 입력받으면 재 입력받아야 하므로
# :.2f



