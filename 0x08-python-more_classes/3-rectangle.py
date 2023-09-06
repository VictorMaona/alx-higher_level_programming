#!/usr/bin/python3
"""representing a rectangle class."""


class Rectangle:
    """Gives techniques for representing a rectangle."""

    def __init__(self, width=0, height=0):
        """Creates a new instance of Rectangle..

        Args:
            width (int): the width of the rectangle which is 0 by default.
            height (int): The rectangle height the default value is.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter the width attribute getter."""
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
        """__height getter the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """gives the area of a rectangle with the specified `width` and `height`."""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the size of specified rectangle perimeter `width` and `height`."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """direct printing of instances is possible.

        array of characters that represents the # and creates string.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
