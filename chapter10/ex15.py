my_list = [76] + [92.3] + ["hello"] + [True] + [4] + [76]
print(my_list)
my_list.append(76)
print(my_list)
my_list.insert(2, "cat")
my_list.insert(0, 99)
print(my_list.index("hello"))
print(my_list.count(76))
my_list.remove(76)
my_list.pop(my_list.index(True))
print(my_list)