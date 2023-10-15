'''lambda functios - sort by name, sort by cost'''
'''
items = {{'tomato',  50},
    {'potato', 30},
   {'onion',70},
   {'brinjal', 20}}

sortedByName = sorted(items,key = lambda x:x['item'])
print("Sorted Names:")
for item in sortedByName:
    print(item)

sortedByCost = sorted(items,key=lambda x:x['detail'])
print("sorted costs:")
for item in sortedByCost:
    print(item)

'''
items = [{'name': 'tomato', 'cost': 50},
         {'name': 'potato', 'cost': 30},
         {'name': 'onion', 'cost': 70},
         {'name': 'brinjal', 'cost': 20}]

sortedByName = sorted(items, key=lambda x: x['name'])
print("Sorted Names:")
for item in sortedByName:
    print(item)

sortedByCost = sorted(items, key=lambda x: x['cost'])
print("Sorted Costs:")
for item in sortedByCost:
    print(item)