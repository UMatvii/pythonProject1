i = 0
suma = 0
for i in range(5):
    x = float(input("Podaj liczbę zmiennoprzecinkowe: "))
    i += 1
    if x > 0:
        suma += x
    else:
        continue
print(suma)