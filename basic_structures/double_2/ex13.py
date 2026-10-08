# Написать программу на Python для решения квадратного уравнения ax^2 + bx + c = 0.
# Если дискриминант отрицателен, программа должна выдать ошибку и предложить пользователю попробовать еще раз с другими
# коэффициентами. При выполнении скрипта в лог должна записываться информация о успехе или неудаче операции.
import logging
import math
import sys

#  1 -6 9 - один корень

# алгоритм:
# 1. найти дискреминанту: 𝐷 = 𝑏^2 − 4𝑎𝑐 и a не может быть 0
# 2. Если  D>0: уравнение имеет два различных действительных корня
# 3. Если D<0 то программа должна выдать ошибку и предложить пользователю попробовать еще раз с другими коэффициентами
logging.basicConfig(level=logging.INFO, stream=sys.stdout, filemode='w', encoding='utf-8',
                    format="[%(asctime)s] [%(levelname)s]:{%(message)s}")


def insert_data():
    try:
        a = int(input("Введите первое число a:"))
        if a == 0:
            logging.error('Вы ввели не валидные данные, а не может быть равна нулю')
            a = int(input("Введите первое число a ещё раз:"))
            b = int(input("Введите второе число b:"))
            c = int(input("Введите третье число c:"))
            logging.info(f'введены числа {a} и {b} и {c}')
        else:
            b = int(input("Введите второе число b:"))
            c = int(input("Введите третье число c:"))
        logging.info(f'введены числа {a} и {b} и {c}')
    except ValueError:
        logging.error('Вы ввели не валидные данные, повторите попытку')
        a = int(input("Введите первое число a ещё раз:"))
        b = int(input("Введите второе число b ещё раз:"))
        c = int(input("Введите третье число c ещё раз:"))
        logging.info(f'введены числа {a} и {b} и {c}')
    return a, b, c


def descreminante(a, b, c):
    D = b ** 2 - 4 * a * c
    return D

def solve_quadratic(a,b,c,D):
    logging.info(f'Дискреминанта равна {D}')
    if D < 0:
        logging.error(f'Дискреминанта не может быть меньше нуля, введите данные занова')
        a, b, c = insert_data()
        solve_quadratic(descreminante(a, b, c))
    elif D==0:
        x = -b / (2 * a)
        logging.info(f"Успех: D = 0, единственный корень x = {x}")
        return (x)
    else:
        x_1 = (-b + math.sqrt(D))/(2*a)
        x_2 = (-b - math.sqrt(D))/(2*a)
        logging.info(f"Успех: D > 0, два кореня x1 = {x_1}, x2 = {x_2}")
        return (x_1, x_2)

a, b, c = insert_data()
descreminante(a, b, c)
solve_quadratic(a,b,c,descreminante(a, b, c))
