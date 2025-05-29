# Quiz05_202404002 강지수
# 출석 점수 계산

# 학번/이름 출력문
print("*****************")
print("202404002/강지수")
print("*****************")
print("[[출석 계산]]")
print("(1:출석/2:지각/3:결석)")

# 출석 정보를 저장할 리스트
attendance = []

for week in range(1, 16):
    # 사용자로부터 15주차까지의 출석 정보를 입력받는 코드
    check = int(input(f"{week:02}주차 출석:")) # 사용자는 1~3까지만 입력
    attendance.append(check)  # 리스트에 출석 정보 저장

# 출석 정보를 기반으로 각 일수와 전체 퍼센트(%), 점수를 출력하는 함수
def calculate_attendance(attendance):
    total_score = 10  # 초기 점수 (총 10점)

    attend_count = attendance.count(1)  # 출석 일수
    late_count = attendance.count(2)  # 지각 일수 (3번당 -1점)
    absent_count = attendance.count(3)  # 결석 일수 (-1점)

    # 총 출석 점수 (10 - (결석 + 지각/3))
    total_score -= (absent_count + late_count // 3)

    # 퍼센트 계산
    attend_percentage = (attend_count / 15) * 100 # 출석 일수 퍼센트
    late_percentage = (late_count / 15) * 100 # 지각 일수 퍼센트
    absent_percentage = (absent_count / 15) * 100 # 결석 일수 퍼센트

    # 결과 출력
    print("\n****************************")
    print(f"출석 \t{attend_count}일({attend_percentage:.2f}%)") # 출석 일수 결과
    print(f"지각 \t{late_count}일({late_percentage:.2f}%)") # 지각 일수 결과
    print(f"결석 \t{absent_count}일({absent_percentage:.2f}%)") # 결석 일수 결과
    print("****************************")
    print(f"출석점수 \t\t{total_score}점") # 계산된 총 출석 점수 결과

# 함수 호출
calculate_attendance(attendance)

# 퀴즈 풀면서 공부한 내용
# list.count(value) 해당 리스트에서 특정 값이을 세어주는 기능
# 02는 숫자 출력 시 최소 두 자리로 표시