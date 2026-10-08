# Даны два целых числа:
# D(день) и M (месяц), определяющие правильную дату невисокосного года.
# Вывести значения D и M для даты, следующей за указанной.
import logging
import sys

logging.basicConfig(level=logging.INFO, stream=sys.stdout, filemode='w', encoding='utf-8',
                    format="[%(asctime)s] [%(levelname)s]:{%(message)s}")


def insert_month():
    try:
        M = int(input('Введите номер месяца: '))
    except ValueError:
        logging.error('Введены не верные данные, номер месяца должен быть цыфрой, повторите попытку')
        M = int(input('Введите номер месяца: '))
    except:
        logging.error('Введены не верные данные, номер месяца должен быть целым числом, повторите попытку')
        M = int(input('Введите номер месяца: '))
    if not (1 <= M <= 12):
        logging.warning('Номер месяца должен быть в диапазоне от 1 до 12, повторите попытку')
        M = int(input('Введите номер месяца: '))
    return M


def insert_day(M):
    try:
        D = int(input('Введите номер дня: '))
    except ValueError:
        logging.error('Введены не верные данные, номер дня должен быть цыфрой, повторите попытку')
        D = int(input('Введите номер дня: '))
    except TypeError:
        logging.error('Введены не верные данные, номер дня должен быть целым числом, повторите попытку')
        D = int(input('Введите номер дня: '))

    match M:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            if D < 0 or D > 31:
                logging.warning('Кол-во дней должен быть в диапазоне от 1 до 31, повторите попытку')
                D = int(input('Введите номер дня: '))
        case 4 | 6 | 9 | 11:
            if D < 0 or D > 30:
                logging.warning('Кол-во дней должен быть в диапазоне от 1 до 30, повторите попытку')
                D = int(input('Введите номер дня: '))
        case 2:
            if D < 0 or D > 28:
                logging.warning('Кол-во дней должен быть в диапазоне от 1 до 28, повторите попытку')
                D = int(input('Введите номер дня: '))
    return D

DAYS_IN_MONTH = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

def next_day(D, M):
    if D < DAYS_IN_MONTH[M]:
        new_D, new_M = D + 1, M
    elif M == 12:
        new_D, new_M = 1, 1
    else:
        new_D, new_M = 1, M + 1

    logging.info(f'Следующая дата: {new_D}/{new_M}')
    return new_D, new_M


M = insert_month()
D = insert_day(M)
next_day(D, M)
