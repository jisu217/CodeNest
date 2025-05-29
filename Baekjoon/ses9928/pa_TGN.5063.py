N = int(input()) # 테스트의 개수

for i in range(N) :
    r, e, c = map(int, input().split())

    if r < e - c :
       print('advertise')
    elif r == e - c :
         print('does not matter')
    else :
        print('do not advertise')
