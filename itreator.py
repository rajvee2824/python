dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key, value in dt.items():
    print(key, value)
    dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key in dt:
    print(key, dt[key])
    dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key in dt.keys():
    print(key)

for value in dt.values():
    print(value)
