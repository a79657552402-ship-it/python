# Задание 2: Работа со списками.
# Создайте программу, которая:
# 1. Создает список из 10 чисел
# 2. Находит максимальное и минимальное значение
# 3. Сортирует список двумя разными способами
# 4. Измеряет время выполнения каждой операции сортировки
import time

lst = [i for i in range(11)]
print(lst)
min_num = lst[0]
max_num = lst[0]

for num in lst:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
print(min_num)
print(max_num)

"""Сортировка пузырком"""
# смысл в том что мы проходим по списку и проверяем два соседних элемента и меняем их местами
lst_new = [3, 2, 7, 9, 10, 1, 5, 6, 8, 4, 11, 15, 16, 18, 20, 21, 34, 53, 23]
t_start = time.time()
for i in range(len(lst_new)):
    for j in range(i):
        if lst_new[i] < lst_new[j]:
            lst_new[i], lst_new[j] = lst_new[j], lst_new[i]
t_finish = time.time()
time_p = t_finish - t_start
print(lst_new)

"""Сортировка вставками"""
# смысл в том что каждый элемент из не отсортированной части вставляем в отсартированую на нуное место
lst_new_2 = [3, 2, 7, 9, 10, 1, 5, 6, 8, 4, 11, 15, 16, 18, 20, 21, 34, 53, 23]
t_start = time.time()
lst = [lst_new_2[0]]
for i in range(1, len(lst_new_2)):
    inserted = False
    for j in range(len(lst)):
        if lst_new_2[i] < lst[j]:
            lst.insert(j, lst_new_2[i])
            inserted = True
            break
    if not inserted:
        lst.append(lst_new_2[i])
lst_new_2 = lst
t_finish = time.time()
time_s = t_finish - t_start
print(lst_new_2)

print(f'{time_p-time_s}')