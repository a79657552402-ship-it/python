from enum import Enum


class Hellow:
    def __enter__(self):
        print('Привет, начнём работать')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Работа выполнена')


with Hellow():
    print('Я работаю')

print('===============================')


class Summa:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __enter__(self):
        self.summa = self.a + self.b
        return self.summa

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('подсчёт закончен')


a = 5
b = 10
with Summa(a, b) as suma:
    print(f'Сумма равна = {suma}')

print('=======================')

class Unm(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3

def day():
    d = Unm.MONDAY
    print(d.name)
    print(d.value)
day()