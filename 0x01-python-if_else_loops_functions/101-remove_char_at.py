#!/usr/bin/python3


'''function to remove character at index n'''
def remove_char_at(str, n):
    '''remove and print it'''
    if n < 0 or  n > (len(str)):
        return str
    return str[:n] + str[n+1:]
