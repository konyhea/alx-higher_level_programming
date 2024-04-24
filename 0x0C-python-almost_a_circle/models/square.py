#!/usr/bin/python3
'''import from Rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''a sub class from rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''initialization of the inherited square'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''size getter'''
        return self.width

    @size.setter
    def size(self, value):
        '''size setter'''
        self.width = value
        self.height = value

    def __str__(self):
        '''overiding __str__ method'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)
