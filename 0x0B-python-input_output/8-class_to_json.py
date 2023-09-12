#!/usr/bin/python3
"""creates a Python class to JSON function."""


def class_to_json(obj):
    """the representation of straightforward data structure in dictionary."""
    return obj.__dict__
