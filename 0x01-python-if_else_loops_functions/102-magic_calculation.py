#!/usr/bin/python3
''' function to mimic byte code presented in the 16 ByteCode challenge'''
def magic_calculation(a, b, c):
    '''function to compare argument and return answers'''
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c

