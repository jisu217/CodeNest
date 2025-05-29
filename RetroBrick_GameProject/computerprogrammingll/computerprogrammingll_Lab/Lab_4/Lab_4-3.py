# 구구단 출력

line = ""
for a in range(2,10) : # 뒷 숫자
    for b in range(1,10) : # 앞 숫자
        line = line + str(b) + " X " + str(a) + " = " + str(a*b) + "\t"
        # line 변수에 새로운 문자열을 추가하여 계속 누적하는 방식
        # = line += str(b) + " X " + str(a) + " = " + str(a*b) + "\t"
    print(line) # 출력
    line = "" # 초기화