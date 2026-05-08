#!/usr/bin/python3
"""
Bu modul Rectangle-dan miras alan Square sinfini təyin edir.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square sinfi, Rectangle sinfindən miras alır."""

    def __init__(self, size):
        """
        Yeni Square nümunəsini başladır.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Kvadratın sahəsini hesablayır və qaytarır."""
        return self.__size ** 2

    def __str__(self):
        """Kvadratın [Square] <width>/<height> formatında təsvirini qaytarır."""
        return "[Square] {}/{}".format(self.__size, self.__size)
