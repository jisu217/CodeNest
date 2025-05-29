S = int(input())

result = 0
count = 0

for i in range(1, S+1) :
    result += i
    count += 1

    if result > S :
       count -= 1
       break

print(count)