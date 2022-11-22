values = [10, 20, 30]
keys = ["ten", "twenty", "thirty"]

d = dict(zip(keys, values))
print(d)
#print(list(zip(keys, values)))

d = {keys[i]: values[i] for i in range(len(values))}
print(d)


d1 = dict(thirty = 35, forty = 40, fifty = 50)
print(d1)

d2 = {}
d2 = d.copy()
d2.update(d1)
print(d2)
