#!/usr/bin/python3

def raise_exception_msg(message=""):
    try:
        jen = find_sus(8, 9)
    except NameError as error:
        raise NameError(message) from error
