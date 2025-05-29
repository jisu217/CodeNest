K, N, M = map(int, input().split())

A = K * N
if A > M :
   result = A - M
   print(f"{result}")
elif A <= M :
     print("0")