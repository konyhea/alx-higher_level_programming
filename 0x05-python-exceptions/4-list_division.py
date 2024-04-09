#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    try:
        result = [i / j for i, j in zip(my_list_1, my_list_2)]
        for i, j in zip(my_list_1, my_list_2):
            if not isinstance(i, (float| int)) or not isinstance(j, (float | int)):
                result.append(0)
        if j == 0:
            result.append(0)
    except ZeroDivisionError:
        print("division by 0")
    except TypeError:
        print("wrong type")
    except IndexError:
        print("out of range")
    
    finally:
        for i in range(list_length):
            return result

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
        