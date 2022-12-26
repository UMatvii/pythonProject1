x = int(input("Poddadj liczbę dzielnika: "))
i = 0
for i in range(5):
    y = int(input("Podaj liczbę: "))
    if (y % x) == 0:
        print(y)
    else:
        print("Nie jest podzielne: ")
