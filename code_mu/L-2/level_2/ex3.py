# Дана строка. Удалите предпоследний символ из этой строки.

string = "Hi my world"
s = list(string)
s.pop(-2)
string="".join(s)
print(string)