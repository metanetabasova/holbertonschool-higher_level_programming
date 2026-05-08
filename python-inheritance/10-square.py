#!/usr/bin/python3
'''
Rectangle-dan miras alan Square sinfi
'''
Rectangle = __import__('9-rectangle')/Rectangle


class Square(Rectangle):
    '''Square sinifi'''

    def __init__(self, size):
        '''
        Yeni Square yaradir
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    
    def area(self):
        '''Kvadratin sahesini hesablayir'''
        return self.__size ** 2
