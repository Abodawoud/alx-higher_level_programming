#!/usr/bin/python3
def no_c(my_string):
    list1 = []
    list1[:] = my_string
    for str in list1:
        if str == 'c' or str == 'C':
            index = list1.index(str)
            del list1[index]
    new_string = ''.join(list1)
    return (new_string)