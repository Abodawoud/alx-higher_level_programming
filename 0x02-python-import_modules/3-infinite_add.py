#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argvs = sys.argv
    sum = 0
    for arg in argvs:
        if arg != argvs[0]:
            sum += int(arg)
    print(sum)
