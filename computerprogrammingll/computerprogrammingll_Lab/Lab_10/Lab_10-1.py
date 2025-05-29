# 도서관 책 추가

class Book :

    def __init__(self, name, ID, price) :
        self.name = name
        self.ID = ID
        self.price = price

    def printBook(self) :
        print(f"({self.ID}){self.name} {self.price}원")

import random

n = int(input("몇 권 입력?"))
bookList = []

for i in range(n) :

    n = input("이름:")
    p = int(input("가격:"))

    num = "C" + str(int(random.random()*10000))

    b = Book(n, num, p)
    bookList.append(b)

    print("--------------------------------")

print("\n\n [출 력]")
total = 0
for data in bookList :
    data.printBook()
    total = total + data.price

print("--------------------------------")
print(f"\n총 가격:{total}")
print("--------------------------------")
