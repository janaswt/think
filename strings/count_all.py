def count_all(the_string):
    letters = {}
    for char in the_string.lower():
        if char.isalpha():
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] +=1
    return letters
string = "the_string, który jest fajny"
letters = count_all(string)
keys = list(letters.keys())
keys.sort()
for k in keys:
    print(k, "=", letters[k])
 

    