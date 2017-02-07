def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
print(is_prime(25))
print(is_prime(7))
print(is_prime(251))
print(is_prime(20))