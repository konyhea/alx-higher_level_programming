#!/usr/bin/python3

def element_at(my_list, idx):
    """ fnc that retrieves an element from a list like in c"""
    if idx < 0 or len(my_list) <= idx:
        return None
    else:
        return my_list[idx]
