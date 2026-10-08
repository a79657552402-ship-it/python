# 7 Дан датасет. По нему выполните следующие задания:
#
# Найдите час, в который чаще всего совершались сделки. (Подсказка: из ячеек формата DateTime можно извлечь час с помощью .dt.hour; например data['Date'].dt.hour)
# Найдите среднее, медиану и стандартное отклонение у округленных до целого значений df['Price'].
#  Ответы округлите до десятых и выпишите их через пробел.
# Найдите возрастную группу, представители которой чаще являются агентами, не используя фильтрацию. Возрастные группы:
# 0-35: Young
# 36-55: Middle-aged
# 56+: Senior

import logging as log
import sys
import pandas as pd

log.basicConfig(level=log.WARNING, stream=sys.stdout, filemode='w', encoding='utf-8', format="[%(asctime)s] [%(levelname)s]:{%(message)s}")

file = pd.read_csv('C:/Users/Mustafa/Downloads/3.3.2.csv', sep=';')
log.info('Найдите час, в который чаще всего совершались сделки.')
file['Time of deal'] = pd.to_datetime(file['Time of deal'], format='%d.%m.%Y %H:%M')
log.info(f'Передаём часы в список')
hours_list = [t.hour for t in file['Time of deal']]
log.info(f'Список часов {hours_list}')
log.info('создадим словарь в который вставим в качестве ключа час, а в качестве велью это кол-во повторении')
counts = {}
for h in hours_list:
    if h in counts:
        counts[h] += 1
    else:
        counts[h] = 1
log.info(f'Словарь counts {counts}')
log.info('Ищем час в который чаще всего соверщались сделаки')
total = None
max_count = 0
for h, c in counts.items():
    if c > max_count:
        max_count = c
        total = h
log.info(f'Час в котором чаще всего совершались покупки: {total}')
print(f'Час в котором чаще всего совершались покупки: {total}')

log.info('Ищем среднюю медиану')
log.info('Вставляем данные Price в лист')
prices_list = [p for p in file['Price']]
log.info(f'Лист Price: {prices_list}')
log.info('Сортировка пузырком данные листа')
lst = prices_list[:]
for i in range(len(lst)-1):
    for j in range(len(lst)-1-i):
        if lst[j] > lst[j + 1 ]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
log.info(f'Отсартированый prices_list: {prices_list}')
n = len(lst)
median = 0
log.info('Находим медиану')
if n%2==0:
    median= (lst[n // 2 - 1] + lst[n // 2]) / 2
else:
    median = lst[n // 2]
log.info(f'Средняя медиана = {median}')
log.info('среднее откланение, округленое до десятичный значений после.')
mean = round(sum(lst)/n,1)
log.info(f'среднее откланение = {mean}')

log.info('Ищем стандартное отклонение')
variance = sum((x - mean) ** 2 for x in lst) / (n - 1)
std = round(variance ** 0.5,1)
log.info(f'стандартное отклонение = {std}')
print(f'{median} {mean} {std}')

log.info("""Найдите возрастную группу, представители которой чаще являются агентами, не используя фильтрацию. Возрастные группы:\n
                    0-35: Young\n
                    36-55: Middle-aged\n
                    56+: Senior""")
log.info('Вставляем данные в лист')
list_age = [i for i in file['Agent age']]

log.info(f'Список возрастов list_age: {list_age}')
log.info('Создаём счёчики для возрастных категории')
count_young = 0
count_middle = 0
count_senior = 0
for age in list_age:
    if 0 < age < 35:
        count_young+=1
    elif 35 < age < 55:
        count_middle+=1
    else:
        count_senior+=1

log.info(f'count_young: {count_young}')
log.info(f'count_middle: {count_middle}')
log.info(f'count_senior: {count_senior}')


if count_young > count_middle and count_young > count_senior:
    print('возрастная группа, представители которой чаще являются агентами - Young')
elif count_middle > count_young and count_middle > count_senior:
    print('возрастная группа, представители которой чаще являются агентами - Middle-aged')
else:
    print('возрастная группа, представители которой чаще являются агентами - Senior')
