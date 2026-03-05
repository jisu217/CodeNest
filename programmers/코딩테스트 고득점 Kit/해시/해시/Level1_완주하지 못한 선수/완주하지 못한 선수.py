def solution(participant, completion):
    participant.sort() # 마라톤에 참여한 선수들
    completion.sort()  # 완주한 선수들

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]