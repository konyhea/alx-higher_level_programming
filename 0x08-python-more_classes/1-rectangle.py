#!/usr/bin/python3


class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        elif height < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = height
