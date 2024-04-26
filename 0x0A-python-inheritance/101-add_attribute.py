#!/usr/bin/python3
"""Function that adds a new attribute to an object if possible."""


def add_attribute(obj, attr, value):
    """
    Add a new attribute to an object if possible.
    Raise a TypeError exception if the object can't have new attributes.
    """
    if hasattr(obj, '__dict__') or (hasattr(type(obj), '__slots__') and
                                    '__dict__' in type(obj).__slots__):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
