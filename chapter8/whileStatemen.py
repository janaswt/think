def sum_to(a_bound):
    """Return the sum of 1+2+3... n"""
    the_sum = 0
    a_number = 1
    while a_number <= a_bound:
        the_sum += a_number
        a_number += 1
    return the_sum

print(sum_to(999))