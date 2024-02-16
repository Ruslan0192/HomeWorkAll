# class Bread:
#     def __str__(self):
#         return 'хлеба'
#     def __add__(self, other):
#         return Sandwich(part1=self, part2=other)
#
# class Sausage:
#     def __str__(self):
#         return 'колбасы'
#     # def __add__(self, other):
#     #     return Sandwich(part1=self, part2=other)
#
#
# class Sandwich:
#     def __init__(self, part1, part2):
#         self.part1 = part1
#         self.part2 = part2
#     def __str__(self):
#         return 'Бутерброд состоит из ' + str(self.part1) + ' и ' + str(self.part2)
#
# borodin = Bread()
# salami = Sausage()
# result = borodin +  salami
# print(result)

class Multyplyer:
    def __init__(self, factor=2):
        self.factor = factor
    def __call__(self, *args, **kwargs):
        res = []
        for item in args:
            res.append(item*self.factor)
        return res

um_27 = Multyplyer(27)
result = um_27(1, 2, 3)
print(result)