#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """Defines a square with size validation and an area method."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): Size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
