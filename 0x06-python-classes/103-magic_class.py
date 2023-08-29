#!/usr/bin/python3
"""Create MagicClass that exactly matches a Holberton provided bytecode."""

import math


class MagicClass:
    """Create a circle."""

    def __init__(self, radius=0):
        """Create a MagicClass.

        Arg:
            radius (float or int): The new MagicClass radius.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Bring back the MagicClass area."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The MagicClass circumference"""
        return (2 * math.pi * self.__radius)
