A, B, C = map(int, input().split())

numbers = [A, B, C]
numbers.sort()
print(numbers[0], numbers[1], numbers[2])


# 최대값 구하기
# if A >= B and A >= C:
#     max_value = A
# elif B >= A and B >= C:
#     max_value = B
# else:
#     max_value = C
#
# print(max_value)