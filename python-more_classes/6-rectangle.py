#!/usr/bin/python3
"""Bu modul instansiya sayını izləyən Rectangle klasını təyin edir."""


class Rectangle:
    """Düzbucaqlını təmsil edən və sayını izləyən klas."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Yeni bir Rectangle yaradır."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Eni geri qaytarır."""
        return self.__width

    @width.setter
    def width(self, value):
        """Eni təyin edir."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Hündürlüyü geri qaytarır."""
        return self.__height

    @height.setter
    def height(self, value):
        """Hündürlüyü təyin edir."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Sahəni qaytarır."""
        return self.__width * self.__height

    def perimeter(self):
        """Perimetri qaytarır."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Düzbucaqlını '#' ilə çəkir."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Obyektin kod təmsilini qaytarır."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Obyekt silinəndə sayğacı azaldır."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
