x = int(input("Podaj liczbę 1: "))
y = int(input("Podaj liczbę 2: "))
suma = 0
if x > y:
    step = -1
else:
    step = 1
for x in range(x,y, step):
    suma += x
print(suma + y)