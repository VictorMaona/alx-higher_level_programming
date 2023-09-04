#!/usr/bin/python3
"""2-rectangle class that can build upon and be extended.
"""


class Rectangle:
    """A rectangle is represented by this class.

    Args:
        width (int): Rectangle horizontal dimension by default is 0.
        height (int): Default value for rectangle vertical dimension is 0

    """
    def __init__(self, width=0, height=0):
        """Creates a new instance of Rectangle.

        Args:
            width (int): The width of the rectangle (which is 0 by default).
            height (int): The rectangle height (which is by default 0).
        """

    @property
    def width(self):
        """__width getter is 'width' getter method.

        Returns:
            __width (int): Dimensions of rectangle horizontal side

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): Dimensions of rectangle horizontal side

        Attributes:
            __width (int): rectangle horizontal measurement

        Raises:
            TypeError: When 'value' is not an int.
            ValueError: if 'value' is not or less 0.

        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must exceed zero be >= 0')
        self.__width = value

    @property
    def height(self):
        """__height getter for the 'height' parameter.

        Returns:
            __height (int): rectangle vertical measurement

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Method setter for 'height'.

        Args:
            value (int): rectangle vertical measurement

        Attributes:
            __height (int): rectangle vertical dimension

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('height must be integer')
        if value < 0:
            raise ValueError('height must exceed zero be >= 0')
        self.__height = value

    def area(self):
        """provides the rectangle area back.

        Returns:
            int: Rectangle size in terms of area __width * __height.
        """
        return self.__width * self.__height

    def perimeter(self):
        """gives back the perimeter of rectangle with the specified `width` and `height`

        Attributes:
            __width (int): Dimensions of rectangle horizontal side
            __height (int): rectangle vertical measurement

        Returns:
            0 if either attribute 0, or perimeter: (__width * 2) +
            (__height * 2).

        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
