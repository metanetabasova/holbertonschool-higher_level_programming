#!/usr/bin/python3
'''
bu modul basegeometry-de rectangle sinifi ucundur
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    BaseGeometry-den miras alan duzbucaqli sinifi
    '''

    def __init__(self, width, height):
        '''
        Yeni Rectangle numunesi yaradir
        '''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
