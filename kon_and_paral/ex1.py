
# 1. Самостоятельно напишите следующие функции для практики алгоритмов:
# *Поиск N-го числа Фибоначчи, **Поиск N-го простого числа* и *Поиск факториала*.
# Запустите данные функции последовательно в одном процессе, а потом - каждую в отдельном процессе.
# С помощью библиотеки time замерьте и сравните время выполнения последовательного и параллельного выполнения программы.

# Поиск N-го числа Фибоначчи

# Поиск конкретного числа в последовательности Фибоначчи — это вычисление n-го числа в последовательности,
# где каждое последующее число равно сумме двух предыдущих.
# Последовательность Фибоначчи начинается с 0 и 1 (или с 1 и 1 — в зависимости от выбранной формы записи).
# Первые числа последовательности: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 и т. д..

import multiprocessing
import time


def fibonachi(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a + b
    return a


def prime_number(n):
    result = []
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            result.append(i)
    return result

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

if __name__ == '__main__':
    start = time.perf_counter()
    fib_result = fibonachi(100000)
    prime_result = prime_number(100000)
    fact_result = factorial(100000)
    results = [fib_result, prime_result, fact_result]
    finish = time.perf_counter()
    print(f'Потраченное время последовательно в одном процессе = {finish - start:.4f} сек')

if __name__ == "__main__":
    with multiprocessing.Pool(processes=3) as pool:
        start = time.perf_counter()
        fib = pool.apply_async(fibonachi,(100000,))
        prime = pool.apply_async(prime_number,(100000,))
        fact = pool.apply_async(factorial,(100000,))
        results = [fib.get(), prime.get(), fact.get()]
        finish = time.perf_counter()
        print(f'Потраченное время последовательно на 3-х процессров через Pool = {finish - start:.4f} сек')

if __name__ == "__main__":
    start = time.perf_counter()
    fib = [multiprocessing.Process(target=fibonachi, args=(100000,)) for i in range(multiprocessing.cpu_count())]
    prime = [multiprocessing.Process(target=prime_number, args=(100000,)) for i in range(multiprocessing.cpu_count())]
    fact = [multiprocessing.Process(target=factorial, args=(100000,)) for i in range(multiprocessing.cpu_count())]
    results = [fib, prime, fact]
    finish = time.perf_counter()
    print(f'Потраченное время последовательно на 3-х процессров = {finish - start:.4f} сек')