# 스케쥴러

from datetime import date
# 파일 읽기
sch = open(".//res//Scheduler.txt","r")
scheduler = sch.readlines() # 파일 전체의 내용을 리스트로 만듦
sch.close()

weekdays = ['월', '화', '수', '목', '금', '토', '주일']

# 오늘 날짜 기준으로 요일 숫자 가져오기
today = date.today()
weekdayNum = today.weekday() # 0: 월요일 ~ 6: 일요일

# 출력을 위한 폼 맞추기
line1 = ""
line2 = ""
line3 = ""
for w in range(7) :

    # 첫 번째 줄 오늘 날짜 표시
    if w==weekdayNum :
        line1 += "\t"
    else :
        line1 += "  \t"

    # 두 번째 줄
    line2 += weekdays[w] + "\t"

    # 세 번째 줄
    toDo = scheduler[w].split(":")
    if toDo[1] != "\n" :
        line3 += "*\t"
    else :
        line3 += "  \t"

# 실제 출력
print(line1)
print(line2)
print(line3)

print("\n[오늘의 할일]")
toDo = scheduler[weekdayNum].split(":")
if toDo[1] != "\n" : print(toDo[1])
else : print("없음")




from datetime import date
sch = open(".//res//Scheduler.txt","r")
scheduler = sch.readlines() #sch 파일을 리스트로 만듦
sch.close()

weekdays = ['월', '화', '수', '목', '금', '토', '주일']

today = date.today()
weekdayNum = today.weekday()

line1 = ""
line2 = ""
line3 = ""

for w in range(7) :
    # w는 0,1,2,3,4,5,6,7 진행, weekdayNum은 0~7

    # 첫 번째 줄
    if w==weekdayNum :
        line1 += "*\t"
    else :
        line1 += " \t"

    # 두 번째 줄
    line2 += weekdays[w] + "\t"

    # 세 번째 줄
    toDo = scheduler[w].split(":")
    if toDo[1] != "\n" :
        line3 += "*\t"
    else :
        line3 += " \t"

print(line1)
print(line2)
print(line3)

print("\n[오늘의 할일]")
toDo = scheduler[weekdayNum].split(":")
if toDo[1] != "\n" :
    print(toDo[1])
else :
    print("없음")
