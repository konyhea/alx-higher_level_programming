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
        self.__width = width
        self.__height = height

    def get_width(self):
        """ width getter """
        return self.__width

    def set_width(self, width):
        """
        the width setter
        if width is not an int, raise TypeError
        if width is < 0, raise ValueError
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    def get_height(self):
        """ height getter """
        return self.__height

    def set_height(self, height):
        """
        the width setter
        if width is not an int, raise TypeError
        if width is < 0, raise ValueError
        """
        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        elif height < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = height
