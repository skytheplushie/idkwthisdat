import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            value = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += value
            print(f'u have added {value} to ur balance. at the moment u have {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            value = randint(50, 500)
            print(f'u have asked to take {value}')
            if value <= self.balance:
                self.balance -= value
                print(f'the taking was successful. balance at the moment {self.balance}')
            else:
                print('not enough funds! the asking declined')
                self.lock.acquire()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()


print(f'total balance: {bk.balance}')