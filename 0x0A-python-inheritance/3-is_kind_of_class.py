#!/usr/bin/python3
'''File function kind of class'''


def is_kind_of_class(obj, a_class):
    '''Kind of class'''
    if type(obj) is a_class or isinstance(obj, a_class):
        return True
    return False
