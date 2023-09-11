#!/usr/bin/python3
"""Defines a function that gives objects properties."""


def add_attribute(obj, att, value):
    """If at all possible add new attribute to an object.

    Args:
        obj (any): The object should provide an attribute to.
        att (str): Name of attribute that to be added to obj.
        value (any): The amount att.
    Raises:
        TypeError: if it is impossible to add the attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
