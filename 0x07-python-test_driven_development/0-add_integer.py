#!/usr/bin/python3
# 0-add_integer.py
"""Creates a function for adding integers."""


def add_integer(a, b=98):
    """Return the result of a and b integer addition.

    Prior to addition float arguments are typecasted to ints.

    Raises:
        TypeError: In event that either a or b is not integer or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
