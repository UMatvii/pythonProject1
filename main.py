import random as r
zestaw_1 = []
n = int(input("Podaj liczbę elementów: "))
for i in range(n):
    zestaw_1.append(r.randint(1, 10))
print(zestaw_1)

zestaw_2 = []
m = int(input("Podaj liczbę elementów: "))
for i in range(n):
    zestaw_2.append(r.randint(5, 15))
print(zestaw_2)

x = int(input("Podaj liczbę: "))
if x in zestaw_1:
    print("Liczba z zestawu 1")
elif x in zestaw_2:
    print("Liczba z zestawu 2")
else:
    print("Liczba poza zestawami")

zestaw_1_2 = zestaw_1 + zestaw_2
print(zestaw_1_2)
