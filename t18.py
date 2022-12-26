def sum_of_values(słownik):
    suma = 0
    for x in słownik.values():
        suma += x
    return  suma


wartość = sum_of_values({'data1':-1, 'data2':-6, 'data3':2})
print(wartość)