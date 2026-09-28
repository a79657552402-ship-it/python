# Написать программу на Python для решения квадратного уравнения ax^2 + bx + c = 0.
# Если дискриминант отрицателен, программа должна выдать ошибку и предложить пользователю попробовать еще раз с другими коэффициентами.
# При выполнении скрипта в лог должна записываться информация о успехе или неудаче операции.
import logging
import math
import sys

#  1 -6 9 - один корень

# алгоритм:
# 1. найти дискреминанту: 𝐷 = 𝑏^2 − 4𝑎𝑐 и a не может быть 0
# 2. Если  D>0: уравнение имеет два различных действительных корня
# 3. Если D<0 то программа должна выдать ошибку и предложить пользователю попробовать еще раз с другими коэффициентами

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("quadratic.log", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)

def insert_data():
    a = int(input("Введите знаечение a:"))
    b = int(input("Введите знаечение b:"))
    c = int(input("Введите знаечение c:"))
    return a,b,c

def solve_quadratic(a, b, c):

    if a == 0:
        logging.error("a не может быть 0")
        return None

    D = b**2 - 4*a*c
    logging.info(f"Коэффициенты: a={a}, b={b}, c={c}; D={D}")

    if D<0:
        logging.warning("D меньше нуля")
        print("введите данные снова")
        a, b, c = insert_data()
        return solve_quadratic(a, b, c)
    elif D==0:
        x = -b/(2*a)
        logging.info(f"Успех: D = 0, единственный корень x = {x}")
        return (x)
    else:
        x_1 = (-b + math.sqrt(D))/(2*a)
        x_2 = (-b - math.sqrt(D))/(2*a)
        logging.info(f"Успех: D > 0, два кореня x1 = {x_1}, x2 = {x_2}")
        return (x_1, x_2)

def insert_data():
    global a, b, c
    a = int(input("Введите знаечение a:"))
    b = int(input("Введите знаечение b:"))
    c = int(input("Введите знаечение c:"))
    return a,b,c



a, b, c = insert_data()
solve_quadratic(a,b,c)