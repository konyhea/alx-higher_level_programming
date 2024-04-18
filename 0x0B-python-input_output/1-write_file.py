#!/usr/bin/python3
"""function that writes a string to a text file"""


def write_file(filename="", text=""):
    """function to write to a text file"""
    with open(filename, "w", encoding='utf-8') as f:
        charLength = f.write(text)
    return charLength
