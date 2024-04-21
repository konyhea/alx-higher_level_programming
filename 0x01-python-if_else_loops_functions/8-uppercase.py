#!/usr/bin/python3

def uppercase(s):
    upper_str = ""
    for char in s:
        if 97 <= ord(char) <= 122:  # Check if lowercase
            upper_str += chr(ord(char) - 32)  # Convert to uppercase
        else:
            upper_str += char
    print("{}".format(upper_str), end="\n")
