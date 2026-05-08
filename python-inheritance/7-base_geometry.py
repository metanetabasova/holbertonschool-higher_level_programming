#!/usr/bin/python3
"""BaseGeometry sinfi üçün modul."""


class BaseGeometry:
    """BaseGeometry sinfi."""

    def area(self):
        """area() metodunu təyin edir."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Dəyəri tam ədəd olub-olmamasına görə yoxlayır.
        
        Qeyd: Tapşırıqda 'name' həmişə string fərz edilir, 
        amma biz onu istifadə etməliyik.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
