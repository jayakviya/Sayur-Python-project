'''lambda functios - sort by name, sort by cost'''

items = [('tomato',  50),
    ('potato', 30),
   ('onion',70),
   ( 'brinjal', 20)]

sortedByName = sorted(items,key = lambda x:x[0])
print("Sorted Names:")
for item in sortedByName:
    print(item)

sortedByCost = sorted(items,key=lambda x:x[1])
print("sorted costs:")
for item in sortedByCost:
    print(item)

    '''
    def sol(x,y,z):
        '''