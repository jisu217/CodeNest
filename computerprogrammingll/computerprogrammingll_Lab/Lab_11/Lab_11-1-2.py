class Student :
    def __init__(self, name = "default", ID = "000000000", majorNum = 1 ) :
        self.name = name
        self.ID = ID
        self.majorNum = majorNum

        if(majorNum == 1) : self.major = "신학과"
        elif(majorNum == 2) : self.major = "사회복지학과"
        elif (majorNum == 3): self.major = "영유아보육학과"
        elif (majorNum == 4) : self.major = "컴퓨터소프트웨어과"
        elif (majorNum == 2): self.major = "간호학과"

        self.subjects = []

    def setSubjects(self) :
        print(f"({self.ID}){self.name}\t{self.major}")

    def setSubjects(self) :
        for s in self.suzbjects :
            s.showInfo()

    def courseAvg(self) :
        total = 0
        for s in self.subjects :
            total += s.score

        return total/len(self.subjects)
class Subject :
   def __init__(self, name = "defauit", courseNum = "000000000", score = 0 ) :
       self.name = name
       self.courseNum = courseNum
       self.score = score

   def showInfo(self) :
       print(f"({self.couresNum}){self.name}\t{self.score}")