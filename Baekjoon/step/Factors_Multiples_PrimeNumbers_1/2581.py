M = int(input())
N = int(input())
list = []

for i in range(M, N+1):
    if i % 2 == 0:
       list.append(i)

if len(list) == 0:
   print(-1)
else:
   print(list)
