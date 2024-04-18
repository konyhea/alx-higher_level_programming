#!/usr/bin/python3
"function that checks if an obj is inherited"


def inherits_from(obj, a_class):
    """inherited directly or indirectly"""
    return issubclass(type(obj), a_class)  and type(obj) != a_class
