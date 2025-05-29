T = int(input()) # 테스트 케이스의 개수

for i in range(T) :
    number = input().split()
    result = float(number[0])

    for l in number[1:] :
        if l == '@' :
           result *= 3
        if l == '%' :
           result += 5
        if l == '#' :
           result -= 7

    print(f"{result:.2f}")

