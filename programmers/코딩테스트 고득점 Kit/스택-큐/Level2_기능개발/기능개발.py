def solution(progresses, speeds)
    answer = []
    time = 0 # 현재 흐른 시간 (일수)
    count = 0 # 오늘 한꺼번에 배포될 기능의 개수

    while len(progresses) > 0:
        # (현재 진도 + 흐른 시간 * 작업 속도)가 100 이상인지 확인
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0

            time += 1

    answer.append(count)
    return answer