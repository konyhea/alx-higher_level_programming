#!/usr/bin/python3

def raise_exception():
    try:
        1 + 'e'
    except ValueError as error:
        raise error
