#!/usr/bin/python3
'''
BaseGeometry sinifine integer_validator metodunu elave eden modul.
'''


class BaseGeometry:
    '''hendesi fiqurlar ucun'''

    def area(self):
        '''saheni hesablayir'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        deyerin musber tam eded oldugunu yoxlayir
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <=0:
            raise ValueError("{} must be greater than 0".format(name))
