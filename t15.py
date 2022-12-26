values = [10,20,30]
keys = ["ten", "twenty", "thirty"]
dictionary = dict(zip(keys,values))
print(dictionary)
dictionary1 = dict(thirty = 30, fourty = 40, fifty = 50)
print(dictionary1)
dictionary.update(dictionary1)
print(dictionary)