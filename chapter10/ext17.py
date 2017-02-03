import random
my_lsit = []
my_iter = 0
while my_iter < 100:
    my_lsit.append(random.randrange(0, 1000))
    my_iter += 1

print(my_lsit)
print(len(my_lsit))

my_list2 = []
for i in range(100):
    my_list2.append(random.randrange(0, 1000))
print(my_list2)