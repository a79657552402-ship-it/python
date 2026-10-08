# Вывести все числа от 1 до 100, которые делятся на 3 без остатка.

num = [i for i in range(1, 101) if i % 3 == 0]
print(num)

for i in range(1, 101):
    if i % 3 == 0:
        print(i)
