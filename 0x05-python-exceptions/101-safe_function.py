#!/usr/bin/python3

import sys

def fct(a, b):
    return a / b


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
    