#!/usr/bin/python3
"""
    class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    A class for designing rectangle

    Attributes
    ------------
    width : int
        the width of the rectangle
    height : int
        the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Parameters
        -----------
        width : int
            the width of the rectangle
        height : int
            the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """
        the width setter
        if width is not an int, raise TypeError
        if width is < 0, raise ValueError
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """
        the width setter
        if width is not an int, raise TypeError
        if width is < 0, raise ValueError
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


    def area(self):
        """
        method that finds the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        method that solves the perimeter of the rectangle
        return 0 if both width and height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """ print the rectangle with the character #"""
        result = ""
        for _ in range(self.__height):
            result += '#' * self.__width + '\n'
        return result

    def __repr__(self):
        """ return a string reprsentation of the rectangle to be able
        to recreate new instances
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ detect when deletion """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
