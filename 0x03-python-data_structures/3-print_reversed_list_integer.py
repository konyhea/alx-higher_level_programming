#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list) // 2):
        temp = my_list[i]
        my_list[i] = my_list[len(my_list) - 1 - i]
        my_list[len(my_list) - 1 - i] = temp

    for num in my_list:
        print("{:d}".format(num))
