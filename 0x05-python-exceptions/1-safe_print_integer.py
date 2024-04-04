#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except (ValueError, TypeError):
        return False

    #return False



value = 89
safe_print_integer(value)


value = -89
safe_print_integer(value)

value = "School"
safe_print_integer(value)


