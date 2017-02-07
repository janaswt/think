import random
def sum_even(lst):
    eve = 0
    for i in lst:
        if i % 2 == 0:
            eve += i
    return eve
lst = []
for i in range(100):
    lst.append(random.randint(0, 1000))

print(sum_even(lst))

