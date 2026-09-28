# Напишите рекурсивную функцию, которая находит факториалы чисел от 1 до 5 (включительно).
# n = 1*2*3*4*5
# n! = n * (n-1)! 0! = 1 b 1!=1

def factoreal(n):
    if n <= 1:
        return 1
    else:
        return n * factoreal(n - 1)


print(factoreal(5))
