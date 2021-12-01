#!/usr/bin/python3
'''File function inherits_from'''


def inherits_from(obj, a_class):
    '''Function inherits_from'''
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
