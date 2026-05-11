#!/usr/bin/python3
'''
Bu modun Student sinifi ucundur
'''


class Student:
    '''Telebe melumatlarini saxlayan sinif.
    '''

    def __init__(self, first_name, last_name, age):
        '''
        Student instansiyasini baslangicidir.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            '''
            Student instansiyasinin luget tesvirini qaytarir
            '''
            return self.__dict__
