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
            size (int): Kvadratın ölçüsü.
        """
        self.size = size

    @property
    def size(self):
        """
        __size atributunu əldə etmək üçün getter metodu.

        Returns:
            Kvadratın ölçüsü.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        __size atributunu təyin etmək üçün setter metodu.

        Args:
            value (int): Yeni ölçü dəyəri.

        Raises:
            TypeError: Əgər value tam ədəd deyilsə.
            ValueError: Əgər value 0-dan kiçikdirsə.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Kvadratın cari sahəsini hesablayır.

        Returns:
            Kvadratın sahəsi.
        """
        return self.__size ** 2
