#!/usr/bin/python3
"""Defines a class and a function for checking inherited classes."""


def is_kind_of_class(obj, a_class):
    """Test object to see if it is an instance or an inherited instance of a class.

    Args:
        obj (any): checking the object.
        a_class (type): Matching the type of object class of obj.
    Returns:
        If obj is a direct or indirect descendant of a_class otherwise False then True.
    """
    if isinstance(obj, a_class):
        return True
    return False
