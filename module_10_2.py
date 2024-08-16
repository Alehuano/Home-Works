from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали')
        vol_enemy = 100
        day = 0
        while vol_enemy > 0:
            vol_enemy -= self.power
            day += 1
            print(f'{self.name} сражается {day} дней, осталось {vol_enemy} воинов.')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились')
