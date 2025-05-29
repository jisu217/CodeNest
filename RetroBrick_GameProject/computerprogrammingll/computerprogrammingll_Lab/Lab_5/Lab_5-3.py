cafeMenu = ["아메리카노", 2700], ["카페라떼", 3500], ["바닐라라뗴", 4200], ["코코넛스무디", 5800]

print("[[메뉴]]")
num = 1
for m in cafeMenu :
    print(f"{num}. {m[0]}\t{m[1]}원")
    num = num + 1

# 장바구니 추기
cart = [] # 리스트로 초기화
num = -1
while num != 0 :
    # num != 0은 사용자가 0을 입력할 때까지 루프를 계속 돌리기 위해 사용됩니다.
    # 만약 num == 0이 되면, 더 이상 메뉴 선택을 진행하지 않으므로 루프가 끝나야 하기 때문입니다.

    # while True로 작성하려면
    # elif num == 0:
    # print("[[[종료]]]")
    # break

    num = int(input("번호(종료는 0):"))

    # 예외처리
    if num < 0 or num >= len(cafeMenu) :
        print("!!!잘못입력!!!")

    # 종료 문구 출력
    elif num == 0 :
            print("[[[종료]]]"3

    else :
         cart.append(cafeMenu[num-1])
        # 사용자가 입력한 번호는 1부터 시작하지만, 파이썬의 리스트는 0부터 시작합니다.
        # 그래서 **num-1**을 통해 사용자 입력을 리스트의 올바른 인덱스에 맞춰주는 것입니다. 이것이 리스트에서 항목을 "거꾸로" 가져오는 게 아닙니다.

# 결과 출력
total = 0
print("\n\n*********주문내역********")
for c in cart :
    print(f"{c[0]}\t{c[1]}원") # 메뉴출력
    total = total + c[1] # 총 금액계산

print("***********************")
print(f"총 개수 \n{len(cart)}개")
print(f"총 금액 \n{total}원")
print("***********************")
