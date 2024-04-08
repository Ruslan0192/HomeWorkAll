
import time
from threading import Thread

class Knight(Thread):
    def __init__(self, name, skills, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.attack = 100
        self.name = name
        self.skills = skills
    def run(self):
        day = 0
        while self.attack > 0:
            self.attack -= self.skills
            day += 1
            print(f'{self.name} сражается {day} день(дня)..., осталось {self.attack} воинов')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {day} дней!')

lanselot = Knight(name='Lanselot', skills=10)
galahat = Knight(name='Galahat', skills=20)

print(f'{lanselot.name}, на нас напали!')
print(f'{galahat.name}, на нас напали!')

lanselot.start()
time.sleep(0.5)
galahat.start()

lanselot.join()
galahat.join()
print('Все битвы закончились!')