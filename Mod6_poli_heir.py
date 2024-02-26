class Vehicle:
    vehicle_type = None

class Car:
    price = 1000000
    def horse_powers(self):
        return 150

class Nissan (Vehicle, Car):
    vehicle_type = 'автомобиль'
    price = 900000

    def horse_powers(self):
        return 100
    def __str__(self):
        return 'тип {}, цена {}.'.format(self.vehicle_type, self.price)

my_car = Nissan()
print(my_car)

