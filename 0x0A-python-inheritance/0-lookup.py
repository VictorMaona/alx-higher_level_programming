#!/usr/bin/python3
"""Establishes function for object attribute lookup."""


def lookup(obj):
    """Bring back list of object available characteristics."""
    return (dir(obj))
