# Quiz06_202404002 강지수
# 도서관 좌석 예약 시스템

# 학번/이름 출력문
print("*****************")
print("202404002/강지수")
print("*****************")

# 좌석번호: 가능 상태("0")인 딕셔너리 생성
# 좌석번호(key)는 "A#" 형태
seats = {f"A{i}": "0" for i in range(4)}

# 좌석의 상태를 "|상태탭" 형태로 출력
# 각 좌석 상태 출력 함수
def print_seat_status():
    print(f"|{seats['A0']}|\t|{seats['A1']}|\t|{seats['A2']}|\t|{seats['A3']}|")

# 초기 좌석 상태 출력
print_seat_status()

print("A0\tA1\tA2\tA3\n")
print("[예약시스템]")

# 사용자로부터 번호만 입력받는 코드
seat_number = int(input("좌석번호 입력: "))

# 사용자로부터 번호만 입력받아 예약 불가능 상태 "X"로 변경
if 0 <= seat_number <= 3:
    # 좌석번호에 해당하는 key의 값을 "X"로
    seats[f"A{seat_number}"] = "X"
else:
    print("잘못된 좌석 번호입니다.")

print("\n[완료]")

# 변경 좌석 상태 출력
print_seat_status()

# 퀴즈 풀면서 공부한 내용
# 딕셔너리 구조: d = { "name" : "홍길동", "age" : 20, "취미" : ["영화 감상", "게임", "독서"] }
# 처음에는 가능 상태("0")로 초기화, 후 변화에 따라 "X"로 변경
# def print_seat_status(): 함수를 이용하여 출력 편의]
# seats[seat_number] = "X"이 아닌 seats[f"A{seat_number}"] = "X"