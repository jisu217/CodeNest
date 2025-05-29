C = int(input())
D = 1

while D <= C :
  A, B = map(int, input().split())
  print(f"Case #{D}: {A} + {B} = {A+B}")
  D += 1

