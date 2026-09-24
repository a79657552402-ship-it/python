# Дана некоторая строка:
#
# 'abcde'
# Переведите в верхний регистр все нечетные буквы этой строки. В нашем случае должно получится следующее:
#
# 'AbCdE'

string = 'abcde'
new_str = ''

for i, char in enumerate(string):
    if i % 2 == 0:
        new_str+=char.upper()
    else:
        new_str+=char
print(new_str)        