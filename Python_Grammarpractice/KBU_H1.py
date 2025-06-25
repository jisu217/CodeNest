# 초급: 비밀번호 탐정
# 사용자로부터 암호를 입력받아 사용자가 입력한 비밀번호가 다음 조건을 모두 만족하는지 검사하는 프로그램

password = input("비밀번호를 입력하세요: ") # 사용자로부터 비밀번호 입력받기

# 각 조건을 확인할 변수 초기화
has_length = False  # 1) 길이가 8자 이상인가?
has_upper = False   # 2) 영어 대문자가 있는가?
has_lower = False   # 3) 영어 소문자가 있는가?
has_digit = False   # 4) 숫자가 있는가?

# 1) 길이 조건 검사
if len(password) >= 8:
    has_length = True

# 2, 3, 4) 문자 종류 검사
for char in password:
    if char.isupper():  # 문자가 대문자이면
        has_upper = True
    elif char.islower(): # 문자가 소문자이면
        has_lower = True
    elif char.isdigit(): # 문자가 숫자이면
        has_digit = True

# 네 가지 조건을 모두 만족하는지 확인
if has_length and has_upper and has_lower and has_digit:
    print("비밀번호가 안전합니다.")
else: # 하나라도 만족하지 않으면
    print("비밀번호가 불안합니다.")