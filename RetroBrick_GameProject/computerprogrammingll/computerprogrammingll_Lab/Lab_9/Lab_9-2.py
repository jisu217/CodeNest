# 3개의 숫자 정렬

def sort_three_numbers(a = 1, b = 1, c = 1) : # 기본 값으로 1을 설정
    if a > b : # a = 5, b = 3, c = 7인 경우
               # 첫 번째 if 조건: a > b (즉, 5 > 3) 이므로, 이때 a와 b를 교환
               # a = 3, b = 5
               # 교환 이유: 3이 5보다 작으므로, 작은 값 3을 앞으로 보내기 위해 교환
        a, b = b, a
    if a > c :
        a, c = c, a
    if b > c :
        b, c = c, b

    return a, b, c

# 사용 예시
nums = []
for i in range(3) :
    n = int(input("숫자:"))
    nums.append(n)

sorted_numbers = sort_three_numbers(nums[0], nums[1], nums[2])
print("정렬된 숫자:", sorted_numbers)