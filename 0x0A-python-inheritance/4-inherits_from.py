#!/usr/bin/python3
"function that checks if an obj is inherited"


def inherits_from(obj, a_class):
    """Check if obj is inherited directly or indirectly from a_class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
