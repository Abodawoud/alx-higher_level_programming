#!/usr/bin/python3
if __name__ == "__main__":
    import decompile
    functions_name = dir(decompile)
    for name in functions_name:
        if name[0:2] != "__":
            print(name)
