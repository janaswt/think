def reverse(a_string):
    a_reversed = ""
    a_count = 0
    while a_count < len(a_string):
        a_reversed = a_string[a_count] + a_reversed
        a_count += 1
    return a_reversed
print(reverse("jakas dupa"))
def reverse2(a_string):
    text_reversed = a_string[::-1]
    return text_reversed
print(reverse2("jakas dupa"))