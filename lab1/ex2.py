# Задание 2: Работа со списками.
# Создайте программу, которая:
# 1. Создает список из 10 чисел
# 2. Находит максимальное и минимальное значение
# 3. Сортирует список двумя разными способами
# 4. Измеряет время выполнения каждой операции сортировки

"""1. Создает список из 10 чисел"""
import time

new_list = [11,4,3,7,9,10,2,8,5,6]

"""Находит максимальное и минимальное значение"""
"""Вариант 1 - методом min и max"""
list_min = min(new_list)
list_max = max(new_list)
print(f"Минальное значение = {list_min}, максимальное значение = {list_max}")

"""Вариант 2 - через цыкл for"""
list_min = new_list[0]
list_max = new_list[0]

for num in new_list:
   if num < list_min:
       list_min = num
   if num > list_max:
       list_max = num
print(f"Минальное значение = {list_min}, максимальное значение = {list_max}")

"""3. Сортирует список двумя разными способами"""
"""4. Измеряет время выполнения каждой операции сортировки"""
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







