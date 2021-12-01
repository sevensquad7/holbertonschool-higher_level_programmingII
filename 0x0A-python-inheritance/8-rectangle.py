#!/usr/bin/python3
'''Documentation class'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Class Rectangle inheret BaseGeometry'''
    def __init__(self, width, height):
        '''Define constructor'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
