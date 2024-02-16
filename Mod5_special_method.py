class Backpack:
    def __init__(self, gift=None):
        self.content = []
        if gift:
            self.content.append(gift)

    def inspect(self):
        # проверка содержимого
        print('В рюкзаке лежит')
        for item in self.content:
            print('   ', item)


    def add(self, item):
         # положить в рюкзак
        self.content.append(item)
        print('в рюкзак положили: ', item)

    def __str__(self):
        return ('В рюкзаке лежит: ' + ', '.join(self.content))

    # def __bool__(self):
    #     return self.content != []

    def __del__(self):
        print('Рюкзак удален')

    def __len__(self):
        return len(self.content)

my_backpack = Backpack(gift='phone')
my_backpack.add(item='ноутбук')

print(bool(my_backpack), len(my_backpack))
if my_backpack:
    print('В рюкзаке лежит ', len(my_backpack), ' предметов')
    my_backpack.inspect()
    # print()
    print(my_backpack)
else:
    print('Рюкзак пуст')


