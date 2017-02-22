def reverse(a_string):
    a_reversed = ""
    for char in a_string:
        a_reversed = char + a_reversed
    return a_reversed
def mirror(a_string):
    return a_string + reverse(a_string)

if __name__ == "__main__":
    print(mirror("dupa jaKAS"))
    print(reverse("dupa jakas tu była"))