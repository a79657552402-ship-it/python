# Создайте список с разными значениями, пройдитесь по нему в цикле и выведите на экран.
# (Сделайте тоже самое со словарем и выведите ключ и значение)

lst = [1, 4, 5, "hellow", False, True, 0, 10]
print("====== for list=========")
[print(i) for i in lst]
print("====== while list=====")
n = len(lst)
i = 0
while n>i:
    print(lst[i])
    i+=1
print("======= DICT ========")
dct={
    "Mash":"19",
    "Dash":"29",
    "Sash":"39"
}

print("======== for dict ==========")
for key in dct:
    print(key, dct[key])

print("======== while dict ==========")
keys = list(dct)
n = len(keys)
i = 0
while i < n:
    key = keys[i]
    print(key, dct[key])
    i += 1

