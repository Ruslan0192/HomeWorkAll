from random import randint

_holder = []
max_stone = 5

def get_stone():
    return _holder

def put_stone():
    # global _holder
    # _holder = []
    for i in range(max_stone):
        _holder.append(randint(1,20))

def is_gameover():
    return sum(_holder) == 0

def take_stone(position, quantity):
    if 1 <= position <= max_stone:
        if _holder[position - 1] >= quantity:
            _holder[position - 1] -= quantity
        else:
            print('Нельзя забрать больше камней чем есть. Переход хода')
