class Car :
    def __init__(self, company, model, year, price) :
        self.company = company
        self.model = model
        self.year = year
        self.price = price

    def display_info(self) :
        return f"{self.year} {self.company} {self.model}, 가격: {self.price}만원"

class Dealer :
    def __init__(self, name) :
        self.name = name
        self.inventory = []

    def add_car(self, car) :
        self.inventory.append(car)
        print(f"{car.display_info()} 추가되었습니다.")

    def sell_car(self, car) :
        if car in self.inventory :
            self.inventory.remove(car)
            print(f"{car.display_info()} 판매되었습니다.")
        else :
            print("해당 차량은 재고에 없습니다.")

    def display_inventory(self) :
        print(f"{self.name}의 재고 목록:")
        for car in self.inventory :
            print(car.display_info())