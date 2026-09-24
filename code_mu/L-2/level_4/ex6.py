# Дана дата в следующем формате:
#
# '2025-12-31'
# Преобразуйте эту дату в следующий кортеж:
#
# ('31', '12', '2025')

string = '2025-12-31'

parts = string.split("-")

lst = []
lst.insert(0, parts[2])
lst.insert(1, parts[1])
lst.insert(2, parts[0])
print(lst)