#!/usr/bin/python3
import json
"importing json library"
"function that returns object represented by a JSON string "


def from_json_string(my_str):
    """Function that returns the object represented by object JSON """
    newstr = json.loads(my_str)
    return (newstr)
