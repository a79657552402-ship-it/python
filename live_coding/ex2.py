lst = [2, 5, 7, 9, 0]
lst.reverse()
print(lst)

print(lst[::-1])

dct = {
    "Masha": ("31", "doctor"),
    "Dasha": ("18", "model")
}

print(dct["Dasha"])
dct["1"] = ["1"]
print(dct)

st1 = {1, 2, 3, 4}
st2 = {1, 2, 3, 4, 5, 6}

print(st1.intersection(st2))
