from strings import mirroring
def is_palindrome(a_string):
    if a_string in mirroring.reverse(a_string):
        return True
    else:
        return False
print(is_palindrome("abba abba"))
print(is_palindrome("abbas"))