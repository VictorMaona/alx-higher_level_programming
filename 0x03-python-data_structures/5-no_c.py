#!/usr/bin/python3
# 5-no_c.py


def no_c(my_string):
    """Get rid of every c and C in the string."""
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
