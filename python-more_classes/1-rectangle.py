#!/usr/bin/python3
'''Bu modul en ve hundurluyu olan rectangle klasini teyin edir.'''


class Rectangle:
    '''Duzbucaqlini teyin eden klas.'''

    def __init__(self, width=0, height=0):
        '''Yeni bir Rectangle instansiyasi yaradilir.'''

        self.width = width
        self.height = height

    @property
    def width(self):
        '''eni qaytarmaq ucun'''
        return self .__width

    @width.setter
    def width(self, value):
        '''eni teyin etmek ucun(yoxlama ile).'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self .__width = value

    @property
    def height(self):
        '''hundurluyu geri qaytarmaq ucun.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Hundurluyu teyin etmek ucun (yoxlama ile).'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
