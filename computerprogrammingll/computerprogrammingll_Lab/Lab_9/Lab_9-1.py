# 아이디 생성하기

users = ["yangdana", "kingwang", "babobabo", "hellopython"]

isStop = True

def checkID(user) :
    global isStop # 함수 내에서 전역 변수를 수정할 수 있도록 선언

    if len(user) < 6 or len(user) > 16 :
        print("글자 수를 맞추어주세요.")

    elif not user.islower() :
        print("소문자가 아닙니다.")

    elif user in users :
        print("중복된 아이디")

    else :
        print("아이디 생성")
        isStop = False # 전역 변수 isStop을 False로 설정하여 반복문 종료

while isStop :
    userID = input("생성할 ID: ")
    checkID(userID)