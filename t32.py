def myfunk(a,b):
    slownik = {}
    if a > b:
        while a >= b:
            slownik[f"{a}"] = f"{a}**3"
            a -= 1
    else:
        while a <= b:
            slownik[f"{a}"] = f"{a}**3"
            a += 1
    return slownik

a = 2
b = 10
print(myfunk(a,b))

