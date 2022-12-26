a = int(input("Podaj liczbę 1: "))
b = int(input("Podaj liczbę 2: "))
suma = 0
a += 3
if a > b:
    step = -3
else:
    step = 3
for a in range(a,b,step):
    suma += a
print(suma)