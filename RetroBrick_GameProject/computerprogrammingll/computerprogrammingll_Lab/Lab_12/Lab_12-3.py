# 점수 관리
# 클래스 정의
class Score :
    def __init__(self, name="default", score=0) :
        self.name = name
        self.score = score

    def writeFile(self) :
        return self.name+","+str(self.score)+"\n"

# 객체 생성
s1 = Score("김샤넬", 85)
s2 = Score("지방시", 96)

# 객체 내용 파일에 쓰기
cp = open("//res//cp.txt","w")
cp.write(s1.writeFile())
cp.write(s2.writeFile())
cp.close()

# 파일 읽고 폼에 맞추어 보여주기
record = open("//res//cp.txt","r")
for r in record :
    line = r.strip(" ,")
    print(line[0]+"\t"+line[1], end = '') # print 함수 내 출력 끝을 없앰
record.close()

# 새로운 학생추가
print("\n[새로운 학생]")
name = input("이름:")
score = int(input("점수:"))

f = open(".//res//cp.txt","a")
# newS = Score[name.score]
# f.write(newS.writeFile())
# 위 두줄을 요약하면 아래와 같음
f.write(Score(name, score).writeFile())
f.close()