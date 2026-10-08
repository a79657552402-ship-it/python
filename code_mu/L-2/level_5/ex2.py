# Дана некоторая строка:#
# 'abcdefg'
# Удалите из этой строки каждый третий символ. В нашем случае должно получится следующее:#
# 'abdeg'
from os import remove

string = 'abcdefg'
print(''.join(ch for i, ch in enumerate(string) if (i + 1) % 3 != 0))
