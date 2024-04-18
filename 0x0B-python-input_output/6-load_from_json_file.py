#!/usr/bin/python3
"importing json library"
import json
"function that creates an Object from a JSON file"


def load_from_json_file(filename):
    """Function that creates an Object"""
    with open(filename) as f:
        return json.load(f)
