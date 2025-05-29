import math

T = int(input())

for i in range(T) :
    A, B = map(int, input().split())

    # 최소 공배수 = 두 수의 곱 / 최대 공약수
    result = (A*B) // math.gcd(A, B)
    print(result)

#     for l in range(1, 45000) :
#         if (A * l) % B == 0 :
#             print(A * l)
#             break