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

"""Валидация строк на длину строки. строка не должна быть пустой и не может быть больше 20 символов"""
def str_validator(string: str):
    if len(string) <= 0 or len(string) > 20:
        raise ValueError('Строка не может быть пустой или больше 20 символов')
    return True

"""Валидация диапазона чисел. Число должно быть положительным и не больше 100"""
def num_validator(number):
    if number < 0 or number > 100:
         raise ValueError('Число не может быть отричательной или больше 100 цифр')
    return True

"""Валидация email формата"""
EMAIL_RE = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+"
    r"@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
    r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$"
)

def email_validator(string):
    if not EMAIL_RE.fullmatch(string.strip()):
        raise ValueError('Неверный формать для email')
    return True

"""Функция `create_validator()`, которая принимает условие и возвращает функцию-валидатор"""
def create_validator(data):
    if isinstance(data, str):
        if '@' in data:
            return email_validator(data)
        return str_validator(data)
    if isinstance(data, (int, float)):
        return num_validator(data)
    raise ValueError('Неизвестный формат')

"""Функцию `compose_validators()`, которая объединяет несколько валидаторов"""
def compose_validators(data, *validators):
    for validator in validators:
        validator(data)
    return True

"""Функцию `validate_data()`, которая применяет валидаторы к данным"""
def validate_data(data):
    return compose_validators(create_validator(data))

"""Проверка"""
print(validate_data(23))
print(validate_data("HI"))
print(validate_data("my@mail.ru"))


