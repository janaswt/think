def replace(s, old, new):
    # split string into list by the occurance of "old"
    # use "new" to rejoin the split string/list
    return new.join(s.split(old))
ss = "Mississipi".split('i')
print(ss)
ll = "I".join(ss)
print(ll)
s = 'I love spom! Spom is my favorite food.  Spom, spom, spom, yum!'.split("om")
print(s)
print("am".join(s))