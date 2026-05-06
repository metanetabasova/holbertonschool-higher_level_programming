#!/usr/bin/python3
"""Bu modul fərqli çap simvolları dəstəkləyən Rectangle klasını təyin edir."""


class Rectangle:
    """Düzbucaqlını təmsil edən klas.

    Atributlar:
        number_of_instances (int): Yaradılmış obyektlərin sayı.
        print_symbol (any): Vizuallaşdırma üçün istifadə olunan simvol.
    """

    number_of_instances = 0
    print_symbol = "#"

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
        """Düzbucaqlını print_symbol ilə vizuallaşdırır."""
        if self.__width == 0 or self.__height == 0:
            return ""
        
        # print_symbol istənilən tip ola biləcəyi üçün onu string-ə çeviririk
        symbol = str(self.print_symbol)
        rect_lines = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(rect_lines)

    def __repr__(self):
        """Obyektin kod təmsilini qaytarır."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Obyekt silinəndə mesaj verir və sayğacı azaldır."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
