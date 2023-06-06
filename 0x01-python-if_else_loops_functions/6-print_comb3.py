#!/usr/bin/python3
for number in range(0, 90):
    if ((number % 10) > (number / 10)):
        if number != 89:
            print("{:s}, ".format(str(number).zfill(2)), end="")
        else:
            print("{:d}".format(number))
