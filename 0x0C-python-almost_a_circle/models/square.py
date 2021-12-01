#!/usr/bin/python3
'''Model Square'''


from models.rectangle import Rectangle


class Square(Rectangle):
        '''Class Square'''

        def __init__(self, size, x=0, y=0, id=None):
                '''Define constructor'''
                super().__init__(size, size, x, y, id)

        def __str__(self):
                '''Define function str'''
                x = self.x
                y = self.y
                size = self.width
                form = type(self).__name__
                txt = "[" + form + "] "
                txt += "(" + str(self.id) + ") "
                txt += str(x) + "/" + str(y) + " - "
                txt += str(size)
                return txt

        @property
        def size(self):
                '''Get size'''
                return self.width

        @size.setter
        def size(self, size):
                '''Set size'''
                self.width = size
                self.height = size

        def update(self, *args, **kwargs):
                '''Update square'''
                list = ['id', 'size', 'x', 'y']
                for i in range(len(args)):
                        setattr(self, list[i], args[i])
                if len(args) == 0:
                        for (key, value) in kwargs.items():
                                setattr(self, key, value)
