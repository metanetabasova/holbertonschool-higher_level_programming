#!/usr/bin/python3
'''Rectangle klasini teyin edir'''
class Rectangle:
    '''Duzbucaqlini temsil eden klass'''
    def __init__(self, width=0, height=0):
        '''yeni bir rectangle instansiyasi yaradir'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''eni geri qaytarir'''
        return self.__width
    
    @width.setter
    def width(self, value):
        '''eni teyin edir'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''hundurluyu geri qaytarir'''
        return self.__height

    @height.setter
    def height(self, value):
        '''hundurluyu teyin edir'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''saheni qaytarir'''
        return self.__width * self.__height

    def perimeter(self):
        """Perimetri qaytarır."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        '''duzbucaqlini '#' simvollari ile cekir'''
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = []
        for i in range(self.__height):
            rect_str.append("#" * self.__width)
        return "/n".join(rect_str)

    def __repr__(self):
        '''obyektin yeniden yaradilmasi ucun string temsilini qaytarir'''
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        '''obyekt silindikde bu mesaji cap edir'''
        print("Bye rectangle...")
