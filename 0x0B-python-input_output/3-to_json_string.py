#!/usr/bin/python3
"importing json library"
import json
"function that returns the JSON representation of an object"


def to_json_string(my_obj):
    """Function that returns the JSON representation of an object"""
    newstr = json.dumps(my_obj)
    return (newstr)
