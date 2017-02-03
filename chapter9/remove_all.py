def remove_all(substr, the_string):
    it_stil_is = True
    while it_stil_is:
        index = the_string.find(substr)
        if index < 0:
            it_stil_is = False
            return the_string
        the_string = the_string[:index] + the_string[index + len(substr):]
    return the_string
print(remove_all("iss", "Mississipi"))

def remove_all2(substr, the_str):
    new_string = the_str.replace(substr, "")
    return new_string
print(remove_all2("iss", "Mississipi"))        