def remove_substr(substr, the_string):
    index = the_string.find(substr)
    if index < 0:
        return the_string
    return_str = the_string[:index] + the_string[index+len(substr):]
    return return_str
print(remove_substr('an', 'banana'))
print(remove_substr('cyc', 'bicycle'))