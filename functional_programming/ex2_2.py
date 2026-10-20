import re

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

def len_str(string:str):
    if len(string)<=0:
        raise ValueError('Валидция не пройдена')

def range_of_numbers(number: int):
    if number <=0 or number >=1000:
        raise ValueError('Валидция не пройдена')

EMAIL_RE = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+"
    r"@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
    r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$"
)

def email_validate(string:str):
    if not EMAIL_RE.fullmatch(string.strip()):
        raise ValueError('Валидция не пройдена')

# Функцию `create_validator()`, которая принимает условие и возвращает функцию-валидатор
def create_validator(condition):
    def validator(value):
        condition(value)
        return True
    return validator

# Функцию `compose_validators()`, которая объединяет несколько валидаторов
def compose_validators(*validators):
    def composed(value):
        for v in validators:
            v(value)
        return True
    return composed

# Функцию `validate_data()`, которая применяет валидаторы к данным
def validate_data(data, validator):
    for value in data:
        try:
            validator(value)
        except ValueError as e:
            print(f'Ошибка для {value!r}: {e}')

validate_len   = create_validator(len_str)
validate_range = create_validator(range_of_numbers)
validate_email = create_validator(email_validate)

# список из одного элемента — валидный
validate_data(['string'], compose_validators(validate_len))

# список из одного элемента — невалидный
validate_data([''], compose_validators(validate_len))

# список из нескольких элементов
validate_data(['', 'ok', 'another'], compose_validators(validate_len))

# числа
validate_data([500, 1500, -1], compose_validators(validate_range))

# email
validate_data(['a@b.co', 'bad', ''], compose_validators(validate_len, validate_email))
