T = int(input()) # 테스트의 개수

for i in range(T) :
    R, S = input().split()
    R = int(R)

    result = ""
    for l in S :
        result += l*R
    print(f"{result}")

