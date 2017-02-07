def find(a_string, a_char):
    """Find and return the index of achar in astring.
    Return -1 if achar does not occur in astring."""
    idx = 0
    found = False
    while idx < len(a_string) and not found:
        if a_string[idx] == a_char:
            found = True
        else:
            idx += 1
    if found:
        return idx
    else:
        return -1
print(find("Compsci", "p"))
print(find("Compsci", "C"))
print(find("Compsci", "i"))
print(find("Compsci", "x"))
