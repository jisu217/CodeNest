while True:
    number1, number2 = map(int, input().split())
    
    # 종료 조건
    if number1 == 0 and number2 == 0:
        break

    # 첫 번째 숫자가 두 번째 숫자의 약수
    if number2 % number1 == 0:
       print("factor")
    # 첫 번째 숫자가 두 번째 숫자의 배수
    elif number1 % number2 == 0:
         print("multiple")
    # 둘 다 아님
    else:
        print("neither")
