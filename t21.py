i = 0
suma = 0
for i in range(5):
    x = str(input("Podaj jeden znak:  "))
    i += 1
    if x == "a":
        suma += len(x)
print(suma)