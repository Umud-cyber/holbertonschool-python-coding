#!/usr/bin/python3
"""
This module defines a Square class.
"""

class Square:
    """Defines a square"""
    def __init__(self, size):
         # Assigning the incoming 'size' to the private attribute '__size'
        # the double underscore (__) tells python: "keep this hidden!"
        self.__size = size
