# №4
#
# Дано некоторое число:
#
# 12345
# Получите список цифр этого числа.

num = 12345
lst = []

while num > 0:
    digit = num % 10
    lst.append(digit)
    num//=10
lst.reverse()
print(lst)
