
# Создайте список с разными значениями,
# пройдитесь по нему в цикле и выведите на экран.
# (Сделайте тоже самое со словарем и выведите ключ и значение)

lst = [1,3,7,'fgdf', True]

for i in lst:
    print(i)

dct={
    'num': 1,
    'num2':2,
    'str':'fgdt',
    'bool':True
}

for key in dct:
    print(f'{key}:{dct[key]}')
