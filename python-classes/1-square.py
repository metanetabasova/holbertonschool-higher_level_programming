#!/usr/bin/python3
"""
Bu modul kvadratı (Square) təmsil edən sinfi ehtiva edir.
"""


class Square:
    """
    Kvadrat sinfi.

    Attributes:
        __size (int): Kvadratın tərəfinin ölçüsü.
    """

    def __init__(self, size):
        """
        Yeni bir Square obyekti yaradır.

        Args:
            size: Kvadratın ölçüsü (növ və dəyər yoxlanışı yoxdur).
        """
        self.__size = size  
