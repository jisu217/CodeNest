import KBU

# 학생 객체 생성
std1 = KBU.Student( "장원영", "202204018", 4)
std2 = KBU.Student( "차은우", "202204018", 1)

print("[학생정보]")
std1.studentInfo()
std2.studentInfo()

s = KBU.Subject("컴퓨터프로그래밍I", "IC136", 85)
std1.subjects.append(s)

s = KBU.Subject("컴퓨터프로그래밍II", "IC142", 94)
std1.subjects.append(s)

std1.subjects.append(KBU.Subject("현대사회와미술", "II215", 77))

print(f"\n[{std1.name}학생이 수강한 과목 정보]")
std1.subjectsInfo()

print(f"\n[{std1.name}학생외 최종 평균]")
print(f"{std1.courseAvg():.2f}")