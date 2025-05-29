# Quiz12_202404002 강지수
# 남녀 평균 키
# "data.txt"에 본인의 정보를 파일에 쓰고, 다시 읽은 후 남녀 평균 키 구하는 프로그램

# 학번/이름 출력문
print("*****************")
print("202404002/강지수")
print("*****************")

# 사용자로부터 성별과 키를 입력받아 "data.txt"에 이어서 쓰기
gender = input("성별: ")
height = float(input("키: "))

f = open(".//res//data.txt", "a")
f.write(f"{gender},{height}\n")
f.close()

male_height = 0.0  # 남자 키 합계
female_height = 0.0  # 여자 키 합계
male_count = 0  # 남자 인원 수
female_count = 0  # 여자 인원 수

# 파일 열기
f = open(".//res//data.txt", "r")
lines = f.readlines()

# 파일 처리
# "data.txt" 파일을 읽어서 남녀의 각각 총 인원수와 평균키 구하여 소수점 2자리로 표현
for line in lines:
    data = line.strip().split(",")
    g, h = data[0], float(data[1])
    if g == "M":
        male_height += h
        male_count += 1
    elif g == "F":
        female_height += h
        female_count += 1

# 파일 닫기
f.close()

male_avg = male_height / male_count
print(f"남자 {male_count}명의 평균 키: {male_avg:.2f}")
female_avg = female_height / female_count
print(f"여자 {female_count}명의 평균 키: {female_avg:.2f}")