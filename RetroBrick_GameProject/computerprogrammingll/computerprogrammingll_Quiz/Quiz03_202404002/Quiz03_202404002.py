# Quiz03_202404002 강지수
# 워터 파크 입장권 계산

# 학번/이름 출력문
print("*****************")
print("202404002/강지수")
print("*****************")

# 사용자로부터 생년을 입력 받는 코드
Birthday_year = int(input("생년:"))

# 사용자가 생년을 잘못 입력할 시
if Birthday_year > 2024 :
   print("!!!잘못입력하였습니다!!!")
   exit()

# 사용자의 나이를 계산하는 코드
age = 2024 - Birthday_year

print("1. 종일권")
print("2. 오후권")
# 사용자로부터 종일권 혹은 오후권을 입력 받는 코드
ticket_choice = int(input("번호 입력:"))

# 요금 적용 연령 구분

# 최종 가격을 문자열로 포맷팅하여 사용자에게 출력하기 위해 사용하는 변수
formatted_price = None

# 1. 사용자가 종일권 혹은 오후권을 잘못입력할 시
if ticket_choice != 1 and ticket_choice != 2 :
   print("!!!잘못입력하였습니다!!!")
   exit()

# 2. 입장권이 종일권일 때
if ticket_choice == 1 :
    ticket = "종일권"
    if age >= 13 : # 대인: 만 13세 이상
       age_group = "대인"
       price = 75000
       formatted_price = "{:,}".format(price) # 가격을 천 단위로 쉼표를 추가하여 포맷팅
    elif 3 <= age and age < 13 : # 소인: 36개월 ~ 만 12세
         age_group = "소인"
         price = 61000
         formatted_price = "{:,}".format(price)
    else: # 36개월 미만: 입장 무료(증빙 서류 지참: 의료 보험증 및 주민 등록 등본 등)
         age_group = "36개월 미만"
         price = 0
    print(f"{age_group}-{ticket}===>{formatted_price}원")

# 3. 입장권이 오후권일 때 (14:00~)
if ticket_choice == 2 :
    ticket = "오후권"
    if age >= 13 :
       age_group = "대인"
       price = 68000
       formatted_price = "{:,}".format(price)
    elif 3 <= age and age < 13 :
         age_group = "소인"
         price = 56000
         formatted_price = "{:,}".format(price)
    else:
         age_group = "36개월 미만"
         price = 0
    print(f"{age_group}-{ticket}===>{formatted_price}원")

# 퀴즈 풀면서 공부한 내용
# break는 반복문 내에서만 사용할 수 있는 명령어로 exit() 사용하기
# if ticket != 0 or ticket != 1 : or이 아님 and임 -> 1이 아니고 2도 아닌 경우를 의미를 나타내야 하기 떄문
# ticket == 1 : ticket = "종일권" -> ticket_choice == 1 : ticket = "종일권"
# age > 13 : age = "대인" -> age > 13 : age_group = "대인"
# format() 함수 사용: 가격을 숫자형으로 유지하지 않고 문자열로 포맷팅
  # number = 56000
  # formatted_number = "{:,}".format(number)
  # print(formatted_number) -> 56,000