import threading
import time


class Knight(threading.Thread):
    def __init__(self,  name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            time.sleep(1)
            self.days += 1
            self.enemies -= self.power

        print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")
        print(f"{self.name} одержал победу спустя {self.days} день(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 25)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('все битвы кончились')


