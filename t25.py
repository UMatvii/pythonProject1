i = 0
suma = 0
for i in range(7):
    x = str(input("Podaj znak: "))
    i += 1
    if x != "a" and x != "c":
        suma += len(x)
print(suma)