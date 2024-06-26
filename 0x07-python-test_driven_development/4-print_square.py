#!/usr/bin/python3
''' print square function y'all'''


def print_square(size):
    ''' prints a square with the character # '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print('#' * size)
