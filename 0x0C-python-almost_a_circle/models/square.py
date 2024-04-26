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

    def update(self, *args, **kwargs):
        '''update using the args'''
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                else:
                    break
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        '''returns the dictionary rep of a square'''
        return {
            "id": self.id, "size": self.width,
            "x": self.x, "y": self.y
        }
