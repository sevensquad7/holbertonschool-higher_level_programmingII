#!/usr/bin/python3
"""Class Square"""


class Square:

    """Define Constructor"""
    def __init__(self, size=0, position=(0, 0)):
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

        try:
            self.position = position
        except:
            pass

    """Calculate area"""
    def area(self):
        return self.__size ** 2

    """Getter Size"""
    @property
    def size(self):
        return self.__size

    """Setter Size"""
    @size.setter
    def size(self, value):
        try:
            if type(value) is not int:
                raise TypeError
            self.__size = value
        except TypeError:
            print("size must be an integer", end="")
            raise

    """Getter Position"""
    @property
    def position(self):
        return self.__position

    """Setter Position"""
    @position.setter
    def position(self, value):
        count = 0
        message = "position must be a tuple of 2 positive integers"
        try:
            if type(value) is not tuple:
                raise TypeError(message)
            if len(value) != 2:
                raise TypeError(message)
            for i in range(0, len(value)):
                if type(value[i]) is not int:
                    raise TypeError(message)
                if value[i] < 0:
                    raise TypeError(message)
            self.__position = value
        except TypeError as e:
            print("{}".format(e))

    """"Define my_print"""
    def my_print(self):
        space = " "
        other = ""
        try:
            if self.__position[1] < 0:
                space = ""
            if self.__size == 0:
                print("")
            else:
                for i in range(self.__position[1]):
                    print()
            for i in range(0, self.__size):
                other = space
                for j in range(0, self.__size):
                    for k in range(0, self.__position[0]):
                        print("{}".format(other), end="")
                    other = ""
                    print("#", end="")
                print("")
        except:
            pass
