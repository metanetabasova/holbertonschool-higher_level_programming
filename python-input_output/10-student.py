#!/usr/bin/python3
'''
Bu modul tekmillesdirilmis Student sinifini ehtiva edir
'''


class Student:
    '''
    Telebe melumatlarini saxlayan ve filtrasiya destekleyen sinif.
    '''

    def __init__(self, first_name, last_name, age):
        ''' 
        Student instansiyasini baslangicilasdirir.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        Student instansiyasinin luget tesvirini qaytarir.
        '''
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            res = {}
            for k in attrs:
                if k in self.__dict__:
                    res[k] = self.__dict__[k]
            return res
        return self.__dict__
