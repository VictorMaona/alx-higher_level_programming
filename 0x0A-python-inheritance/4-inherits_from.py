#!/usr/bin/python3
"""Creates a function that checks inherited classes."""


def inherits_from(obj, a_class):
    """Determines whether object is an inherited instance of a class.

    Args:
        obj (any): The object to examine.
        a_class (type): The class that corresponds to obj type.
    Returns:
        If object obj is inherited instance of a_class true otherwise false.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
