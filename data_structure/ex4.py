# Задание 4: Линейный и бинарный поиск
# Реализуйте:
# 1. Функцию линейного поиска
# 2. Функцию бинарного поиска
# 3. Сравните их производительность на отсортированном списке из 1000 элементов
# 4. Объясните, почему бинарный поиск работает быстрее

"""1. Создать список из 1000 элементов"""
import time

new_list = []
num = 1
while num <= 1000:
    new_list.append(num)
    num+= 1


"1. Функцию линейного поиска. Будем искать число 565"
start = time.perf_counter()
for number in new_list:
    if number == 565:
        break
end = time.perf_counter()
time_lp = end - start

"2. Функцию бинарного поиска. Будем искать число 565"
left_list: int = 0
right_list: int = len(new_list)-1
start = time.perf_counter()
while left_list <= right_list:
    middle: int = (left_list + right_list) // 2
    if new_list[middle] == 565:
        break
    elif new_list[middle] < 565:
        left_list = middle + 1 # ищем в правой половине
    elif new_list[middle] > 565:
        right_list = middle - 1 # ищем в левой половине
end = time.perf_counter()
time_bp = end - start

print(f"Бинарный поиск быстрее чем ленейный в {time_lp/time_bp} раз")