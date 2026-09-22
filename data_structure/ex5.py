# Задание 5: Сортировка
# Реализуйте:
# 1. Пузырьковую сортировку
# 2. Сортировку вставками
# 3. Сравните их с встроенной функцией sorted()
# 4. Измерьте время выполнения для разных размеров входных данных

"""'это задача была реализована в задаче ex2.py"""

"""1. Создает список из 10 чисел"""
import time

new_list = [11,4,3,7,9,10,2,8,5,6]

"""Сортировка пузырком"""
lst1 = new_list[:]
start = time.perf_counter()
for i in range(len(lst1)-1):
    for j in range(len(lst1)-1-i):
        if lst1[j] > lst1[j + 1 ]:
            lst1[j], lst1[j + 1] = lst1[j + 1], lst1[j]
end = time.perf_counter()
total_time_p = end - start
print(total_time_p)
print(lst1)

"""Сортировка вставками"""
lst2 = new_list[:]
start = time.perf_counter()
for i in range(1, len(lst2)):
    key = lst2[i]    # текущий элемент, который вставляем
    j = i - 1    # Самый правый элемент отсортированной части имеет индекс i - 1
    # сдвигаем все элементы больше key на одну позицию вправо
    while j >= 0 and lst2[j] > key:
        lst2[j+1] = lst2[j]
        j-= 1
    lst2[j+1] = key # ставим key на освободившееся место
end = time.perf_counter()
total_time_s = end - start
print(total_time_s)
print(lst2)
print(f"Сортировка пузырком быстрее чем сортировка вставкой в = {total_time_p / total_time_s} раз")