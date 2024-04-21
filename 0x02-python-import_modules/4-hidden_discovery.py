#!/usr/bin/python3
from hidden_4 import *

if __name__ == "__main__":
    arrayFunction = dir()
    for i in range(0, len(arrayFunction)):
        if arrayFunction[i][:2] != '__':
            print("{:s}".format(arrayFunction[i]))
