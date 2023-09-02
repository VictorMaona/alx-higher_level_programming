#!/usr/bin/python3
# 4-print_square.py
"""creates a function that prints squares."""


def print_square(size):
    """The # character should appear in square.

    Args:
        size (int): The height and width of square.
    Raises:
        TypeError: Should size not be an integer.
        ValueError: If the size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
