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
        if not isinstance(value, tuple) or len(value) != 2 or \
            not all(isinstance(num, int) for num in value) or \
                not all(num >= 0 for num in value()):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        '''print the # character'''
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        '''defines the print() rep'''
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
