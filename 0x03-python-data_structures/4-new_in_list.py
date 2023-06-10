#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    c_list = my_list.copy()
    if idx < 0:
        return (c_list)
    elif idx > (len(my_list) - 1):
        return (c_list)
    c_list[idx] = element
    return (c_list)
