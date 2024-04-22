#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i, j in zip(my_list_1, my_list_2):
            if not isinstance(i, (float| int)) or not isinstance(j, (float | int)):
                result.append(0)
                continue
            if j == 0:
                result.append(0)
                continue
            result.append(i/j)
    except ZeroDivisionError:
        print("division by 0")
    except TypeError:
        print("wrong type")
    except IndexError:
        print("out of range")
    finally:
        return result[:list_length]
