def reverse(a_string):
    a_reversed = ""
    a_count = 0
    while a_count < len(a_string):
        a_reversed = a_string[a_count] + a_reversed
        a_count += 1
    return a_reversed
print(reverse("jakas dupa"))