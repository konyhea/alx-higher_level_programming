#!/usr/bin/python3
"function returns True if its the same class or inherit from"


def is_kind_of_class(obj, a_class):
    """same class or inherited"""
    return isinstance(obj, a_class)
