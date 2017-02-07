def remove_vovels(s):
    vovels = "aeiouAEIOU"
    s_without_vovels = ""
    for each_char in s:
        if each_char not in vovels:
            s_without_vovels = s_without_vovels + each_char
    return s_without_vovels
print(remove_vovels("compsci"))
print(remove_vovels("aAbEefIijOopUus"))