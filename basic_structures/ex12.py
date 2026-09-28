# Написать программу для генерации случайных чисел в заданном диапазоне.
# Если пользователь ввел недопустимые границы диапазона (например, меньше нуля),
# программа должна вывести ошибку и попросить ввести диапазон заново. Информация об ошибках должна быть записана в лог.
import logging
import random
import sys

logging.basicConfig(
    level=logging.WARNING,
    stream=sys.stdout,          
    format="%(levelname)s: %(message)s",
)

def round_number(a, b):
    if a < 0 or b < 0 or a > 100 or b > 100:
        logging.warning("Выбран не верный диапазон числе. Допустимы диапозон от 0 до 100")
        print("Повторите попытку, введите a и b")
        a, b = data()
        round_number(a, b)
    else:
        print(random.randint(a, b))


def data():
    print("Введите число a:")
    a = int(input())
    print("Введите число b:")
    b = int(input())
    return a, b


a, b = data()
round_number(a, b)
