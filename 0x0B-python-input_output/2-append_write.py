#!/usr/bin/python3
"""function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """function to append text at EOF"""
    with open(filename, 'a', encoding='utf-8') as f:
        charLength = f.write(text)
    return charLength
