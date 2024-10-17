from time import sleep
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, we are getting attacked!')
        enemies_count = 100
        day = 0
        while enemies_count > 0:
            enemies_count -= self.power
            day += 1
            if enemies_count < self.power:
                enemies_count = 0
            print(f"{self.name} is fighting for {day} day/days... enemies left {enemies_count}")
            sleep(1)
        print(f'{self.name} won the fight in {day} days!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()