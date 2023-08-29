#!/usr/bin/python3
"""rendering of a square."""


class Square:
    """Create a square."""

    def __init__(self, size=0):
        """start a fresh Square

        Args:
            size (int): New size square dimensions.
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Give the square current area again."""
        return (self.__size * self.__size)
