#!/usr/bin/python3
"""fnc to find the highest in a list"""
def max_integer(my_list=[]):
    if not my_list:
        return None

    max_num = my_list[0]
    for num in my_list[1:]:
        if num > max_num:
            max_num = num
    return max_num
