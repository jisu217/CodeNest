while True:
    A, B, C = map(int, input().split())

    if A == 0 and B == 0 and C == 0:
        break  # 종료 조건

    if A + B <= C or A + C <= B or B + C <= A :
       print("Invalid")  # 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우
    elif A == B == C :
         print("Equilateral") # Equilateral :  세 변의 길이가 모두 같은 경우
    elif A == B or B == C or A == C :
         print("Isosceles") # Isosceles : 두 변의 길이만 같은 경우
    else :
         print("Scalene") # Scalene : 세 변의 길이가 모두 다른 경우