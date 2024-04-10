#!/usr/bin/python3
"""
    class lockedClass with no class or object
"""
class LockedClass:
    """ A class that prevents the user from dynamicallly creating
    new instances attributes
    """
    __slots__ = ["first_name"]
