# -*- coding: utf-8 -*-

from Mod4_game_engine import get_stone, put_stone, is_gameover, take_stone
from termcolor import cprint, colored

put_stone()
user_number = 2

while True:
    cprint('Текущая позиция', color='green')
    cprint(get_stone(), color='green')
    user_number = 2 if user_number == 1 else 1
    user_color = 'blue' if user_number == 1 else 'yellow'
    cprint('Ход игрока {}'.format(user_number), color='blue')

    pos = int(input(colored('Откуда берем?', color=user_color)))
    qnt = int(input(colored('Сколько берем', color=user_color)))
    take_stone(position=pos, quantity=qnt)

    if is_gameover():
        break
cprint('Выиграл игрок {}'.format(user_number), color=user_color)