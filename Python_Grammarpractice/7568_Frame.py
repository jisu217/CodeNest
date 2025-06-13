N = int(input()) # 전체 사람의 수
people = [] # 각 사람의 정보를 저장할 리스트

for i in range(N) :
    # x: 사람의 몸무게, y: 사람의 키
    x, y = map(int, input().split())
    people.append((x, y))

for i in range(N) :
    rank = 1 # 등수_규칙(k+1)

    for j in range(N) :
        if people[j][0] > people[i][0] and people[j][1] > people[i][1] :
           rank += 1

    print(rank, end=' ')

# N = int(input()) # 전체 사람의 수
#
# for i in range(N) :
#
#     # x: 사람의 몸무게, y: 사람의 키
#     x, y = list(int, input().split())
#     if x >  :
#        x = \
#        print()