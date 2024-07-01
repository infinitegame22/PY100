def find_integers(my_tuple):
    my_list = list(my_tuple)
    new_list = []

    for item in my_list:
        if type(item) == int:
           new_list.append(item)

    return new_list



my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
# print(list(my_tuple))
integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]

