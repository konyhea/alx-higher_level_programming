#!/usr/bin/python3
'''import the modules you need'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class that inherited from Base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''width property'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        self.validation("width", value, 0)
        '''validates width'''
        self.__width = value

    @property
    def height(self):
        '''height setter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height getter'''
        self.validation("height", value, 0)
        '''validates height'''
        self.__height = value

    @property
    def x(self):
        '''x getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x setter'''
        self.validation("x", value, 1)
        '''validate x'''
        self.__x = value

    @property
    def y(self):
        '''y getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y setter'''
        self.validation("y", value, 1)
        '''validates y'''
        self.__y = value

    def validation(self, name, value, valid=True):
        '''validates method for value'''
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if valid and value < 0:
            raise ValueError(f"{name} must be >= 0")
        elif not valid and value <= 0:
            raise ValueError(f"{name} musr be > 0")
            

    def area(self):
        '''calculate area of'''
        return self.__height * self.__width

    def display(self):
        '''display the # character. x & y inclsuive'''
        lit = '\n' * self.y + \
              (' ' * self.x + '#' * self.width + '\n') * self.height
        print(lit, end='')

    def __str__(self):
        '''overiding __str__ method'''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def update(self, *args, **kwargs):
        '''update using the args'''
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                else:
                    break
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        '''returns dictionary representation of rectangle'''
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y
                }
