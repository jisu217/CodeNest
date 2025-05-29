number = int(input()) # 1 <= number <= 4000 (자연수)

# 윤년일 경우 1, 윤년이 아닐 경우 0
if number % 400 == 0 :
   print(1)
elif number % 4 == 0 and number % 100 != 0 :
   print(1)
else :
   print(0)

# %= 대신 %을 사용하는 이유: 확인만 하면 되니까, 변수 값 바꿀 필요 x
