# Quiz09_202404002 강지수
# SNS 플랫폼별 사용자의 주당 활동 시간

# 학번/이름 출력문
print("*****************")
print("202404002/강지수")
print("*****************")

# SNS 플랫폼별 사용자의 주당 활동 시간 데이터
snsTime = (

"Instagram", 10,

"TikTok", 12,

"Facebook", 8,

"Twitter", 7,

"Snapchat", 9,

"YouTube", 15,

"LinkedIn", 4

)

# 플랫폼과 시간을 리스트로 추출
platform = list(snsTime[0::2])
times = list(snsTime[1::2])

# 최대값 top3를 찾는 함수
def maxSNS(times, platforms):
    top_platforms = []
    top_times = []

    for _ in range(3):
        max_index = 0
        for i in range(1, len(times)):
            if times[i] > times[max_index]:
                max_index = i

        top_platforms.append(platforms[max_index])
        top_times.append(times[max_index])

        # 최대값을 찾은 후 플랫폼과 시간 제거
        times.pop(max_index)
        platforms.pop(max_index)

    return top_platforms, top_times

top_platforms, top_times = maxSNS(times, platform)

print("\n[SNS 플랫폼별 사용자의 주당 활동 시간]")
print(f"1위: {top_platforms[0]}({top_times[0]}시간)")
print(f"2위: {top_platforms[1]}({top_times[1]}시간)")
print(f"3위: {top_platforms[2]}({top_times[2]}시간)")


