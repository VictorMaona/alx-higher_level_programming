#!/usr/bin/python3
"""Defines the Square subclass of the rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Create a square."""

    def __init__(self, size):
        """Start a fresh square.

        Args:
            size (int): The new square dimensions.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
