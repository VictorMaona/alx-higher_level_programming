#!/usr/bin/python3
"""Creates the class Rectangle which is descended from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle representation with BaseGeometry."""

    def __init__(self, width, height):
        """Create a fresh rectangle..

        Args:
            width (int): The new Rectangle width.
            height (int): The new Rectangle height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
