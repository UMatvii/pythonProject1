imiona = ['Kasia', 'Tomek', 'Jan', 'Ola', 'Jerzy', 'Marek', 'Piotr','Zuzia', 'Bartek', 'Jacek']
imiona[3] = "Mark"
imiona.insert(4,"Lord")
imiona.sort()
print(imiona)
imiona.insert(0,"Alex")
imiona.insert(1,"Sofia")
imiona.insert(2,"Maria")
imiona.sort()
print(imiona)
for imie in imiona:
    imie = str(input("Wpisz imię: "))
    if imie not in imiona:
        continue
    imiona.remove(imie)
    break
imiona.sort()
print(imiona)
imiona[-1] = "Zus"
imiona.sort()
print(imiona[0:3])
print(imiona[-3:])
for im in imiona:
    im = str(input("Wpisz imię: "))
    if im not in imiona:
        continue
    if im in imiona:
        print("Tak,jest")
    break

imiona.reverse()
print(imiona)
del imiona[-6:]
print(len(imiona))
print(imiona)