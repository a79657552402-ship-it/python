# Дан список со строками. Оставьте в этом списке только те строки, которые начинаются на http://.

lst = ["http://dfsdf", "dfgghghgh", "vbfgghfghd", "http://cvbcvbcb"]
result = []
for s in lst:
    if s.startswith("http://"):
       result.append(s)
print(result)