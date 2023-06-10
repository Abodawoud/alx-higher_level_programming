#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            a = 0
            x = 0
        else:
            a = tuple_a[0]
            x = 0  # User can not put (, 1)
    elif len(tuple_a) >= 2:
        a = tuple_a[0]
        x = tuple_a[1]

    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            b = 0
            y = 0
        else:
            b = tuple_b[0]
            y = 0
    elif len(tuple_b) >= 2:
        b = tuple_b[0]
        y = tuple_b[1]
    new_tuple = (a + b, x + y)
    return (new_tuple)
