liczba = int(input("Wpisz liczbę: "))
suma = 0
i = 0
for i in range(10):
    i += 1
    if liczba != 0:
       suma += liczba
       liczba = int(input("Wpisz liczbę: "))
    elif liczba == 0:
          break
print(suma)