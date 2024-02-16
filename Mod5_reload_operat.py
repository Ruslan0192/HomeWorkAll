class Buiding:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = int(numberOfFloors)
        self.buildingType = str(buildingType)

    def __eq__(self, other):
        a = self.numberOfFloors == other.numberOfFloors
        b = self.buildingType == other.buildingType
        return a, b

num_flor1 = Buiding(1, 'первый этаж')
# num_flor3 = Buiding(1, 'третий этаж')
num_flor3 = Buiding(3, 'первый этаж')
# num_flor3 = Buiding(3, 'третий этаж')
# num_flor3 = Buiding(1, 'первый этаж')
sravn = num_flor1==num_flor3
if sravn[0]:
    if sravn[1]:
        print('полное совпадение')
    else:
        print('этажи совпали, описание разное')
else:
    if sravn[1]:
        print('номера этажей не совпали, описание сопадает')
    else:
        print('полное отсутствие совпадений')