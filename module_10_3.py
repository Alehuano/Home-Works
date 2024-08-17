import threading
import time
import random


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            delta_1 = random.randint(50, 500)
            self.balance += delta_1
            print(f'Пополнение: {delta_1}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            delta_2 = random.randint(50, 500)
            print(f'Запрос на {delta_2}')
            if delta_2 <= self.balance:
                self.balance -= delta_2
                print(f'Снятие: {delta_2}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
