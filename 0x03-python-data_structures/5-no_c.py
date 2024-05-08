#!/usr/bin/python3

def no_c(my_string):
    rs = ""
    for i in my_string:
        if i != 'C' and i != 'c':
            rs += i
    return rs
