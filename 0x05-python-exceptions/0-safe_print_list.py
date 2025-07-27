#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """fnc to print the number of elements in a list"""
    counter = 0
    try:
        for items in my_list[:x]:
            print(items, end="")
            counter += 1
    except Exception:
        pass
    finally:
        print()
    return counter
