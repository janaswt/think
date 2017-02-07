x = input("Proszę podaj zdanie:")
x = x.lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter_count = {}
for ch in x:
    if ch in alphabet:
        if ch in letter_count:
            letter_count[ch] += 1
        else:
            letter_count[ch] = 1
keys = list(letter_count.keys())
keys.sort()
for char in keys:
    print(char, ":", letter_count[char])