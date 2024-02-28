
class House:
    def __init__(self):
        self.numberOfFloors = 10


my_house = House()
current_floor = 10

while current_floor>0:
    print('Текущий этаж равен', my_house.numberOfFloors)
    current_floor -=1
    my_house.numberOfFloors = current_floor

# for i in range(10):
#     my_house.numberOfFloors = i+1
#     print('Текущий этаж равен', my_house.numberOfFloors)

