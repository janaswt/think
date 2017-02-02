def find2(a_string, a_char, start=0, end=None):
    """
    Find and return the index of achar in astring.
    Return -1 if achar does not occur in astring.
    """
    idx = start
    found = False
    if end == None:
        end = len(a_string)
    while idx < end and not found:
        if a_string[idx] == a_char:
            found = True
        else:
            idx += 1
    if found:
        return idx
    else:
        return -1
print(find2('banana', 'a', 2))
ss = "Python strings have some interesting methods."

print(find2(ss, 's'))
print(find2(ss, 's', 7))
print(find2(ss, 's', 8))
print(find2(ss, 's', 8, 13))
print(find2(ss, '.'))
