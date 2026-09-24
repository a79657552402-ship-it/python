# Дан список со строками. Оставьте в этом списке только те строки, которые заканчиваются на .html.

lst = ["gdfgfh.html", "gdfgd", "fdfgfdg", "gdfgdg.html"]
lst2=[]
for i in lst:
    if i.endswith(".html"):
        lst2.append(i)
lst.clear()
lst.extend(lst2)
print(lst)