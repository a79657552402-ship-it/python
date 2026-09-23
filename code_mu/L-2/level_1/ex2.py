# Дана некоторая строка. Найдите позицию первого нуля в строке.

string = "hy 0 my 0"
for i in range(len(string)-1):
    if string[i] == "0":
        print(i)
        break