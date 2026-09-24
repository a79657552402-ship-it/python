# Дано число. Выведите в консоль количество четных цифр в этом числе.

num = 4334611223
count = 0

while num > 0:
    a = num%10
    if a%2==0:
        count+=1
    num//=10
print(count)

