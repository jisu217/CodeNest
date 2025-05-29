# 주사위 세계

# 1부터 6까지의 눈을 가진 3개의 주사위를 입력 받음
A, B, C = map(int, input().split())

result = 0
numbers = 0

if A == B == C : # 세 주사위가 모두 같은 경우
   result = 10000 + A * 1000

elif A == B or B == C or A == C : # 두 주사위만 같은 경우
     if A == B or A == C :
        numbers = A
     else :
         numbers = B
     result = 1000 + numbers * 100

else : # 모두 다른 경우
     result = max(A, B, C) * 100

print(f"{result}")

