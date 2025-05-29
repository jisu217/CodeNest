# HW1_2_202404002 강지수
# 영화관 예약 시스템

# 학번/이름 출력문
print("*****************")
print("202404002/강지수")
print("*****************")

# 예약 상태를 나타내는 변수
available = "O" # 예약 가능
reserved = "X" # 예약 불가능

# 좌석은 행(A~E), 열(1~5)로 이루어져 있으며 예약 가능 여부를 딕셔너리로 관리
seat = {
    "A1": reserved, "A2": available, "A3": available, "A4": available, "A5": available,
    "B1": available, "B2": reserved, "B3": available, "B4": available, "B5": available,
    "C1": available, "C2": available, "C3": reserved, "C4": available, "C5": available,
    "D1": available, "D2": available, "D3": available, "D4": reserved, "D5": available,
    "E1": available, "E2": available, "E3": available, "E4": available, "E5": reserved
}

# 좌석 현황 출력
print("\t1\t2\t3\t4\t5")
print(f"A\t¦{seat['A1']}¦\t¦{seat['A2']}¦\t¦{seat['A3']}¦\t¦{seat['A4']}¦\t¦{seat['A5']}¦")
print(f"B\t¦{seat['B1']}¦\t¦{seat['B2']}¦\t¦{seat['B3']}¦\t¦{seat['B4']}¦\t¦{seat['B5']}¦")
print(f"C\t¦{seat['C1']}¦\t¦{seat['C2']}¦\t¦{seat['C3']}¦\t¦{seat['C4']}¦\t¦{seat['C5']}¦")
print(f"D\t¦{seat['D1']}¦\t¦{seat['D2']}¦\t¦{seat['D3']}¦\t¦{seat['D4']}¦\t¦{seat['D5']}¦")
print(f"E\t¦{seat['E1']}¦\t¦{seat['E2']}¦\t¦{seat['E3']}¦\t¦{seat['E4']}¦\t¦{seat['E5']}¦")

# 사용자로부터 좌석을 입력받는 코드
seat_choice = input("예약할 좌석: ").upper() # 사용자는 행 번호를 소문자로 입력하더라도 대문자로 변환하여 검사

# 예약 가능한 좌석인지 확인하는 코드
if seat_choice in seat:
    if seat[seat_choice] == available :
        seat[seat_choice] = reserved
        print(f"{seat_choice} 예약 가능")
    else :
        print(f"{seat_choice} 예약 불가능")
else : # 행과 열 범위 밖일 경우
    print(f"{seat_choice} 좌석을 잘못입력했습니다.")

# 홈워크 풀면서 공부한 내용
# seat_choice = input("예약할 좌석: ").upper() 입력받는 즉시 대문자로 변환
# if seat_choice == "O" :
#     seat[seat_choice] = "X"  # 예약 완료
#     print(f"{seat_choice} 예약 가능")
# elif seat_choice == "X" :
#     print(f"{seat_choice} 예약 불가능")
# else : # 행과 열범위 밖일 경우
#     print(f"{seat_choice} 좌석을 잘못입력했습니다.")
# -> 사용자가 예약하고자 하는 좌석의 코드("A1", "B2" 등) 반면 "O" 또는 "X"는 좌석의 예약 상태를 나타내는 값