def sum_to(a_bound):
    the_sum = 0
    for a_number in range(1, a_bound + 1):
        the_sum = the_sum + a_number
    return the_sum
print(sum_to(999))