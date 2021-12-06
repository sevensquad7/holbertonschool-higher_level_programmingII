#!/usr/bin/python3
"""
class Task
"""


class MyInt(int):
    """ MyInt Class """
    def __eq__(self, other):
        if isinstance(self, type(other)):
            return False

    def __ne__(self, other):
        if isinstance(self, type(other)):
            return True
