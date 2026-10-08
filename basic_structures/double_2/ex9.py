# Напишите рекурсивную функцию, которая находит факториалы чисел от 1 до 5 (включительно).

# 1*2*3*4*5

def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)


print(factorial(5))
