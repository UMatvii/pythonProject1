import random as rd
#pok_droga = int(input("Wpisz przebyty dystans: "))
pok_droga =rd.randint(1,1001)
print(f"Przejechana droga: {pok_droga} km")
sr_spal = float(input("Wpisz śriednie spalenie na 100km: "))
x = pok_droga * sr_spal / 100
y = x * 6.5
print(f"Przewidywa zużycia paliwa: {x:.0f}l")
print(f"Szacowana koszta podróży: {y:.2f}zł")