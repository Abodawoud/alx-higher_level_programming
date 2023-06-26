#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except Exception as e:
        sys.stderr.write(s"Exception: {}\n".format(e))
        return (False)
    else:
        return (True)
