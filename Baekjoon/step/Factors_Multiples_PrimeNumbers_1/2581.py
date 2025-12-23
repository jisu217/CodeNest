M = int(input())
N = int(input())
list = []
sum = 0

for i in range(M, N+1):
    if i % 2 == 0:
       list.append(i)
       sum += i

print(sum)
print(list)