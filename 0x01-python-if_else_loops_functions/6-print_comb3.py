#!/usr/bin/python3
# 6-print_comb3.py

"""Print every two digit combination that is conceivable in ascending order.

    The two digits differs 01 and 10 are regarded as the same.
    """
for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 8 and digit2 == 9:
            print("{}{}".format(digit1, digit2))
        else:
            print("{}{}".format(digit1, digit2), end=", ")
