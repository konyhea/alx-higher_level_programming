#!/usr/bin/python3
class LockedClass:
    __slots__ = "first_name"

lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))