#!/usr/bin/python3
'''Define Class'''


class Base:
    '''Class Base'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id
