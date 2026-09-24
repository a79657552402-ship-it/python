# '2025-12-31'
# Преобразуйте эту дату в следующий словарь:
#
# {
# 	'year' : '2025',
# 	'month': '12',
# 	'day'  : '31',
# }

string = '2025-12-31'
dct = {}

parts = string.split("-")
print(parts)

dct["year"] = parts[0]
dct["month"] = parts[1]
dct["day"] = parts[2]
print(dct)