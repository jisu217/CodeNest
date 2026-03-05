count = 0
numbers = {}
result = []

def solution():
    progresses = list(map(int, input().split()) # 배포 순서를 담는 배열
    speeds = list(map(int, input().split()) # 작업의 개발 속도를 담는 배열

    # 각 작업이 며칠째에 끝나는지 계산하는 코드
    for i in range(len(progresses)):
        i += speeds[i]
        if i < 100:
            count +
        else:
             numbers["i"] = "count"

        if numbers.values(i) == user.values(i+1):
           result[]

           return print(result)

def solution(progresses, speeds):
    answer = []
    time = 0   # 경과된 '일수' (시간)
    count = 0  # 한 번에 배포될 기능의 개수

    # 배포해야 할 작업이 남아있는 동안 계속 반복
    while len(progresses) > 0:
        # [핵심] (현재 진도 + 경과시간 * 작업속도)가 100%를 넘었는지 확인
        if (progresses[0] + time * speeds[0]) >= 100:
            # 100%를 넘었다면 리스트의 맨 앞(0번 인덱스)에서 제거
            progresses.pop(0)
            speeds.pop(0)
            # 오늘 같이 배포할 기능 개수 +1
            count += 1
        else:
            # 아직 100%가 안 됐는데, 이전에 완료된 기능(count > 0)이 있다면?
            if count > 0:
                # 지금까지 쌓인 count를 결과 리스트에 담기 (배포 발생!)
                answer.append(count)
                # 배포를 했으니 count는 다시 0으로 초기화
                count = 0

            # 아직 맨 앞 작업이 안 끝났으므로 하루를 더 보냅니다 (시간 증가)
            time += 1

    # 반복문이 끝나고 마지막으로 쌓여있던 count까지 추가해주면 끝
    answer.append(count)
    return answer