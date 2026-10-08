# Найти все простые числа от 2 до 50.

# простое число это число которое делиться только на себя и на 1
for i in range(2, 51):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)

