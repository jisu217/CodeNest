N = int(input())
list_N = []

for i in range(1, N + 1):
    numbers = int(input())
    if numbers % 2 == 1:
       list_N.append(numbers)
 
print(len(list_N))
