inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
del(inventory["pears"])
print(inventory)

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
inventory['pears'] = 0
print(inventory)

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
inventory['bananas'] = inventory['bananas'] + 200
numItems = len(inventory)
print(numItems)