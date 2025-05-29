T = int(input()) # 테스트 케이스의 개수

for i in range(T) :
    numbers = input().split()
    result = float(numbers[0])

    for l in numbers[1:] :
        if l == '@' :
           result *= 3
        if l == '%' :
           result += 5
        if l == '#' :
           result -= 7

    print(f"{result:.2f}")


