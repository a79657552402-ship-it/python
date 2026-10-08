# Дана некоторая строка:
#
# 'AbCdE'
# Смените регистр букв этой строки на противоположный. В нашем случае должно получится следующее:
#
# 'aBcDe'

string = 'AbCdE'

print(''.join(ch.lower() if ch.isupper() else ch.upper() for ch in string))