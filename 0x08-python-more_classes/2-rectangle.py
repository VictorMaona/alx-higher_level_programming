#!/usr/bin/python3
"""Establishes the Rectangle class."""


class Rectangle:
    """rectangle class that can build upon and be extended."""

    def __init__(self, width=0, height=0):
        """Creates a new instance of Rectangle..

        Args:
            width (int): The width of the rectangle which is 0 by default.
            height (int): The rectangle height which is by default 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter is 'width' getter method."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """__width getter is 'width' getter method height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """provides the rectangle area back."""
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter of rectangle with the specified `width` and `height`."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
