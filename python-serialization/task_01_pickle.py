#!/usr/bin/python3
'''
Bu modul pickle modulu vasitəsilə fərdi obyektlərin
seriyalaşdırılması və deserilizasiyasını həyata keçirir.
'''
import pickle


class CustomObject:
    '''
    Ferdi melumatlari saxlayan ve pickle destekleyen sinif.
    '''

    def __init__(self, name, age, is_student):
        '''Obyekti baslangicilasdirir.'''
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        '''Obyektin atributlarini teleb olunan formatda cap edir.'''
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        '''
        Cari obyekti pickle vasitesile fayla yazir
        '''
        try:
            with opem(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        '''
        Fayldan obyekti yukleyir ve CustomObject instansiyasi qaytarir.
        '''
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.PickleError, OSError):
            return None
