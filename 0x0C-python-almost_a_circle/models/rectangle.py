#!/usr/bin/python3
'''Model Rectangle'''


from models.base import Base


class Rectangle(Base):
    '''Class Rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Define constructor'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        '''Define function str'''
        x = self.__x
        y = self.__y
        width = self.__width
        height = self.__height
        form = type(self).__name__
        txt = "[" + form + "] "
        txt += "(" + str(self.id) + ") "
        txt += str(x) + "/" + str(y) + " - "
        txt += str(width) + "/" + str(height)
        return txt

    @property
    def width(self):
        '''Get width'''
        return self.__width

    @width.setter
    def width(self, width):
        '''Set width'''
        self.validator_integer("width", width, 1)
        self.__width = width

    @property
    def height(self):
        '''Get height'''
        return self.__height

    @height.setter
    def height(self, height):
        '''Set height'''
        self.validator_integer("height", height, 1)
        self.__height = height

    @property
    def x(self):
        '''Get x'''
        return self.__x

    @x.setter
    def x(self, x):
        '''Set x'''
        self.validator_integer("x", x, 2)
        self.__x = x

    @property
    def y(self):
        '''Get y'''
        return self.__y

    @y.setter
    def y(self, y):
        '''Set y'''
        self.validator_integer("y", y, 2)
        self.__y = y

    def validator_integer(self, name, value, flag):
        '''Validate integer'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if flag == 1:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        if flag == 2:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    def area(self):
        '''Function to calculate area of rectangle'''
        return self.__width * self.__height

    def display(self):
        '''Display rectangle'''
        if self.__x == 0:
            x = 0
        else:
            x = self.__x + 1

        if self.__y == 0:
            y = 0
        else:
            y = self.__y + 1

        for l in range(1, y):
            print()
        for i in range(self.__height):
            for k in range(1, x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        '''Update rectangle'''
        list = ['id', 'width', 'height', 'x', 'y']
        for i in range(len(args)):
            setattr(self, list[i], args[i])
        if len(args) == 0:
            for (key, value) in kwargs.items():
                setattr(self, key, value)
