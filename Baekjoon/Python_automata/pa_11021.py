count = int(input())
C = 1

while C <= count :
   A, B = map(int, input().split())
   print(f"Case #{C}: {A+B}")
   C += 1

