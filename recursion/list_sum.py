def list_sum(a_list):
    if(len(a_list)) == 1:
        return a_list[0]
    else:
        return a_list[0] + list_sum(a_list[1:])
print(list_sum([1, 2, 3, 4, 5, 6,]))
