#!/usr/bin/python3
"""Class-checking function is defined here."""


def is_same_class(obj, a_class):
    """Determine whether an object is an exact instance of given class.

    Args:
        obj (any): The object to be examined.
        a_class (type): The class that corresponds to type of object.
    Returns:
        True if obj is an exact instance of a_class; otherwise False.
    """
    if type(obj) == a_class:
        return True
    return False
