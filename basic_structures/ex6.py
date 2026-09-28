# Найти все простые числа от 2 до 50.
lst = []
for num in range(2, 51):
    if num == 2:
        lst.append(2)
    if num == 3:
        lst.append(3)
    if num % 2 != 0 and num % 3 != 0:
        lst.append(num)
print(lst)
