#!/usr/bin/python3
for i in range(0, 99):
    if i == 98:
        print("{:d}".format(i))
    else:
        print("{:s}, ".format(str(i).zfill(2)), end="")
