#!/usr/bin/python3

""" sqaure class with size attributes"""


class Square:

    """
    class that defines a square.

    Attributes
    -------------
    size: a private instance attribute
    """
    def __init__(self, size=0):
        """ initializing new square
        size: the size of the sqauare formed
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
