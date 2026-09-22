# Дано число. Выведите количество цифр в этом числе.

num = 1234454

count = 0

while num > 0:
    num //= 10
    count += 1
print(count)
