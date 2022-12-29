def myfunk(wzrost):
    if wzrost < 120:
        return 0
    elif wzrost >= 120 and wzrost < 150:
        return 1
    else:
        return 2

x = int(input("Wpisz wzrost w cm: "))
print(myfunk(x))