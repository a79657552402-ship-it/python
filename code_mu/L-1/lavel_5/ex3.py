# Найдите сумму всех целых нечетных чисел в промежутке от 1 до 100.

count = 0

for i in range(1, 101, 2):
    count+=i
print(count)