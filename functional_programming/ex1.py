import sys

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


# Генератор, который имитирует чтение данных из файла (генерирует числа от 1 до 1000000)
gen = (i for i in range(1, 1000001))
print(f'{sys.getsizeof(gen)} байт')
next(gen)
print(f'{sys.getsizeof(gen)} байт')
next(gen)
print(f'{sys.getsizeof(gen)} байт')
next(gen)
print(f'{sys.getsizeof(gen)} байт')
next(gen)
print(f'{sys.getsizeof(gen)} байт')

print('===============================================')
# Генератор для фильтрации данных (только четные числа)
gen_filter = (i for i in range(1, 11) if i % 2 == 0)
print(next(gen_filter))
print(f'{sys.getsizeof(gen_filter)} байт')
print(next(gen_filter))
print(f'{sys.getsizeof(gen_filter)} байт')
print(next(gen_filter))
print(f'{sys.getsizeof(gen_filter)} байт')
print(next(gen_filter))
print(f'{sys.getsizeof(gen_filter)} байт')
print(next(gen_filter))
print(f'{sys.getsizeof(gen_filter)} байт')
# print(next(gen_filter)) StopIteration

print('===================================')
gen_sqr = (i * i for i in range(1, 11))
print(next(gen_sqr))
print(f'{sys.getsizeof(gen_sqr)} байт')
print(next(gen_sqr))
print(f'{sys.getsizeof(gen_sqr)} байт')
print(next(gen_sqr))
print(f'{sys.getsizeof(gen_sqr)} байт')
print(next(gen_sqr))
print(f'{sys.getsizeof(gen_sqr)} байт')
print(next(gen_sqr))
print(f'{sys.getsizeof(gen_sqr)} байт')
print(next(gen_sqr))
print(f'{sys.getsizeof(gen_sqr)} байт')
print(next(gen_sqr))
print(f'{sys.getsizeof(gen_sqr)} байт')
print(next(gen_sqr))
print(f'{sys.getsizeof(gen_sqr)} байт')
print(next(gen_sqr))
print(f'{sys.getsizeof(gen_sqr)} байт')
print(next(gen_sqr))
print(f'{sys.getsizeof(gen_sqr)} байт')
# print(next(gen_filter)) StopIteration

print('==================================')


# Функцию для агрегации результатов (сумма первых N элементов)
def gen_agr_result(num, N):
    result = 0
    for i in range(N):
        result += num[i]
        yield result


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
N = 5
gen = gen_agr_result(num,N)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) StopIteration