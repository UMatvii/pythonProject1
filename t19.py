def potęga(list1,list2):
    Lista = []
    długość1 = len(list1)
    długość2 = len(list2)
    if długość1 == długość2:
        for i in range(długość1):
            Lista.append(list1[i] ** list2[i])

        return Lista

Lista1 = [3,4,7,1]
Lista2 = [4,7,9,3]
p = potęga(Lista1,Lista2)
print(p)