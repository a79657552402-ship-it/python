# Задание 1: Обработка данных с генераторами
# Создайте систему для обработки большого потока данных, используя генераторы. Реализуйте:
#
# Генератор, который имитирует чтение данных из файла (генерирует числа от 1 до 1000000)
# Генератор для фильтрации данных (только четные числа)
# Генератор для преобразования данных (возведение в квадрат)
# Функцию для агрегации результатов (сумма первых N элементов)
# Требования:
#
# Используйте только генераторы, не создавайте промежуточные списки
# Реализуйте цепочку обработки данных
# Измерьте потребление памяти и сравните с обычными списками
import sys
import tracemalloc
from itertools import islice


# Генератор, который имитирует чтение данных из файла (генерирует числа от 1 до 1000000)
def immutator():
    for i in range(1, 1000001):
        yield i

# Генератор для фильтрации данных (только четные числа)
def even_numbers(num):
    for i in num:
        if i % 2 == 0:
            yield i

# Генератор для преобразования данных (возведение в квадрат)
def squaring(num):
    for i in num:
        yield i * i

# Функцию для агрегации результатов (сумма первых N элементов)
def result(num, N):
    return sum(islice(num, N))

# Реализуйте цепочку обработки данных
"""1. включаем генератор, 
   2. оставляем только чётные числа
   3. возводим в квадрат оставщийся числа
   4. суммируем первев N числа"""


def data_processing_chain(N):
    gen_num = immutator()
    event = even_numbers(gen_num)
    sqr = squaring(event)
    summa = result(sqr, N)
    return (summa)


N = 4
print(f'Сумма первых {N} чисел {data_processing_chain(N)} при работы с генератором')
b = sys.getsizeof(data_processing_chain(N))
tracemalloc.start()          # начинаем следить
tracemalloc.reset_peak()     # сбрасываем пик (важно!)
result = data_processing_chain(N)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f'Пиковая память: {peak} байт')

# Функция, который имитирует чтение данных из файла (генерирует числа от 1 до 1000000)
def immutator_def():
    lst = [i for i in range(1, 1000001)]
    return lst


# Функция для фильтрации данных (только четные числа)
def even_numbers_def(num):
    lst = [i for i in num if i % 2 == 0]
    return lst


# Генератор для преобразования данных (возведение в квадрат)
def squaring_def(num):
    lst = [i*i for i in num]
    return lst


# Функцию для агрегации результатов (сумма первых N элементов)
def result_def(num, N):
    return sum(num[:N])

# Реализуйте цепочку обработки данных
"""1. включаем генератор, 
   2. оставляем только чётные числа
   3. возводим в квадрат оставщийся числа
   4. суммируем первев N числа"""
def data_processing_chain_def(N):
    num = immutator_def()
    event = even_numbers_def(num)
    sqr = squaring_def(event)
    summa = result_def(sqr, N)
    return (summa)


N = 4
print(f'Сумма первых {N} чисел {data_processing_chain_def(N)} при работы со списком')
b = sys.getsizeof(data_processing_chain_def(N))
tracemalloc.start()
data_processing_chain_def(N)
current, peak = tracemalloc.get_traced_memory()
print(f'Пиковое потребление памяти: {peak / 1024 / 1024:.2f} МБ')
tracemalloc.stop()