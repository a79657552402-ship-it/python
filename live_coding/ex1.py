
# list
print("========= list =========")
lst = [1, 2, 3, 4, 5]
print(lst[0])
print(lst.pop())
print(lst.pop(2))
lst.remove(1)
print(lst)
lst.append(6)
lst.extend([7,8,9,10])
lst.insert(0,1)
print(lst)
print(lst[0:6:2])
print(list(i for i in lst if i == 5))
print(lst.reverse())
lst.extend([23, 18 , 21])
lst.sort()
lst.reverse()
print(lst)
print("======== sort =======")
lst2 = [1,4,8,2,5,4,7,9]
n = len(lst2)-1
for i in range(n):
    for j in range(n-i):
        if lst2[j] > lst2[j+1]:
            lst2[j], lst2[j + 1] = lst2[j + 1], lst2[j]
print(lst2)



# tuple
print("========== tuple ==========")
tpl = (1,2,1,3,5,6,1)
print(tpl.count(1))
print(tpl)
print(tpl[1:5])
print(tuple(i for i in tpl if i == 1))
print(id(tpl[2]))
print(3 in tpl)

# dict
print("============= dict ==========")
dct = {
    "Masha": ("36", "doctor"),
    "Dasha": ("36", "doctor"),
    "Sasha": ("36", "doctor"),
    "Aysha": ("36", "doctor")
}
print(dct)
print(dct["Masha"])
print(dct.values())
dct["Petya"] = ("41", "engineer")
print(dct)
dct["Dasha"] = ("18", "student")
print(dct)
dct.pop("Aysha")
print(dct)
print("Sasha" in dct)

# set
print("========= set ==========")
st = {1,5,7,9,10,11,18}
st.add(15)
st.remove(1)
st.pop()
print(st)
print(11 in st)
st.update([16, 13, 11])
print(st)

print("======== sort list======")
ls = [4,9,10,7,12,32,11,18]
n = len(ls)-1
for i in range(n):
    for j in range(n-i):
        if ls[j] > ls[j+1]:
            ls[j], ls[j+1] = ls[j+1], ls[j]
print(ls)
