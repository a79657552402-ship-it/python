# Дана некоторая строка, например, вот такая:#
# '023m0df0dfg0'
# Получите сет позиций всех нулей в этой в строке.

string = '023m0df0dfg0'
print({i for i, ch in enumerate(string) if ch == "0"})

