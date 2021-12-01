#!/usr/bin/python3
'''Define class'''


class BaseGeometry:
    '''Class BaseGeometry'''
    def area(self):
        '''Method public area()'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validator'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
