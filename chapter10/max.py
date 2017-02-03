import random
def max_from_list(lst):
    max_lst = 0
    for e in lst:
        if e > max_lst:
            max_lst = e
    return max_lst
lst = []
for i in range(100):
    lst.append(random.randrange(0, 1000))
print(max_from_list(lst))