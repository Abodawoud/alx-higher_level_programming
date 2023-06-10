#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    even = 0
    list = []
    for i in my_list:
        if i % 2 == 0:
            even = 1
        else:
            even = 0
        if even:
            list.append(True)
        else:
            list.append(False)
    return (list)
