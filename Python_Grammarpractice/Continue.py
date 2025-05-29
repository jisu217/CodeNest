numbers = [(1, 2), (10, 0)]

for a, b in numbers:
    if b == 0:
        print("0으로 나눌 수는 없습니다.")
        continue  # 현재 반복을 건너뛰고 다음 반복으로 넘어감 (반복문의 나머지 부분을 보지 않고, 반복문의 처음으로 돌아가는 기능)
    print("{}을(를) {}로 나누면 {}".format(a, b, a/b))
