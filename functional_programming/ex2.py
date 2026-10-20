# Задание 2: Функции высшего порядка
# Создайте систему валидации данных, используя функции высшего порядка:
#
# Функцию `create_validator()`, которая принимает условие и возвращает функцию-валидатор
# Функцию `compose_validators()`, которая объединяет несколько валидаторов
# Функцию `validate_data()`, которая применяет валидаторы к данным
# Требования:
#
# Используйте замыкания
# Реализуйте композицию функций
# Создайте несколько различных валидаторов (длина строки, диапазон чисел, email формат)
import re
from functools import partial

EMAIL_RE = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+"
    r"@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
    r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$"
)

def create_validator(data):
    if isinstance(data, int):
        if data < 0 or data > 1000:
            print('невалидные данные')
        return
    if isinstance(data, str):
        if len(data) == 0  or len(data) > 20:
            print('невалидные данные')
            return
    if '@' in data and not EMAIL_RE.fullmatch(data.strip()):
        print('невалидные данные')
        return
    return


# create_validator(5)
# create_validator(10000)
# create_validator('')
# create_validator('hell')
# create_validator('hell wordhell wordhell wordhell wordhell wordhell wordhell wordhell word')
# create_validator('mu@er.ru')
# create_validator('mu@re')


def summa(a,b):
    print(a+b)

summa_2 = partial(summa, b = 10)
summa_2(2)
