#!/usr/bin/python3
'''importing modules'''
import math


class MagicClass:
    '''python class bytecode'''
    def __init__(self, raduis):
        '''constructor'''''
        self.__raduis = 0
        if type(raduis) is not int and type(raduis) is not float:
            raise TypeError("raduis must be a number")
        self.__raduis = raduis

    def area(self):
        '''calculate area of the circle'''
        return (math.pi * (self.__raduis ** 2))

    def circumference(self):
        '''circumference of the circle'''
        return (2 * math.pi * self.__raduis)
