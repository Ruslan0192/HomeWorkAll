from random import randint

class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print('Установленный этаж:', floors)

my_house = House()
for _ in range(5):
    current_floor = randint(1, 10)
    my_house.setNewNumberOfFloors(floors=current_floor)
