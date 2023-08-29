#!/usr/bin/python3
"""rendering of a square."""


class Square:
    """Create a square."""

    def __init__(self, size=0, position=(0, 0)):
        """start a fresh Square.

        Args:
            size (int): New size square dimensions.
            position (int, int): The new square is situated.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """determine or alter square current size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Find or change square current location."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be 2 of positive integers tuple.")
        self.__position = value

    def area(self):
        """revert to the square current area."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the # symbol in the square."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
