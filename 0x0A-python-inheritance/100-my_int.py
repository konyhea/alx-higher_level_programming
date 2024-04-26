#!/usr/bin/python3
"""customising my own under the hood functions"""


class MyInt(int):
    """my own customized Int class"""
    def __eq__(self, other):
        # Invert the behavior of the equality operator
        return not super().__eq__(other)

    def __ne__(self, other):
        # Invert the behavior of the inequality operator
        return not super().__ne__(other)
