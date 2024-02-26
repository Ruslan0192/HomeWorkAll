class Car:
    price = 1000000
    def horse_powers(self):
        return 150
    def __str__(self):
        return 'машина {}, цена {}, мощность {}.'.format(
            self.__class__.__name__, self.price, self.horse_powers())

class Nissan(Car):
    def horse_powers(self):
        return 120

class Kia(Car):
    def horse_powers(self):
        return 180

my_car = Nissan()
my_car.price = 900000
print(my_car)

my_car = Kia()
my_car.price = 1100000
print(my_car)
