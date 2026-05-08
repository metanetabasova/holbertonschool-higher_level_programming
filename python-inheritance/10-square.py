#!/usr/bin/python3
"""
Bu modul Square sinfini təyin edir.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square sinfi üçün sənədləşdirmə."""

    def __init__(self, size):
        """
        Yeni Square nümunəsini başladır.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Square sinfi üçün sahəni hesablayan metod."""
        return self.__size ** 2
