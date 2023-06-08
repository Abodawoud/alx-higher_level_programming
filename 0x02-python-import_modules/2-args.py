#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import os

    argvs = sys.argv
    argv_length = len(argvs)
    i = 0
    file_name = os.path.basename(__file__)
    file_path = f"./{file_name}"

    if argv_length == 1:
        print("0 arguments.")
    elif argv_length == 2:
        print("1 argument:")
        print("1: {:s}".format(argvs[1]))
    else:
        print("{:d} arguments:".format(argv_length - 1))
        for argv in (argvs):
            if argv == file_path:
                continue
            i += 1
            print("{:d}: {:s}".format(i, argv))
