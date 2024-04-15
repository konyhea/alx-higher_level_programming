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
        not isinstance(value[0], int) or not isinstance(value[1], int) or \
        not value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        display = ""
        if self.__size == 0:
            print()
        for _ in range(self.__size):
            print('#' * self.__size)
        return


my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
