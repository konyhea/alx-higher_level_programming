#!/usr/bin/python3
"importing json library"
import json
"function that writes object to a text file using JSon"


def save_to_json_file(my_obj, filename):
    """Function that rites object to a text file using JSon """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
