def kwa(lista,a):
    j = False
    for i in range(len(lista)):
        if lista[i]==a:
            j = True
    return j
print(kwa([1,3,5,7,9,11,13,15],15))