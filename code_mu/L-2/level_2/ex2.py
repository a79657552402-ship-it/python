# Дан список с числами. Оставьте в нем только положительные числа.

lst = [1, 2, 5, -1, 0, -4]
for num in lst:
    if num < 0:
        lst.remove(num)
print(lst)
