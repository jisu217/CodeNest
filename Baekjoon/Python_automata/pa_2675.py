T = int(input()) # 테스트의 개수 (1 ≤ T ≤ 1,000)

for i in range(T) :
    R, S = input().split()  # R: 테스트 케이스의 반복 횟수, S: 문자열 입력 받음
    R = int(R)

    result = "" # 결과 문자열 초기화
    for l in S :
        result += R * l

    print(f"{result}")