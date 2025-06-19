T = int(input()) # 테스트 케이스의 수

for i in range(T) :
    Korea = 0
    Yonsei = 0

    for i in range(9) :
        K, Y = map(int, input().split())
        Korea += K
        Yonsei += Y

    if Korea > Yonsei :
        print("Korea")
    elif Korea < Yonsei :
        print("Yonsei")
    else :
        print("Draw")

