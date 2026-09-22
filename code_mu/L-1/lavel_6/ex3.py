# Дан список с числами:
#
# [1, 2, 3, 4, 5]
# Найдите сумму квадратных корней элементов этого списка.
import math

lst = [1, 2, 3, 4, 5]
count = 0

for i in lst:
    n = math.sqrt(i)
    count+=n
print(count)
