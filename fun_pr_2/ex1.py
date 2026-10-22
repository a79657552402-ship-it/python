from basic_structures.double_2.ex19 import total

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
print('========генерирует числа от 1 до 1000000==========')
gen_big_data = (i for i in range(1000001))
g_1 = gen_big_data
print(next(g_1))
print(next(g_1))
print(next(g_1))
print(next(g_1))

# Генератор для фильтрации данных (только четные числа)
print('========только четные числа=======================')
gen_even = (i for i in range(1000001) if i % 2 == 0)
g_2 = gen_even
print(next(g_2))
print(next(g_2))
print(next(g_2))
print(next(g_2))

# Генератор для преобразования данных (возведение в квадрат)
print('========возведение в квадрат=======================')
gen_sgr = (i ** 2 for i in range(1000001))
g_3 = gen_sgr
print(next(g_3))
print(next(g_3))
print(next(g_3))
print(next(g_3))

# Функцию для агрегации результатов (сумма первых N элементов)
print('========сумма первых N элементов=======================')


def agr_data(n, N):
    total = 0
    for i in range(n)[:N]:
        total += i
    yield total


n = 1000001
g_4 = agr_data(n, 5)
print(next(g_4))


# вторая версия
print('================= вторая версия=============')
def create_data(n):
    for i in range(n + 1):
        yield i

def filtar_data(g):
    for i in g:
        if i % 2 == 0:
            yield i

def sqr_data(x):
    for i in x:
        yield i**2

def agr_data_2(n, N):
    total = 0
    for idx, i in enumerate(n):
        if idx >= N:
            break
        total += i
    yield total

n = 1000000
N = 5
result = agr_data_2((sqr_data(filtar_data(create_data(n)))), N)
print(next(result))