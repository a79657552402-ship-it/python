import logging
import sys

# Дано целое число K.
# Вывести строку-описание оценки,
# соответствующей числу K(1 — «плохо», 2 — «неудовлетворительно», 3 — «удовлетворительно», 4 — «хорошо», 5 — «отлично»).
# Если K не лежит в диапазоне 1–5, то вывести строку «ошибка».

logging.basicConfig(level=logging.INFO, stream=sys.stdout, filemode='w', encoding='utf-8',
                    format="[%(asctime)s] [%(levelname)s]:{%(message)s}")

ENTER_A_RATING = 'Введите оценку: '
ENTERED_AN_ESTIMATE='Вы ввели оценку:'


def insert_number():
    try:
        a = int(input(ENTER_A_RATING))
        logging.info(f'{ENTERED_AN_ESTIMATE} {a}')
    except ValueError:
        logging.error('Вы ввели не валидное значение, оценка может быть только цыфрой, повторите попытку')
        a = int(input(ENTER_A_RATING))
        logging.info(f'{ENTERED_AN_ESTIMATE} {a}')

    if a < 0 or a > 5:
        logging.error('Вы ввели не валидное значение, оценка может быть только цыфрой то 1 до 5 повторите попытку')
        a = int(input(ENTER_A_RATING))
        logging.info(f'{ENTERED_AN_ESTIMATE} {a}')

    return a


def result_num(a):
    text = ''
    match a:
        case 1:
            text = 'плохо'
        case 2:
            text = 'неудовлетворительно'
        case 3:
            text = 'удовлетворительно'
        case 4:
            text = 'хорошо'
        case 5:
            text = 'отлично'
    logging.info(f'Ваша оценка {a}:{text}')

result_num(insert_number())

