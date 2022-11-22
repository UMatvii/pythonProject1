import random as r
punkty = [round(r.uniform(0, 50), 2) for i in range(15)]
print(punkty)

print(f"Najmniejsza liczba punktów:  {min(punkty)}, Największa liczba punktów: {max(punkty)}")

x = float(input("Proszę podać liczbę: "))
if x in punkty:
 print(punkty.index(x))
else:
    print("Nie ma tej liczby")

a=sum(punkty)
b=len(punkty)
sriednia =round(a/b, 2)
print(sriednia)
ponizej=[]
for i in punkty:
    if i < sriednia:
        ponizej.append(i)
print(len(ponizej), ponizej)
powyzej = [i for i in punkty if i > sriednia]
print(len(powyzej), powyzej)

