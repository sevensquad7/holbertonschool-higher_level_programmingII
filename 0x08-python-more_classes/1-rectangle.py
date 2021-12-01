#!/usr/bin/python3
'''Defined Class Rectangle'''


class Rectangle:
    '''
    Class Rectangle
    '''
    def __init__(self, width=0, height=0):
        '''Defined constructor'''
        self.height = height
        self.width = width

    @property
    def width(self):
        '''Getter width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Getter height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
