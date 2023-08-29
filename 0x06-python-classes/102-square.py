#!/usr/bin/python3
"""rendering of a square."""


class Square:
    """Create a square."""

    def __init__(self, size=0):
        """start a fresh Square.

        Args:
            size (int): New size square dimensions.
        """
        self.size = size

    @property
    def size(self):
        """Give the size square current area again."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """revert to the square current area."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Define the square comparison with ==."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Explain the square comparison with!=."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Explain <  the Square comparison."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the square comparison to <=."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Explain > the square comparison."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the square >= comparison."""
        return self.area() >= other.area()
