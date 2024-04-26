#!/usr/bin/python3
"""An empty BaseGeometry class"""


class BaseGeometry:
    """class is empty oops"""
    def area(self):
        """public instance methof that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        public instance that validates values
        name will always be a string
        if value is not an integer raise a TypeError
        if value is less than 0, also raise Value Error

        """
        name = str(name)
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ Rectangle inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initialize Rectangle with height and width"""
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
