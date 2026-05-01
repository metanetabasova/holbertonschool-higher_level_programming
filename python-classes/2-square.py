#!/usr/bin/python3
"""
Bu modul kvadratı təmsil edən Square sinfini təyin edir.
"""


class Square:
    """
    Kvadratı təmsil edən sinif.
    """

    def __init__(self, size=0):
        """
        Yeni bir Square instansiyası yaradır.

        Args:
            size (int): Kvadratın ölçüsü (defolt 0).

        Raises:
            TypeError: Əgər size integer deyilsə.
            ValueError: Əgər size 0-dan kiçikdirsə.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
