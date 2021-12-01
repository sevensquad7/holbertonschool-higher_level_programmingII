#!/usr/bin/python3
"""Class Square"""


class Square:

    """Define Constructor"""
    def __init__(self, size=0):
        try:
            if type(size) is not int:
                raise TypeError
            if size < 0:
                raise ValueError
            self.__size = size
        except ValueError:
            print("size must be >= 0", end="")
            raise
        except TypeError:
            print("size must be an integer", end="")
            raise

    """Calculate area"""
    def area(self):
        return self.__size ** 2
