#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    add_1 = add(a, b)
    sub_1 = sub(a, b)
    mul_1 = mul(a, b)
    div_1 = div(a, b)
    print("{} + {} = {}".format(a, b, add_1))
    print("{} - {} = {}".format(a, b, sub_1))
    print("{} * {} = {}".format(a, b, mul_1))
    print("{} / {} = {}".format(a, b, div_1))
