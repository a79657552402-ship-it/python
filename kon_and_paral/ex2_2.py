import threading
import time


# 2. Создайте класс BankAccount с полем balance, реализуйте методы deposit(amount: float) (пополнение) и withdraw(amount: float) (списание).
# Запустите несколько потоков, которые одновременно меняют баланс и добейтесь возникновения RaceCondition.
# Скопируйте код, в копии избавьтесь от RaceCondition одним из методов ограничения потоков.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        self.balance -= amount


def deposit_many(account):
    for i in range(10):
        account.deposit(1)


def withdraw_many(account):
    for i in range(10):
        account.withdraw(10)


if __name__ == '__main__':
    account = BankAccount(1000)
    t1 = threading.Thread(target=deposit_many, args=(account,))
    t2 = threading.Thread(target=withdraw_many, args=(account,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Ожидали: 1000")
    print("Получили:", account.balance)