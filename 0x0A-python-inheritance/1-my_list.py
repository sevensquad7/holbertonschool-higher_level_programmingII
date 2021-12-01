#!/usr/bin/python3


'''File to class MyList'''


class MyList(list):
    '''Class MyList inheret object list'''
    def print_sorted(self):
        '''Print list sorted'''
        print(sorted(self))
