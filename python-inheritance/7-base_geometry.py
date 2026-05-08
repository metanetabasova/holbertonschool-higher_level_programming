#!/usr/bin/python3
"""BaseGeometry sinfi üçün modul."""


class BaseGeometry:
    """BaseGeometry sinfi."""

    def area(self):
        """Sahəni hesablayan metod."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Dəyərin tam ədəd olub-olmadığını yoxlayır."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
