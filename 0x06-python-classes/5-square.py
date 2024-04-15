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

    def area(self):
        """ returns the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """ property retriever """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        method to print sqaure
        """
        display = ""
        if self.__size == 0:
            print()
        for _ in range(self.__size):
            print('#' * self.__size)
        return
    
