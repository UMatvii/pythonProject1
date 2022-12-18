ilość = int(input("Podaj ilość wiersz: "))
for i in range(0, ilość):
    for j in range(0,i+1):
        print("*", end='')
    print()