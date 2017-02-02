def encrypt(message, cipher):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for char in message:
        if char == " ":
            encrypted += " "
        else:
            pos = alphabet.index(char)
            encrypted += cipher[pos]
    return encrypted
def decrypt(message, cipher):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted = ""
    for char in message:
        if char == " ":
            decrypted += " "
        else:
            pos = cipher.index(char)
            decrypted += alphabet[pos]
    return decrypted
cipher = "badcfehgjilknmporqtsvuxwzy"

encrypted = encrypt('hello world', cipher)
print(encrypted)

decrypted = decrypt(encrypted, cipher)
print(decrypted)