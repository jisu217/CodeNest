# Quiz10_202404002 강지수
# 유기동물 입양

# 학번/이름 출력문
print("*****************")
print("202404002/강지수")
print("*****************")
print("\n[[[보호중 아이들]]]")

# Pet 클래스 정의
class Pet:
    def __init__(self, region, category, species, name):
        self.region = region
        self.category = category
        self.species = species
        self.name = name

    def displayInfo(self):
        return f"[{self.region}] {self.species} '{self.name}' {self.category} 책임분양♥︎"

# 객체 생성
pet1 = Pet("서울본점", "고양이", "랙돌", "까망이")
pet2 = Pet("인천지점", "고양이", "코리안 숏 헤어", "비호")
pet3 = Pet("수원동탄", "강아지", "래브라도 리트리버", "다비")
pet4 = Pet("수원동탄", "강아지", "말티푸", "럭키")
pet5 = Pet("수원동탄", "고양이", "코리안숏헤어", "배꼽이")
pet6 = Pet("수원동탄", "고양이", "코리안숏헤어", "밀크")
pet7 = Pet("수원동탄", "강아지", "포메라니안", "봉구")
pet8 = Pet("김포지점", "고양이", "먼치킨", "아훌")

# List에 pet1~8까지 해당하는 객체 추가
pets = [pet1, pet2, pet3, pet4, pet5, pet6, pet7, pet8]

# Pet에 대한 정보 List를 이용하여 출력
for pet in pets:
    print(pet.displayInfo())

# List 마지막에 강아지와 고양이의 수 출력
totalDog = sum(1 for pet in pets if pet.category == "강아지")
totalCat = sum(1 for pet in pets if pet.category == "고양이")
print(f"강아지 총 {totalDog}마리")
print(f"고양이 총 {totalCat}마리")
