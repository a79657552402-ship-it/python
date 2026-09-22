# Дано число. Выведите в консоль сумму первой и последней цифры этого числа.

num = 12234342

num_first = 0
num_last = num % 10

while num > 9:
    num//=10
    num_first = num
print(f"Cумма первого и последнего числа = {num_last+num_first}")

