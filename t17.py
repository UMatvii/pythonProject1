def find(lista,watrość):
    indeksy = []
    a = 0
    for i in lista:
        if i == watrość:
            indeksy.append(a)
        a += 1
    return indeksy

x = find([1,4,5,6,2],2)
print(x)