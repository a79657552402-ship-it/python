# Дана некоторая строка:#
# 'abcdeabc'
# Очистите ее от дублей символов:#
# 'abcde'

string = "abcdeabc"
result = []

for ch in string:
    if ch not in result:
        result.append(ch)
print("".join(result))
