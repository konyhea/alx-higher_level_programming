#!/usr/bin/python3
import functools


def weight_average(my_list=[]):
    num = list(map(lambda x: x[0] * x[1], my_list))
    denum = functools.reduce(lambda a, b: a+b, [x[1] for x in my_list])
    return sum(num) / denum
