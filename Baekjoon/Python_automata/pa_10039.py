A = int(input()) # 원섭이의 점수
B = int(input()) # 세희의 점수
C = int(input()) # 상근이의 점수
D = int(input()) # 숭이의 점수
E = int(input()) # 강수의 점수

if A < 40 :
   A = 40
if B < 40 :
   B = 40
if C < 40 :
   C = 40
if D < 40 :
   D = 40
if E < 40 :
   E = 40

result = (A + B + C + D + E) // 5
print(result)

