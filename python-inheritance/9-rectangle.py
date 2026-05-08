#!/usr/bin/python3
'''
bu modul basegeometry- den miras alan rectangle sinifi ucundur
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''BaseGeometry-den miras alan rectangle sinifi'''

    def __init__(self, width, height):
        '''yeni rectangle yaradir'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        '''duzbucaqlinin sahesini hesablayir ve qaytarir'''
        return self.__width * self.__height

    def __str__(self):
        '''duzbucaqlinin tesvirini qaytarir'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
