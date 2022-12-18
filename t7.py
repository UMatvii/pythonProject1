#studenty = int(input("Podaj ilość studentów: "))
x = 1 #(номер студента)
punkty_sum = 0 #(начальная сумма пунктов)
while x == x:
    punkty = int(input(f"Podaj ilość punktów studenta {x}: " ))
    if punkty < 1 or punkty > 100: #если пункты меньше 0 либо пункты больше 100
     break #закончить #continue (продолжить)
    punkty_sum += punkty #(сумма пунктов)
    x += 1 #(увелечение номера студента на 1)



srednia = punkty_sum / (x - 1) #(среднее количество пунктов)
print(f"{srednia:.0f}")


