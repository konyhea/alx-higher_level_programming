#!/usr/bin/python3

""" sqaure class with size attributes"""


class Square:
    """
    class that defines a square.

    Attributes
    -------------
    size: a private instance attribute
    """
    def __init__(self, size=0, position=(0, 0)):
        """ initializing new square
        size: the size of the sqauare formed
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise ValueError("position must be a tuple of 2\
                 positive integers")
        for args in value:
            if type(args) is not int or args < 0:
                raise ValueError("position must be a tuple of 2 \
                    positive integers")
        self.__position = value

    def my_print(self):
        y = '_' * self.__position[0]
        if self.__size == 0:
            print()
        for _ in range(self.__size):
            print(y + '#' * self.__size)
        return
