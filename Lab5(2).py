sample_dict = {"name": "Kelly","surname": "Jones","age": 25, "salary": 8000,"city": "New york"}
for key in sample_dict.keys():
    print(f'{key:<10} = {sample_dict[key]:>10}')


for k, v in sample_dict.items():
    print(f'{k:<10} = {v:>10}')


l = ['age', 'name', 'abc']
p = {}
for i in l:
    if i in sample_dict:
        p[i] = sample_dict[i]
print(p)


for d in l:
   x = sample_dict.pop(d, 'bląd')
   print(x)

# for w in sample_dict.values():
#     if w == 'Jones':
#         print('Jest')
#         break
# else:
#     print('Nie ma')

if 'Jones' in sample_dict.values():
    print('Jest')
else:
    print('Nie ma')



