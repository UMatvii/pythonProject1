x = list(range(10))
x[:0] = x[-3:]
x[-3:] = []
print(x)