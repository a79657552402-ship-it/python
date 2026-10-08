
# Вывести значения функции y=x^2 от 1 до 10 с шагом 0.5.

for  i in range(2,22):
    x = i/2
    print(f'y = {x**2}')

print([(i/2)**2 for i in range(2, 22)])