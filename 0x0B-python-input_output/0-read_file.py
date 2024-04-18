#!/usr/bin/python3
"""function that writes strings to a text file"""


def read_file(filename=""):
    """write strings to a text file"""
    with open(filename, "r", encoding='utf-8') as f:
        print(f.read(), end="")
