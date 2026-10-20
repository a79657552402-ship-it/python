import math
import sys

#
# n = 10_000_000
#
# lst = [i for i in range(n)]
# gen = (i for i in range(n))
#
# print(sys.getsizeof(lst), " bayt")
# print(sys.getsizeof(gen), " bayt")
#
# keys = ['A', 'B', 'C']
# values = [1, 2, 3]
#
# dct = {k: v ** 5 for k, v in zip(keys, values)}
# print(dct)
#
# values_set = [1, 2, 4, 5, 7, 8, 1, 4, 3, 7, 0, 2, 5]
# data_set = {i**3 for i in values_set if i % 2 == 0}
# print(data_set)
#
#
# def pr():
#     n = 10000000
#     pt = (i for i in range(n))
#     yield pt
#
# p = pr()
# inner = next(p)
# print(next(inner))
# print(next(inner))
# print(next(inner))
# print(next(inner))
# print(next(inner))

'''Функция для подсчёта произведения квадратов сложения двух суммы списков, и разделить их на результат сложения третий суммы'''

'''сумма чисел в списке'''


def summa_def(num: list) -> int | float:
    return sum(num)


'''возведение степень  резултат работы фуекции summa_def'''


def sqr(num: int, stepen: int) -> int | float:
    return math.pow(num, stepen)


'''произведение результата суммы возведеной степени двух списков'''


def product_of_two_numbers(num_1: int, num_2: int) -> int | float:
    return num_1 * num_2


def division(num_1, num_2) -> int | float:
    return num_1 / num_2


'''Деление производение сумм возведеных в степень чисел на результать суммы чисел из списка'''


def result(lst_1, lst_2, lst_3, stepen) -> int | float:
    num_1 = summa_def(lst_1)
    num_2 = summa_def(lst_2)
    num_3 = summa_def(lst_3)
    num_4 = sqr(num_1, stepen)
    num_5 = sqr(num_2, stepen)
    num = product_of_two_numbers(num_4, num_5)
    results = division(num, num_3)
    return results


lst_1 = [1, 3, 5, 7, 2, 3, 10]
lst_2 = [4, 6, 2, 1, 8, 9, 12, 18]
lst_3 = [5, 8, 9, 21, 11, 45, 19, 123]
stepen = 2
print(result(lst_1, lst_2, lst_3, stepen))

lst_new = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst_new_2 = [6, 7, 8, 9, 10]
print(list(map(lambda x: x ** 3, lst_new)))
print(list(filter(lambda x: x % 2 == 0, lst_new)))
print(dict(zip(lst_new, lst_new_2)))
