#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if sentence == "":
        first = None
    else:
        first = sentence[0]
    my_result = (length, first)
    return my_result
