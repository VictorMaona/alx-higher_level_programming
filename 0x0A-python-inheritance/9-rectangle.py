#!/usr/bin/python3
"""Creates class Rectangle which is descended from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle representation with BaseGeometry."""

    def __init__(self, width, height):
        """Create a fresh rectangle.

        Args:
            width (int): The new Rectangle width.
            height (int): The new Rectangle height.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Get the rectangle area back."""
        return self.__width * self.__height

    def __str__(self):
        """Return a Rectangle print() and str() representation."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
