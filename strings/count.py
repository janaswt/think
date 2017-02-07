def count(text, a_char):
    letter_count = 0
    for i in text:
        if i == a_char:
            letter_count += 1
    return letter_count
print(count("Banana", "a"))
a_string = "banana"
print(a_string.count("a"))
print(count(a_string, "a"))