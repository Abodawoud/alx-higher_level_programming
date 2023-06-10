#!/usr/bin/python3
def max_integer(my_list=[]):
    list_length = len(my_list)
    j = 1

    if list_length == 0:
        return (None)

    for i in my_list:
        if my_list[j] > i:
            maximum_number = my_list[j]

    return (maximum_number)
