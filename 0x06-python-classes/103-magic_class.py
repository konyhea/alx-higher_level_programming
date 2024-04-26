#!/usr/bin/python3
'''importing modules'''
import math


class MagicClass:
    '''python class bytecode'''
    def __init__(self, radius=0):
        '''constructor'''''
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("raduis must be a number")
        self.__radius = radius

    def area(self):
        '''calculate area of the circle'''
        return (math.pi * (self.__radius ** 2))

    def circumference(self):
        '''circumference of the circle'''
        return (2 * math.pi * self.__radius)
