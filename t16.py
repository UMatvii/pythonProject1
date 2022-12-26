sample_dict = {"name" : "Kely","surname" : "Jones","age" : 25,"salary" : 8000,"city" : "New York" }
slownik = {}
for keys, values in sample_dict.items():
    if keys in sample_dict:
        slownik[keys] = values
print(slownik)
if "surname" in slownik:
    print("Tak, jest")

slownik["location"] = slownik.pop("city")
print(slownik)
#1) создать словарь куда буду добавлять
#2) поиск по ключах
#3) проверка есть ли в списке этот ключ
#4) добавление в список ключей с значениями