A, B = map(int, input().split())
C, D = map(int, input().split())
E, F = map(int, input().split())

if A == C and C != E :
   result1 = E
elif A == E and C != E :
     result1 = C
elif A != E and C == E :
     result1 = A

if B == D and D != F :
   result2 = F
elif B == F and D != F :
     result2 = D
elif B != F and D == F :
     result2 = B


print(f"{result1} {result2}")