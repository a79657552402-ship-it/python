# Дана некоторая строка. Найдите позицию третьего нуля в строке.

string = "gfhfgh0gfhfgh0dfhfgh0dfg"

count = 0

lst = list(string)

for i in range(len(lst)):
    if lst[i] == "0":
        count+=1
        if count == 3:
            print(i)
            break