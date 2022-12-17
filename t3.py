wartosc = str(input("Wpisz liczbę od 2 do 10 liczby N: "))
liczcba = list(wartosc)
max_stopen = len(liczcba) - 1
wynik = 0
for i in liczcba:
    if len(liczcba) <= 2 or (len(liczcba) == 1 and i >= "2") or (len(liczcba) == 2 and (i == "1" or i == "0")):
     wynik += (int(i) * 10 ** max_stopen)
     max_stopen -= 1
    else:
     print("Nie mamy taką liczby")
    break
print(wynik)
