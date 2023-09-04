#!/usr/bin/python3
"""Gives techniques for representing a rectangle.
"""


class Rectangle:
    """gives techniques for calculating and printing while representing rectangle.

    Args:
        width (int): the width of the rectangle, which is 0 by default.
        height (int): The rectangle height the default value is 0.

    """
    def __init__(self, width=0, height=0):
        Initialize a Rectangle instance.

        Args:
            width (int): the width of the rectangle which is 0 by default.
            height (int): The rectangle height the default value is ).
        """

    @property
    def width(self):
        """__width getter the width attribute getter.

        Returns:
            __width (int): Dimensions of rectangle horizontal side

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): the width attribute setter

        Attributes:
            __width (int): Dimensions of rectangle's horizontal side

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than the 0.

        """
        if type(value) is not int:
            raise TypeError('An integer must represent width.')
        elif value < 0:
            raise ValueError('width must exceed zero >= 0')
        self.__width = value

    @property
    def height(self):
        """__height getter the height attribute.

        Returns:
            __height (int): rectangle vertical measurement

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): rectangle vertical measurement

        Attributes:
            __height (int): rectangle vertical measurement

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If the `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('An integer must represent height')
        if value < 0:
            raise ValueError('Height must be greater than zero >= 0')
        self.__height = value

    def area(self):
        """gives the area of a rectangle with the specified `width` and `height`.

        Attributes:
            __width (int): Dimensions of rectangle horizontal side
            __height (int): rectangle vertical measurement

        Returns:
            Area of rectangle: __width * __height

        """
        return self.__width * self.__height

    def perimeter(self):
        """returns the size of specified rectangle perimeter `width` and `height`

        Attributes:
            __width (int): Dimensions of rectangle horizontal side
            __height (int): Rectangle vertical measurement

        Returns:
            0 if perimeter is 0 or either attribute is 0: (__width * 2) +
            (__height * 2).

        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """Prints the rectangle that the current instance is currently represented
        by using a string of '#' and 'n' characters as its format.

        Attributes:
            __width (int): Dimensions of rectangle horizontal side
            __height (int): rectangle vertical measurement
            str (str): created string for return

        Returns:
            str (str): Provide string representation of the rectangle for printing.

        """
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += '#'
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __str__(self):
        """direct printing of instances is possible.

        Returns:
            array of characters that represents the rectangle and creates string.

        """
        return self._draw_rectangle()
