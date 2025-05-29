# 주사위 게임

N = int(input()) # 참여하는 사람 수

result = 0
max_result = 0
D = 0

for i in range(N) :
    A, B, C = map(int, input().split())

    if A == B == C :
       result = 10000 + A * 1000

    elif A == B or A == C or B == C :
         if A == B or A == C :
            result = 1000 + A * 100
         else :
              result = 1000 + B * 100

    else :
         result = max(A, B, C) * 100

    max_result = max(max_result, result)

print(max_result)

