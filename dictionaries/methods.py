inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
for akey in inventory.keys():
    print("Got key", akey, "which maps to value", inventory[akey])
ks = list(inventory.keys())
print(ks)
for k in inventory:
    print("Got key", k)
print(list(inventory.values()))
print(list(inventory.items()))

for (k, v) in inventory.items():
    print("Got", k, "that maps to", v)
for k in inventory:
    print("Got", k, "that maps to", inventory[k])
print('apples' in inventory)
print('cherries' in inventory)

if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print("We have no bananas")