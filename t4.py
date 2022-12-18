liczba = int(input("Wpisz liczbę 1: "))
liczba1 = int(input("Wpisz liczbę 2: "))
while liczba > liczba1:
    x = liczba1 % 2
    if x != 0:
        liczba1 += 1
        continue
    print(liczba1, end=' ')
    liczba1 += 1
else:
    while liczba1 >= liczba:
        x = liczba % 2
        if x != 0:
            liczba += 1
            continue
        print(liczba, end=' ')
        liczba += 1
