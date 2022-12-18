import random as rd
zestaw_1_zawierającą = [1,2,3,4,5,6,7,8,9,10]
#ilość = int(input("Podaj ilość liczb: "))
#найти то количевство в листе
#for i in range(ilość):
    #x = rd.randint(0,9)
    #print(zestaw_1_zawierającą[x],end=' ')
#высветлить то количество сслучайных чисел
#print()
zestaw_2_zawierającą = [5,6,7,8,9,10,11,12,13,14,15]
#ilość = int(input("Podaj ilość liczb: "))
#for i in range(ilość):
  #  y = rd.randint(0,9)
   # print(zestaw_2_zawierającą[y],end=' ')

#liczba = int(input("Podaj liczbę: "))
#if liczba in zestaw_1_zawierającą:
 #   print("Licba z zestawu 1")
#elif liczba in zestaw_2_zawierającą:
  #  print("Liczba z zestawu 2")
#else:
    #print("Nie ma takiej liczby w obu zestawach")

zestaw_1_2_zawierającą = zestaw_1_zawierającą + zestaw_2_zawierającą
zestaw_1_2_zawierającą.sort()
print(zestaw_1_2_zawierającą)