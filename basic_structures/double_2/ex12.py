# Написать программу для генерации случайных чисел в заданном диапазоне.
# Если пользователь ввел недопустимые границы диапазона (например, меньше нуля),
# программа должна вывести ошибку и попросить ввести диапазон заново. Информация об ошибках должна быть записана в лог.
import logging
import random
import sys

logging.basicConfig(level=logging.INFO, stream=sys.stdout, filemode='w', encoding='utf-8',
                    format="[%(asctime)s] [%(levelname)s]:{%(message)s}")


def random_data(a, b):
    result = random.randint(a, b)
    logging.info(f"Сгенерировано число {result} в диапазоне [{a}, {b}]")
    return result


def insert_date():
    try:
        a = int(input("Введите первое число:"))
        b = int(input("Введите второе число:"))
        logging.info(f'введены числа {a} и {b}')
    except ValueError:
        logging.warning("Некорректный ввод: не удалось преобразовать в int, введите данные ещё раз")
        a = int(input("Введите первое число ещё раз:"))
        b = int(input("Введите второе число ещё раз:"))
        logging.info(f'введены числа {a} и {b}')
    if 0 < a < 100 and 0 < b < 100 and a <= b:
        return a,b
    else:
        logging.info(f'введены числа {a} и {b} не проходять валидацие, повторите попытку ещё раз' )
        a = int(input("Введите первое число ещё раз:"))
        b = int(input("Введите второе число ещё раз:"))
        logging.info(f'введены числа {a} и {b}')
    return a,b


a,b = insert_date()
random_data(a, b)
