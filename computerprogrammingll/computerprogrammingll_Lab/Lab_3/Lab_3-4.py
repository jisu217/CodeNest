# 좌석 및 인원 수를 입력 받아 티켓 계산하는 프로그램

# 좌석 타입 입력
seatType = input("좌석 클래스(VIP, R, S, A, B):")
# price = 0: # 여기에 선언안해도됨: 입력된 좌석 클래스가 올바를 경우, if-elif 조건문 안에서 정확한 가격으로 price가 설정
#                              좌석 클래스가 잘못 입력된 경우에는 그 부분에 대한 처리가 이미 else에서 이루어져, 잘못된 입력에 대한 오류 메시지를 출력하고 프로그램이 종료
#                              미리 price를 0으로 선언할 필요 없이, 좌석 타입에 따라 올바르게 값을 할당하는 것이 보장되므로 그 부분은 생략해도 문제가 없음

# 좌석 값 검사
if seatType == "VIP" or seatType == "R" or seatType == "S" or seatType == "A" or seatType == "B":

    # 수량 입력
    count = int(input("수량:"))

    # 좌석에 따른 표 가격
    if seatType == "VIP" :
        price = 160000
    elif seatType == "R" :
        price = 140000
    elif seatType == "S" :
        price = 100000
    elif seatType == "A":
        price = 80000
    elif seatType == "B": # "B" 좌석도 하나의 선택지일 뿐_ else는 특정 조건에 해당하지 않을 때 처리할 내용을 지정
        price = 60000

    print(f"{seatType}석 {count}개 ===> 총 {price*count}원")

else:
    print("!!!잘못입력하였습니다!!!")