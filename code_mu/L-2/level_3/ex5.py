# {
# 	'a': 1,
# 	'b': 2,
# 	'c': 3,
# 	'd': 4,
# }
# Получите сет его значений:
#
# {1, 2, 3, 4}

dct = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}

st = set()

for key in dct:
    st.add(dct[key])
print(st)
