#!/usr/bin/python3
"""Establishes the rectangle class."""


class Rectangle:
    """Create a rectangle."""

    def __init__(self, width=0, height=0):
        """Start a new Rectangle.

        Args:
            width (int): The the new rectangle width.
            height (int): The the new rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or change the rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be a >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or change the rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError("the height must be >= 0")
        self.__height = value

    def area(self):
        """Determine the area of the rectangle and report it."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Determine the rectangle perimeter and report it."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the Rectangle printed representation.

        The character # is used to represent the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Give the rectangle string representation back."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
