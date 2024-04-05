#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        print("Exception: ValueError Occurred", file=sys.stderr)
        return False
    except TypeError:
        print("Exception: TypeError Occurred", file=sys.stderr)
        return False
