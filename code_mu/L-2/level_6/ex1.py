# Дана некоторая строка с буквами и цифрами. Получите список позиций всех цифр из этой строки.


string = "sd67jhkhj1200ghf"
positions = [i for i, ch in enumerate(string) if ch.isdigit()]
print(positions)
