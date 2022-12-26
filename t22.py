i = 0
j = 0
suma = 0
for i in range(5):
    x = int(input("Wpisz liczbę: "))
    i += 1
    if x < 0:
        suma += x
        j += 1
    else:
        continue
print(suma / j)