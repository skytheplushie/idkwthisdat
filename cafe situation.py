from threading import Thread
from queue import Queue
from random import randint
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in tables:
                if table.guest is None:
                    guest.start()
                    table.guest = guest
                    print(f'{guest.name} sat at table number {table.number}')
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} is in queue')

    def discuss_guests(self):
        while not self.queue.empty() or any([table.guest for table in tables]):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} ate their meal and left')
                    table.guest = None
                    print(f'table number {table.number} is free')
                elif not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    table.guest.start()
                    print(f'{table.guest.name} left from queue and sat at table number {table.number}')



tables = [Table(number) for number in range(1, 6)]

guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

guests = [Guest(name) for name in guests_names]

cafe = Cafe(*tables)

cafe.guest_arrival(*guests)

cafe.discuss_guests()
