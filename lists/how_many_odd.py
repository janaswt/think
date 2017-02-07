import random
def count_odd(lst):
    odd = 0
    for i in lst:
        if i % 2 != 0:
            odd += 1
    return odd
lst = []
for i in range(100):
    lst.append(random.randint(0, 1000))

print(count_odd(lst))
