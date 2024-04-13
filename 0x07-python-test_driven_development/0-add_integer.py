#!/usr/bin/python3


"""function that adds two integr"""
def add_integer(a, b=98):
    """ function that returns the sum of two integers

    arguments
    -----------
    a and b must be either integers or floats, if not raise a TypeError
    if either of the argument is float type,  type caste to an int    
    """
    if not isinstance(a, (float, int)) or not isinstance(b, (float, int)):
        raise TypeError("a must be an integer or b must be an integer")
    elif isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    return (a + b)
