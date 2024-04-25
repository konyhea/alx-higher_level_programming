#!/usr/bin/python3
'''import varaint'''
import json



class Base:
    """first class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        '''constr'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''method that returns the JSON string'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''mwthod that returns the list of the JSON string'''
        if json_string is None or not json_string:
            return '[]'
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs): 
        ''''method that writes the JSON string to a file'''
        fileName  = "{}.json".format(cls.__name__)
        if list_objs is not None:
            list_objs = [objs.to_dictionaary() for objs in list_objs]
        with open(fileName, "w") as f:
            f.write(cls.to_json_string(list_objs))

