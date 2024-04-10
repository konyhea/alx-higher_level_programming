#!/usr/bin/python3

class LockedClass:
    """ A class that prevents the user from dynamicallly creating
    new instances attributes
    """
    __slots__ = "first_name"
