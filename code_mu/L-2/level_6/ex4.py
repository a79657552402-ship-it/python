# Дана некоторая строка со словами:
#
# 'aaa bbb ccc eee fff'
# Сделайте заглавным первый символ каждого второго слова в этой строке. В нашем случае должно получится следующее:
#
# 'aaa Bbb ccc Eee fff'

string = 'aaa bbb ccc eee fff'
parts = string.split()
s = []
print(parts)
for i, v in enumerate(parts):
    if i % 2 == 1:
        v = v[0].upper() + v[1:]
    s.append(v)
print(s)