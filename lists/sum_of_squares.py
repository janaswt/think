lst = [2, 3, 4, ]
def sum_of_squares(lst):
    suma = 0
    for i in lst:
        suma += i**2
    return suma
print(sum_of_squares(lst))