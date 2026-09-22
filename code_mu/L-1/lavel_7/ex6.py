# Дано некоторое число:
#
# 12345
# Найдите сумму цифр этого числа.

num = 12345
total = 0
while num > 0:
    n = num%10
    total+=n
    num//=10
print(total)