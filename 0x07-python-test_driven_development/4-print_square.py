#!/usr/bin/python3


"""function that prints a sqaure with the character #"""
def print_square(size):
    """ function that print # depending on the size
    
    arguments
    ----------
    size: int
    size is the length of the square, size must be an integer
    if not raise TypeError and size is > 0
    """
    n = size
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        while size:
            print('#' * n)
            size = size - 1
