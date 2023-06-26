#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_of_nums = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
        except Exception as e:
            break
        else:
            num_of_nums += 1
    print("")
    return (num_of_nums)
