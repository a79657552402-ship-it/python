# Дана некоторая строка с буквами и цифрами. Получите позицию первой цифры в этой строке.

string = "fgdf1fghfgh1dffgh3gfhg8"

pos = next(i for i,char in enumerate(string) if char.isdigit())
print(pos+1)
