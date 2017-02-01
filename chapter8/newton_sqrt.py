def newton_sqrt(n, howmany):
    approx = 0.5 * n
    for i in range(howmany):
        better_approx = 0.5 * (approx + n/approx)
        approx = better_approx
    return better_approx

print(newton_sqrt(10, 4))
print(newton_sqrt(10, 5))
print(newton_sqrt(10, 33))