#!/usr/bin/python3
"""Establishes the Rectangle class."""


class Rectangle:
    """Create a rectangle.

    Attributes:
        number_of_instances (int): How many Rectangle instances there are.
        print_symbol (any): the mark utilized to signify strings.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """start a new Rectangle.

        Args:
            width (int): The new rectangle length is width.
            height (int): The new rectangle length is height.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Obtain or modify the rectangle width."""
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
        """Get or change the rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer.")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Give me the rectangle area back."""
        return (self.__width * self.__height)

    def perimeter(self):
        """The rectangle perimeter should be returned."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """the Rectangle with the larger area back.

        Args:
            rect_1 (Rectangle): first Rectangle.
            rect_2 (Rectangle): second Rectangle.
        Raises:
            TypeError: If rect_1 or rect_2 is not Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """Deliver the Rectangle printable representation once more.

        uses the letter # to symbolize the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """The Rectangle string representation should be returned."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Every time a rectangle is deleted print a message."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
