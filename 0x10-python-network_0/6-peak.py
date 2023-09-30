#!/usr/bin/python3
"""Peak"""


def find_peak(lst):
    if not lst:
        return None
    elif len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return max(lst)
    for i in range(1, len(lst) - 1):
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            return lst[i]

    return max(lst[0], lst[-1])
