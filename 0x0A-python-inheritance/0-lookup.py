#!/usr/bin/python3
"function that returns the list of available attributes"


def lookup(obj):
    """return the list of available attributes"""
    return dir(obj)
