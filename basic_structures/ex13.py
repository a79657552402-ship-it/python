# Написать программу для нахождения среднего арифметического списка чисел.
# Если при вводе списка чисел была допущена ошибка (например, был передан не список, а строка),
# программа должна корректно обработать эту ошибку и выдать соответствующее сообщение.
# Информация об ошибках должна быть записана в лог.
import logging
import sys

logging.basicConfig(
    level=logging.WARNING,
    stream=sys.stdout,
)


def insert_list_length():
    print("Введите длину списка:")
    a = int(input())
    return a


def insert_data(a):
    lst = []
    while len(lst) < a:
        print(f"Введите число для заполнения списка")
        try:
            b = int(input())
        except ValueError:
            logging.error("введены не валидные данные")
            continue
        lst.append(b)
    return lst


def arithmetic_mean(a):
    lst = insert_data(a)
    length_lst = len(lst)
    total = 0

    for i in lst:
        total += i
    mean = total / length_lst
    print(mean)


a = insert_list_length()
arithmetic_mean(a)
