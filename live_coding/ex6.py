

lst = [1,2,3,'hi', True]

dct = {x: type(x) for x in lst}
print(dct)


def umn(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(umn(2, 3, 4))
