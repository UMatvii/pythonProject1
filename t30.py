def kwa(a,b,c):
    lista = []
    if a > b:
        while a >= b:
            lista.append(a)
            a -= c
    else:
        while b >= a:
            lista.append(a)
            a += c

    return lista

a = 1
b = 25
c = 3
print(kwa(a,b,c))