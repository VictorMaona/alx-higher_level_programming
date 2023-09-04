#!/usr/bin/python3
"""1-rectangle class can be extended and built upon as needed.
"""


class Rectangle:
    """A rectangle is represented by this class by
    combining two arguments.

    Args:
        width (int): Rectangles have a default width of 0.
        height (int): Rectangles have a default height of 0.

    """
    def __init__(self, width=0, height=0):
        # An attribute is assigned the setters listed are engaged.
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter procedure.

        Returns:
            __width (int): rectangle horizontal measurement

        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method.

        Args:
            value (int): the rectangle width

        Attributes:
            __width (int): rectangle horizontal measurement

        Raises:
            TypeError: If the `value` is not an integer.
            ValueError: If 'value' is not 0.

        """
        if type(value) is not int:
            raise TypeError('An integer must represent width')
        elif value < 0:
            raise ValueError('width must be greater >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter technique for __height getter.

        Returns:
            __height (int): Getter technique for height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """the 'height' setter method.

        Args:
            value (int): rectangle vertical measurement

        Attributes:
            __height (int): rectangle vertical dimension

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is not 0.

        """
        if type(value) is not int:
            raise TypeError('An integer must represent height')
        if value < 0:
            raise ValueError('width must be greater >= 0')
        self.__height = value
