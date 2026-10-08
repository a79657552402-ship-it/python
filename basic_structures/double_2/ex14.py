# Написать программу для нахождения среднего арифметического списка чисел.
# Если при вводе списка чисел была допущена ошибка (например, был передан не список, а строка),
# программа должна корректно обработать эту ошибку и выдать соответствующее сообщение.
# Информация об ошибках должна быть записана в лог.
import logging
import sys

logging.basicConfig(level=logging.INFO, stream=sys.stdout, filemode='w', encoding='utf-8',
                    format="[%(asctime)s] [%(levelname)s]:{%(message)s}")


def insert_data_in_list():

    try:
        a = int(input('Введите кол-во эленементов в списке: '))
        logging.info(f'Кол-во элементов в списке: {a}')
        if a < 0:
            logging.error('Кол-во элементов не может быть отрецательным числом, введите кол-во элементов ещё раз')
            a = int(input('Введите кол-во эленементов в списке ещё раз: '))
            logging.info(f'Кол-во элементов в списке: {a}')
    except ValueError:
        logging.error('Кол-во элементов не может быть вещественным числом, введите кол-во элементов ещё раз')
        a = int(input('Введите кол-во эленементов в списке ещё раз: '))
        logging.info(f'Кол-во элементов в списке: {a}')
    try:
        lst = [int(input('Введите число: ')) for _ in range(a)]
        logging.info(f'Созданный список: {lst}')
    except ValueError:
        logging.warning('Введено не верное значение, можно вводить только цыфры')
        lst = [int(input('Введите числы заново: ')) for _ in range(a)]
        logging.info(f'Созданный список: {lst}')
    return lst

def summa_list(lst):
    len_list = len(lst)
    total = (sum(lst))/len_list
    return total


lst = insert_data_in_list()
logging.info(f'Результат выполнение программы является среднеорефмическое значении списка lst: {summa_list(lst)}')