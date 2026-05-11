#!/usr/bin/python3
'''
Bu modul obyektin atributlarını JSON seriyalaşdırması üçün
lüğət şəklində qaytaran funksiyanı ehtiva edir.
'''


def class_to_json(obj):
    '''
    Sinfin instansiyasinin luget tesvirini qaytarir.
    '''
    return obj.__dict__
